---
id: UniProtKB:P25054
symbol: APC
primary_functions:
- description: Functions as a scaffold protein in the β-catenin destruction complex,
    promoting phosphorylation and degradation of β-catenin to negatively regulate
    Wnt signaling. This tumor suppressor function is essential for preventing aberrant
    cell proliferation.
  activity:
    term:
      id: GO:0008013
      label: beta-catenin binding
    support:
    - reference: PMID:8259519
      title: Association of the APC tumor suppressor protein with catenins
      evidence_type: IPI
    description: Binds β-catenin through 15 and 20 amino acid repeats, creating multiple
      binding sites for efficient sequestration
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    description: Primarily cytoplasmic, enriched at cell periphery and microtubule
      plus-ends
  complex:
    term:
      id: GO:0030877
      label: beta-catenin destruction complex
    support: []
    description: Core component with Axin1/2, GSK3α/β, and CK1α, providing scaffold
      for β-catenin phosphorylation
  upstream:
  - term:
      id: GO:0070411
      label: I-SMAD binding
    support: []
    description: Binds Axin1/2 through SAMP repeats to organize destruction complex
    mechanism: Three SAMP repeats mediate Axin RGS domain interaction
  - term:
      id: GO:0034236
      label: protein kinase A catalytic subunit binding
    support: []
    description: Facilitates GSK3β and CK1α binding for β-catenin phosphorylation
  downstream:
  - term:
      id: GO:0090090
      label: negative regulation of canonical Wnt signaling pathway
    support: []
    description: Promotes β-catenin phosphorylation and degradation
  - term:
      id: GO:0006511
      label: ubiquitin-dependent protein catabolic process
    support: []
    description: Facilitates β-catenin ubiquitination by β-TrCP E3 ligase
  processes:
  - term:
      id: GO:0016055
      label: Wnt signaling pathway
    support:
    - reference: PMID:8259519
      title: Association of the APC tumor suppressor protein with catenins
      evidence_type: IDA
  - term:
      id: GO:0030178
      label: negative regulation of Wnt signaling pathway
    support: []
  roles:
  - term:
      id: GO:0051434
      label: BH3 domain binding
    support: []
    description: Key scaffold organizing destruction complex
- description: Regulates microtubule dynamics and cell migration through interactions
    with microtubule plus-ends and associated proteins. This function is important
    for cell polarity, chromosome segregation, and directed cell migration.
  activity:
    term:
      id: GO:0008017
      label: microtubule binding
    support: []
    description: Binds and stabilizes microtubule plus-ends via basic domain
  location:
    term:
      id: GO:0000922
      label: spindle pole
    support: []
    description: Localizes to spindle poles during mitosis
  complex:
    term:
      id: GO:0008021
      label: synaptic vesicle
    support: []
    description: Found at synapses in neurons
  downstream:
  - term:
      id: GO:0031122
      label: cytoplasmic microtubule organization
    support: []
    description: Promotes microtubule assembly and stability
  - term:
      id: GO:0030335
      label: positive regulation of cell migration
    support: []
    description: Coordinates microtubules for directed migration
  processes:
  - term:
      id: GO:0007026
      label: negative regulation of microtubule depolymerization
    support: []
  - term:
      id: GO:0000278
      label: mitotic cell cycle
    support: []
  - term:
      id: GO:0051301
      label: cell division
    support: []
  roles:
  - term:
      id: GO:0015631
      label: tubulin binding
    support: []
    description: Regulates cytoskeleton organization
- description: Maintains intestinal epithelial homeostasis by regulating stem cell
    proliferation and differentiation in the intestinal crypts. APC is essential for
    controlling the Wnt gradient that governs the crypt-villus axis.
  activity:
    term:
      id: GO:2000178
      label: negative regulation of neural precursor cell proliferation
    support: []
    description: Controls proliferation of intestinal stem cells and transit-amplifying
      cells
  location:
    term:
      id: GO:0060077
      label: inhibitory synapse
    support: []
    description: High expression in differentiated villus epithelium, lower in crypts
  downstream:
  - term:
      id: GO:0045596
      label: negative regulation of cell differentiation
    support: []
    description: Promotes differentiation of intestinal epithelial cells
  - term:
      id: GO:0043066
      label: negative regulation of apoptotic process
    support: []
    description: Regulates apoptosis at crypt-villus junction
  processes:
  - term:
      id: GO:0048730
      label: epidermis morphogenesis
    support: []
  - term:
      id: GO:0060729
      label: intestinal epithelial structure maintenance
    support: []
  - term:
      id: GO:0098727
      label: maintenance of cell number
    support: []
  roles:
  - term:
      id: GO:0140297
      label: DNA-binding transcription factor binding
    support: []
    description: Critical gatekeeper of intestinal homeostasis
phenotypes:
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0003003
      label: Colon cancer
    description: Familial adenomatous polyposis with hundreds to thousands of adenomas
    support:
    - reference: PMID:7795585
      title: 'Familial adenomatous polyposis: desmoid tumours and lack of ophthalmic
        lesions (CHRPE) associated with APC mutations beyond codon 1444'
      supporting_text: Classic FAP is characterized by hundreds to thousands of adenomatous
        colonic polyps, beginning on average at age 16 years (range 7-36 years). For
        those with the classic form of FAP, 95% of individuals have polyps by age
        35 years; CRC is inevitable without colectomy.
      evidence_type: TAS
  - term:
      id: MONDO:0021056
      label: Familial adenomatous polyposis
    description: Autosomal dominant syndrome with near 100% penetrance for colorectal
      cancer
    support:
    - reference: PMID:15108286
      title: Mutation analysis of the adenomatous polyposis coli (APC) gene in Danish
        patients with familial adenomatous polyposis (FAP)
      supporting_text: Familial adenomatous polyposis (FAP) is an autosomal dominant
        colorectal cancer predisposition syndrome with near 100% penetrance. The mean
        age of CRC diagnosis in untreated individuals is 39 years (range 34-43 years).
      evidence_type: TAS
  - term:
      id: HP:0100244
      label: Fibroma
    description: Desmoid tumors in 10-15% of FAP patients
    support:
    - reference: PMID:7795585
      title: 'Familial adenomatous polyposis: desmoid tumours and lack of ophthalmic
        lesions (CHRPE) associated with APC mutations beyond codon 1444'
      supporting_text: Desmoid tumors are a group of benign, invasive, solid tumors
        that are relatively rare in the general population, but can occur in up to
        21% of patients with Familial Adenomatous Polyposis (FAP). They can be difficult
        to treat and have high rates of recurrence even after resection.
      evidence_type: IEP
  - term:
      id: HP:0009593
      label: Abnormality of the retinal pigment epithelium
    description: Congenital hypertrophy of retinal pigment epithelium (CHRPE)
    support:
    - reference: PMID:7795585
      title: 'Familial adenomatous polyposis: desmoid tumours and lack of ophthalmic
        lesions (CHRPE) associated with APC mutations beyond codon 1444'
      supporting_text: FAP patients with mutations in codons 136-302 of the APC gene
        do not develop congenital hypertrophy of the retinal pigment epithelium (CHRPE),
        whereas those with mutations in codons 463-1387 regularly do.
      evidence_type: IEP
  - term:
      id: HP:0100031
      label: Neoplasm of the thyroid gland
    description: Increased risk of thyroid cancer
    support:
    - reference: PMID:26311738
      title: A novel pathogenic germline mutation in the adenomatous polyposis coli
        gene in a Chinese family with familial adenomatous coli
      supporting_text: Other signs that may point to FAP include the development of
        Gardner fibromas and desmoid tumors, pigmented lesions of the retina (CHRPE),
        jaw cysts, sebaceous cysts, and osteomata (benign bone tumors). Increased
        risk of thyroid cancer is also observed.
      evidence_type: IEP
- mutation:
    type: loss_of_function
    variant: somatic
  effects:
  - term:
      id: HP:0003003
      label: Colon cancer
    description: Found in ~80% of sporadic colorectal cancers
    support:
    - reference: PMID:1338904
      title: 'Somatic mutations of the APC gene in colorectal tumors: mutation cluster
        region in the APC gene'
      supporting_text: Somatic APC mutations are found in more than 80% of sporadic
        colorectal tumors and the tumor suppressor gene adenomatous polyposis coli
        (APC) is the initiating mutation in approximately 80% of all colorectal cancers
        (CRC).
      evidence_type: IEP
  - term:
      id: HP:0100242
      label: Sarcoma
    description: Desmoid tumors frequently have APC mutations
    support:
    - reference: PMID:8968744
      title: Familial infiltrative fibromatosis (desmoid tumours) (MIM135290) caused
        by a recurrent 3' APC gene mutation
      supporting_text: Desmoids arise following biallelic APC mutation, with one change
        usually occurring distal to the second β-catenin binding/degradation repeat
        of the gene (3' to codon 1399). APC gene mutations which truncate the APC
        protein distal to the beta-catenin binding domain are associated with desmoid
        tumours.
      evidence_type: TAS
  - term:
      id: HP:0100834
      label: Neoplasm of the large intestine
    description: Driver mutation in most colorectal adenomas
    support: []
- mutation:
    type: hypomorphic
    variant: germline
  effects:
  - term:
      id: HP:0005227
      label: Adenomatous colonic polyposis
    description: Attenuated FAP with 10-100 polyps
    support:
    - reference: PMID:9176082
      title: APC gene mutations and extraintestinal phenotype of familial adenomatous
        polyposis
      supporting_text: The attenuated form of FAP is characterized by multiple colonic
        polyps (average of 30), more proximally located polyps, and a diagnosis of
        CRC at a later age than in classic FAP. There is a 70% lifetime risk of CRC
        and the mean age of diagnosis is 50-55 years.
      evidence_type: IEP
  - term:
      id: HP:0040276
      label: Adenoma of large intestine
    description: Later onset than classic FAP
    support:
    - reference: PMID:9176082
      title: APC gene mutations and extraintestinal phenotype of familial adenomatous
        polyposis
      supporting_text: Patients with a mutation in APC 0-178 or 312-412 developed
        polyposis later and survived longer, whereas patients with mutations in APC
        1249-1549 developed polyposis earlier and did not survive as long. The attenuated
        form typically has later onset than classic FAP.
      evidence_type: IEP
---
# APC (Adenomatous Polyposis Coli)

## Overview
APC encodes a large multifunctional protein that serves as the central tumor suppressor in colorectal cancer and a key negative regulator of Wnt/β-catenin signaling. Originally identified through its role in familial adenomatous polyposis (FAP), APC functions as a scaffold protein in the β-catenin destruction complex and independently regulates cytoskeletal dynamics. Loss of APC function is the initiating event in the vast majority of colorectal cancers, highlighting its role as a "gatekeeper" of intestinal epithelial homeostasis.

## Structural Features
APC is a 2843 amino acid protein with multiple functional domains:
- **N-terminal region**: Oligomerization domain and armadillo repeats
- **Central region**: 
  - 15-amino acid repeats (7 copies) - bind β-catenin
  - 20-amino acid repeats (3 copies) - bind and downregulate β-catenin
  - SAMP repeats (3 copies) - bind Axin
- **C-terminal region**:
  - Basic domain - microtubule binding
  - EB1-binding domain - microtubule plus-end tracking
  - PDZ-binding motif - protein interactions

The multiple β-catenin binding sites create an efficient "β-catenin sink" that can sequester and process multiple β-catenin molecules simultaneously.

## Functional Mechanisms

### Wnt Signaling Regulation
1. **Destruction complex scaffold**: Brings together Axin, GSK3β, CK1, and β-catenin
2. **β-catenin processing**: 
   - Captures β-catenin through 15-aa repeats
   - Facilitates phosphorylation by GSK3β/CK1
   - Transfers phospho-β-catenin for ubiquitination
3. **Catalytic function**: Acts processively to degrade multiple β-catenin molecules
4. **Nuclear export**: Shuttles β-catenin out of nucleus

### Cytoskeletal Regulation
- **Microtubule stabilization**: Binds and protects plus-ends from depolymerization
- **Cell migration**: Polarizes microtubule networks
- **Chromosome segregation**: Ensures proper spindle attachment
- **Cell adhesion**: Links to actin cytoskeleton at adherens junctions

### Additional Functions
- **DNA damage response**: Participates in base excision repair
- **Cell cycle control**: Regulates mitotic spindle checkpoint
- **Apoptosis regulation**: Modulates cell survival pathways
- **RNA localization**: Involved in mRNA transport in neurons

## Clinical Significance

### Familial Adenomatous Polyposis (FAP)
Germline APC mutations cause:
- **Classic FAP**: >100 colorectal adenomas by age 20
- **Attenuated FAP**: 10-99 adenomas with later onset
- **Extracolonic manifestations**:
  - Desmoid tumors (15% of patients)
  - Duodenal adenomas and cancer
  - CHRPE (congenital hypertrophy of retinal pigment epithelium)
  - Osteomas and dental abnormalities
  - Thyroid cancer
  - Hepatoblastoma (in children)

### Sporadic Colorectal Cancer
- **Prevalence**: APC mutations in ~80% of colorectal cancers
- **Timing**: Usually the initiating event (gatekeeper mutation)
- **Two-hit mechanism**: Requires biallelic inactivation
- **Mutation spectrum**: 
  - Truncating mutations most common
  - Mutation cluster region (MCR) at codons 1250-1450
  - Specific mutations correlate with phenotype severity

### Genotype-Phenotype Correlations
- **Severe polyposis**: Mutations at codons 1250-1464
- **Attenuated FAP**: Mutations at 5' and 3' ends
- **Desmoid tumors**: Mutations beyond codon 1444
- **CHRPE**: Mutations between codons 463-1387

## Therapeutic Implications

### Current Approaches
- **COX-2 inhibitors**: Reduce polyp burden in FAP
- **Sulindac**: NSAID that reduces adenomas
- **Prophylactic colectomy**: Standard for FAP patients

### Emerging Therapies
- **Tankyrase inhibitors**: Stabilize Axin to compensate for APC loss
- **β-catenin antagonists**: Direct inhibition of TCF/β-catenin interaction
- **Synthetic lethality**: Targeting vulnerabilities in APC-mutant cells
- **Immunotherapy**: Neoantigen vaccines for truncated APC

## Evolutionary Perspective
APC is highly conserved across metazoans, with homologs in all bilateral animals. The protein's dual functions in Wnt signaling and cytoskeletal regulation appear ancient, suggesting these processes were linked early in evolution. The expansion of β-catenin binding repeats in vertebrate APC compared to invertebrate homologs may reflect increased need for stringent Wnt pathway control in complex tissues. The prevalence of APC mutations in human colorectal cancer highlights the evolutionary trade-off between rapid intestinal renewal and cancer susceptibility.

## Regulatory Mechanisms

### Expression Control
- **Transcriptional**: Regulated by CDX2 in intestine
- **Post-transcriptional**: Multiple splice variants
- **MicroRNA**: miR-135a/b target APC in colorectal cancer

### Post-translational Modifications
- **Phosphorylation**: Multiple sites regulate activity and localization
- **Ubiquitination**: Regulates stability and nuclear export
- **SUMOylation**: Affects nuclear functions
- **Caspase cleavage**: Generates pro-apoptotic fragments

### Subcellular Localization
- **Cytoplasmic**: Main pool in destruction complex
- **Cell periphery**: Enriched at cell protrusions
- **Nuclear**: Shuttles to regulate transcription
- **Mitochondrial**: Minor fraction with unclear function

## Key Interactions
- **Destruction complex**: Axin1/2, GSK3α/β, CK1α/ε, β-catenin
- **Cytoskeleton**: EB1, KIF3A, tubulin, actin
- **Adhesion**: E-cadherin, β-catenin, α-catenin
- **Nuclear**: β-catenin, CtBP, TCF/LEF
- **DNA repair**: DNA polymerase β, MUTYH
- **Additional**: PP2A, Asef, IQGAP1, plakoglobin