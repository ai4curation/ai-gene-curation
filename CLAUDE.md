# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered gene curation project focused on agentic collaborative curation of genes. The project uses Python with LinkML for data modeling and includes structured gene annotation data following Gene Ontology (GO) standards.

## Curation Guidelines

### Evidence

Evidence should be as direct as possible. When the evidence is from a publication, `supporting_text` should be included.
For molecular functions, direct assays (IDA) are better than other experimental forms, but where the inference is
from multiple lines of evidence or a review, TAS is often preferred.

It may seem counter-intuitive, but phylogenetic evidence (IBA) is the best because it has been reviewed by PAINT curators.

BAD:

```
    activity:
      term:
        id: GO:0003700
        label: DNA-binding transcription factor activity
      support:
        - reference: PMID:8650545
          title: "XTcf-3 transcription factor mediates beta-catenin-induced axis formation in Xenopus embryos"
          evidence_type: IDA
```

GOOD:

```
    activity:
      term:
        id: GO:0003700
        label: DNA-binding transcription factor activity
      support:
        - reference: GO_REF:0000033
          title: Phylogenetic evidence
          evidence_type: IBA
```

But ONLY include this if you get this from uniprot/amigo

## Development Commands

These instructions are only relevant for technical changes to the repo

### Essential Commands
- **Install dependencies:** `uv sync --group dev`
- **Run tests:** `just test` (runs pytest, mypy, and ruff)
- **Run pytest only:** `uv run pytest`
- **Type checking:** `uv run mypy src tests`
- **Linting:** `uv run ruff check .`
- **Run CLI:** `uv run ai-gene-curation --name <name>`
- **Documentation server:** `uv run mkdocs serve`
- **Validate gene data:** `just validate` (splits markdown to YAML and validates against schema)

### Command-Line Tools
The following CLI tools are available after installation:
- **`split-genes-to-yaml`:** Split markdown files with YAML frontmatter into pure YAML files
  - Usage: `uv run split-genes-to-yaml --input genes --output yaml`
- **`check-term-labels`:** Check ontology term labels against OAK
  - Usage: `uv run check-term-labels genes -o term_label_mismatches.tsv`
  - Writes to stdout if no output file specified
- **`check-publication-titles`:** Check publication titles against PubMed
  - Usage: `uv run check-publication-titles genes -o publication_title_mismatches.tsv`
  - Validates that title fields in Evidence objects match actual PubMed titles
  - Reports missing titles, mismatched titles, and fetch errors
- **`cache-publications`:** Cache PubMed/PMC publications locally with frontmatter
  - Usage: `uv run cache-publications cache PMID:12345678 PMID:87654321`
  - Can fetch from file: `uv run cache-publications from-file pmids.txt`
  - Fetches abstracts from PubMed and full text from PMC when available
  - Stores in `publications/` directory as `PMID_12345678.md`

### Test Commands
- **Full test suite:** `just test-full` (includes integration tests)
- **Doctests:** `uv run pytest --doctest-modules src` (runs doctests for all modules)

## Architecture

### Key Components
- **Gene Data:** `/genes/` directory contains structured markdown files with gene annotations following a YAML frontmatter format with GO terms and primary functions
- **LinkML Integration:** Project uses LinkML for data modeling with runtime validation

### Gene File Structure
Gene files (e.g., `genes/STAT1.md`) contain:
- YAML frontmatter with UniProt ID, symbol, primary functions (GO terms)
- Markdown body with detailed functional descriptions
- Structured annotations following Gene Ontology standards

## Data Schema

### Overview
The project uses a LinkML schema (`src/ai_gene_curation/schema/gene_curation.yaml`) to define and validate the structure of gene annotation data. Gene information is authored in markdown files with YAML frontmatter, then validated against this schema.

### Core Schema Components

#### GeneInfo
The root entity representing a gene with:
- `id`: UniProt identifier (e.g., UniProtKB:P42224)
- `symbol`: Gene symbol (e.g., STAT1)
- `primary_functions`: List of functional annotations
- `phenotypes`: List of mutation-phenotype associations

#### GeneFunctionBlock
Describes a primary function of the gene:
- `description`: Textual description of the function
- `activity`: Molecular function (GO term with evidence)
- `location`: Cellular component where function occurs (GO terms like GO:0005634 for nucleus)
- `complex`: Optional - protein complex where function occurs (GO terms like GO:0070721 for ISGF3 complex)
- `cell_type`: Optional - specific cell type where function occurs (CL terms like CL:0000182 for hepatocyte)
- `gross_anatomy`: Optional - anatomical location where function occurs (UBERON terms like UBERON:0002107 for liver)
- `upstream`: Upstream regulatory components
- `downstream`: Downstream targets/effects
- `processes`: Biological processes involved
- `roles`: Additional functional roles

#### AnnotationUnit
Represents a single annotation with:
- `term`: Ontology term (id, label/name)
- `support`: Evidence supporting the annotation
- `description`: Optional descriptive text
- `mechanism`: Optional mechanism description
- `is_any_of`: For specifying alternative terms
- `category`: Optional categorization (e.g., "over-annotation")

#### Evidence
Supporting evidence for annotations:
- `reference`: Publication ID (e.g., PMID:12345678) or reference (e.g., GO_REF:0000033)
- `evidence_type`: Evidence code (e.g., IDA, IBA, ISS, TAS)

#### PhenotypeBlock
Links mutations to phenotypic effects:
- `mutation`: Mutation details
  - `type`: Type of mutation (e.g., loss_of_function, gain_of_function)
  - `variant`: Optional variant context (e.g., somatic, germline, dominant_negative)
- `effects`: List of phenotypic consequences with HPO terms

### Data Validation

The `just validate` command performs two steps:

1. **Split Markdown to YAML**: Extracts YAML frontmatter from markdown files in `/genes/` and saves as pure YAML files in `/yaml/`
2. **Schema Validation**: Validates the YAML files against the LinkML schema using `linkml-validate`

To validate your gene annotations:
```bash
just validate
```

This ensures:
- All required fields are present
- Data types are correct
- Ontology term structures are valid
- Evidence codes follow expected patterns

### Additional Validation Commands
- `just check-terms`: Verify term labels match ontology definitions using OAK
- `just check-terms-yaml`: Check terms in generated YAML files

## Tool Stack
- **Package Manager:** uv (version 0.6+)
- **Build System:** Hatchling with uv-dynamic-versioning
- **Task Runner:** just (command recipes in justfile)
- **Testing:** pytest with mypy for type checking
- **Linting:** ruff
- **Documentation:** MkDocs with Material theme

## Git Workflow
- Main branch: `main`
- Project uses conventional commits
- GitHub Actions configured for CI/CD