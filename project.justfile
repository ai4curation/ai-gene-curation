## Add your own just recipes here. This is imported by the main justfile.

# Build static site from gene markdown files
build-site:
    uv run build-site

# Build and serve the site
build-and-serve: build-site
    uv run mkdocs serve

# Split markdown gene files into YAML format
split-genes-to-yaml:
    uv run split-genes-to-yaml --input genes --output yaml

# Generate project artifacts from LinkML schema
gen-project:
    uv run gen-project src/ai_gene_curation/schema/gene_curation.yaml -d assets

validate-full: validate test

validate: split-genes-to-yaml _validate_yaml check-terms-yaml check-publications-yaml

_validate_yaml:
    uv run linkml-validate -s src/ai_gene_curation/schema/gene_curation.yaml yaml/*.yaml

# Check term labels against OAK ontologies (write to file)
check-terms:
    uv run check-term-labels genes -o term_label_mismatches.tsv

# Check terms in YAML files (write to file)
check-terms-yaml:
    uv run check-term-labels yaml -o term_label_mismatches.tsv

# Check terms and output to stdout (can be piped)
check-terms-stdout:
    @uv run check-term-labels yaml 2>/dev/null

# Check publication titles against PubMed
check-publications:
    uv run check-publication-titles genes -o publication_title_mismatches.tsv

# Check publication titles in YAML files
check-publications-yaml:
    uv run check-publication-titles yaml -o publication_title_mismatches.tsv

# Check publications and output to stdout
check-publications-stdout:
    @uv run check-publication-titles yaml 2>/dev/null

# Cache PubMed publications locally
cache-pmids *PMIDS:
    uv run cache-publications cache {{PMIDS}}

# Cache publications from a file of PMIDs
cache-pmids-from-file FILE:
    uv run cache-publications from-file {{FILE}}
