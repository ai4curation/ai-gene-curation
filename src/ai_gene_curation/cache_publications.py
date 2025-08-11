#!/usr/bin/env python
"""Cache PubMed/PMC publication texts with frontmatter metadata."""

import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import typer
from typing_extensions import Annotated
from Bio import Entrez  # type: ignore[import-untyped]
import time
import xml.etree.ElementTree as ET
from yaml import dump  # type: ignore

# Set email for NCBI (required for Entrez)
Entrez.email = "ai-gene-curation@example.com"  # type: ignore


@dataclass
class Publication:
    """Represents a publication with metadata and content."""
    pmid: str
    title: str
    authors: List[str]
    journal: str
    year: str
    abstract: str
    full_text: Optional[str] = None
    pmcid: Optional[str] = None
    doi: Optional[str] = None
    keywords: Optional[List[str]] = None
    
    def to_frontmatter_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for YAML frontmatter."""
        data = {
            'pmid': self.pmid,
            'title': self.title,
            'authors': self.authors,
            'journal': self.journal,
            'year': self.year,
        }
        if self.pmcid:
            data['pmcid'] = self.pmcid
        if self.doi:
            data['doi'] = self.doi
        if self.keywords:
            data['keywords'] = self.keywords
        return data
    
    def to_markdown(self) -> str:
        """Generate markdown content with frontmatter."""
        # Create frontmatter
        frontmatter = dump(self.to_frontmatter_dict(), 
                          default_flow_style=False, 
                          allow_unicode=True, 
                          sort_keys=False)
        
        # Create markdown body
        body_parts = [f"# {self.title}\n"]
        
        if self.authors:
            body_parts.append(f"**Authors:** {', '.join(self.authors)}\n")
        
        body_parts.append(f"**Journal:** {self.journal} ({self.year})\n")
        
        if self.doi:
            body_parts.append(f"**DOI:** [{self.doi}](https://doi.org/{self.doi})\n")
        
        if self.pmcid:
            body_parts.append(f"**PMC:** [{self.pmcid}](https://www.ncbi.nlm.nih.gov/pmc/articles/{self.pmcid}/)\n")
        
        body_parts.append(f"\n## Abstract\n\n{self.abstract}\n")
        
        if self.full_text:
            body_parts.append(f"\n## Full Text\n\n{self.full_text}\n")
        
        return f"---\n{frontmatter}---\n\n{''.join(body_parts)}"


def extract_pmid(pmid_str: str) -> str:
    """
    Extract PMID from various formats.
    
    >>> extract_pmid('12345678')
    '12345678'
    >>> extract_pmid('PMID:12345678')
    '12345678'
    >>> extract_pmid('pmid: 12345678')
    '12345678'
    >>> extract_pmid('PMID12345678')
    '12345678'
    """
    # Remove PMID prefix and clean up
    pmid = re.sub(r'^(PMID|pmid)[:\s]*', '', pmid_str.strip())
    return pmid


def fetch_pubmed_data(pmid: str) -> Optional[Publication]:
    """
    Fetch publication data from PubMed.
    
    Returns Publication object with abstract, or None if not found.
    """
    try:
        # Fetch summary from PubMed
        handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
        summary_records = Entrez.read(handle)
        handle.close()
        
        if not summary_records or 'error' in summary_records[0]:
            return None
        
        record = summary_records[0]
        
        # Extract basic metadata (convert Bio.Entrez objects to strings)
        title = str(record.get('Title', 'No title'))
        authors = [str(author) for author in record.get('AuthorList', [])]
        journal = str(record.get('Source', 'Unknown journal'))
        year = str(record.get('PubDate', 'Unknown'))[:4] if 'PubDate' in record else 'Unknown'
        doi = str(record.get('DOI', '')) if record.get('DOI') else None
        
        # Check for PMC ID - try multiple methods
        pmcid = None
        
        # Method 1: Check ArticleIds
        if 'ArticleIds' in record:
            article_ids = record['ArticleIds']
            if isinstance(article_ids, dict):
                for id_type, id_value in article_ids.items():
                    if 'pmc' in str(id_type).lower():
                        pmcid = str(id_value)
                        break
        
        # Method 2: Use Entrez elink to find PMC ID
        if not pmcid:
            try:
                handle = Entrez.elink(dbfrom="pubmed", db="pmc", id=pmid)
                link_records = Entrez.read(handle)
                handle.close()
                
                if link_records and link_records[0].get('LinkSetDb'):
                    for linkset in link_records[0]['LinkSetDb']:
                        if linkset.get('DbTo') == 'pmc' and linkset.get('Link'):
                            pmcid = 'PMC' + str(linkset['Link'][0]['Id'])
                            break
            except Exception:
                pass
        
        # Fetch abstract from PubMed
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
        abstract_text = handle.read()
        handle.close()
        
        # Clean up abstract
        abstract = abstract_text.strip()
        if not abstract or abstract == "":
            abstract = "No abstract available."
        
        publication = Publication(
            pmid=pmid,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            abstract=abstract,
            pmcid=pmcid,
            doi=doi
        )
        
        # Try to fetch full text from PMC if available
        if pmcid:
            full_text = fetch_pmc_fulltext(pmcid)
            if full_text:
                publication.full_text = full_text
        
        return publication
        
    except Exception as e:
        typer.echo(f"Error fetching PMID {pmid}: {e}", err=True)
        return None


def fetch_pmc_fulltext(pmcid: str) -> Optional[str]:
    """
    Fetch full text from PMC.
    
    Returns full text as string, or None if not available.
    """
    try:
        # Remove PMC prefix if present
        pmcid = pmcid.replace('PMC', '')
        
        # Fetch full text XML from PMC
        handle = Entrez.efetch(db="pmc", id=pmcid, rettype="full", retmode="xml")
        xml_data = handle.read()
        handle.close()
        
        # Parse XML to extract text
        root = ET.fromstring(xml_data)
        
        # Extract body text (simplified - could be enhanced)
        body_texts = []
        for elem in root.iter():
            if elem.tag in ['p', 'sec']:
                text = ''.join(elem.itertext()).strip()
                if text:
                    body_texts.append(text)
        
        if body_texts:
            return '\n\n'.join(body_texts)
        
    except Exception as e:
        typer.echo(f"Could not fetch full text for PMC{pmcid}: {e}", err=True)
    
    return None


def cache_publication(pmid: str, output_dir: Path, force: bool = False) -> bool:
    """
    Cache a single publication.
    
    Returns True if successfully cached, False otherwise.
    """
    # Clean PMID
    pmid = extract_pmid(pmid)
    
    # Check if already cached
    output_file = output_dir / f"PMID_{pmid}.md"
    if output_file.exists() and not force:
        typer.echo(f"PMID {pmid} already cached (use --force to re-download)", err=True)
        return True
    
    # Fetch publication data
    typer.echo(f"Fetching PMID {pmid}...", err=True)
    publication = fetch_pubmed_data(pmid)
    
    if not publication:
        typer.echo(f"Failed to fetch PMID {pmid}", err=True)
        return False
    
    # Write to file
    output_file.write_text(publication.to_markdown())
    
    if publication.full_text:
        typer.echo(f"Cached PMID {pmid} with full text from PMC", err=True)
    else:
        typer.echo(f"Cached PMID {pmid} with abstract only", err=True)
    
    return True


app = typer.Typer(help="Cache PubMed/PMC publications locally")


@app.command()
def cache(
    pmids: Annotated[List[str], typer.Argument(help="PMID(s) to cache")],
    output_dir: Annotated[Path, typer.Option("-o", "--output", help="Output directory")] = Path("publications"),
    force: Annotated[bool, typer.Option("-f", "--force", help="Force re-download even if cached")] = False,
    delay: Annotated[float, typer.Option("-d", "--delay", help="Delay between requests (seconds)")] = 0.5,
):
    """Cache PubMed/PMC publications with metadata."""
    
    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each PMID
    success_count = 0
    for i, pmid in enumerate(pmids):
        if i > 0:
            time.sleep(delay)  # Be polite to NCBI servers
        
        if cache_publication(pmid, output_dir, force):
            success_count += 1
    
    typer.echo(f"\nCached {success_count}/{len(pmids)} publications", err=True)


@app.command()
def from_file(
    input_file: Annotated[Path, typer.Argument(help="File containing PMIDs (one per line)")],
    output_dir: Annotated[Path, typer.Option("-o", "--output", help="Output directory")] = Path("publications"),
    force: Annotated[bool, typer.Option("-f", "--force", help="Force re-download even if cached")] = False,
    delay: Annotated[float, typer.Option("-d", "--delay", help="Delay between requests (seconds)")] = 0.5,
):
    """Cache publications from a file of PMIDs."""
    
    if not input_file.exists():
        typer.echo(f"Error: {input_file} not found", err=True)
        raise typer.Exit(1)
    
    # Read PMIDs from file
    pmids = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                pmids.append(line)
    
    if not pmids:
        typer.echo("No PMIDs found in file", err=True)
        raise typer.Exit(1)
    
    typer.echo(f"Found {len(pmids)} PMIDs to cache", err=True)
    
    # Use the cache command
    cache(pmids, output_dir, force, delay)


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()