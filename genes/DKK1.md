---
id: UniProtKB:O94907
symbol: DKK1
primary_functions:
- description: Functions as a potent antagonist of canonical Wnt signaling by binding
    to LRP5/6 co-receptors and preventing formation of Wnt-Frizzled-LRP5/6 signaling
    complexes. This inhibitory function is critical for embryonic head formation,
    bone homeostasis, and regulation of various developmental processes.
  activity:
    term:
      id: GO:0030178
      label: negative regulation of Wnt signaling pathway
    support: []
    description: Inhibits Wnt signaling by preventing receptor complex formation
  location:
    term:
      id: GO:0005576
      label: extracellular region
    support: []
    description: Secreted protein that functions in extracellular space
  complex:
    term:
      id: GO:1904702
      label: negative regulation of Wnt-Frizzled-LRP5/6 complex assembly
    support: []
    description: Prevents Wnt receptor complex assembly and promotes LRP5/6 internalization
  upstream:
  - term:
      id: GO:0038024
      label: cargo receptor activity
    support: []
    description: Acts as a bridge between LRP5/6 and Kremen for internalization
    mechanism: Forms ternary complex with LRP5/6 and Kremen leading to clathrin-mediated
      endocytosis
  - term:
      id: GO:0042803
      label: protein homodimerization activity
    support: []
    description: Can dimerize to enhance antagonist activity
  downstream:
  - term:
      id: GO:0090090
      label: negative regulation of canonical Wnt signaling pathway
    support: []
    description: Blocks β-catenin stabilization and TCF/LEF transcriptional activation
  - term:
      id: GO:0031623
      label: receptor internalization
    support: []
    description: Promotes LRP5/6 endocytosis via Kremen-dependent mechanism
    mechanism: DKK1-LRP5/6-Kremen ternary complex undergoes clathrin-mediated endocytosis
  processes:
  - term:
      id: GO:0060323
      label: head morphogenesis
    support: []
  - term:
      id: GO:0030282
      label: bone mineralization
    support: []
  - term:
      id: GO:0045668
      label: negative regulation of osteoblast differentiation
    support: []
  roles:
  - term:
      id: GO:0030547
      label: signaling receptor inhibitor activity
    support: []
    description: Primary role as Wnt co-receptor antagonist
- description: Regulates bone homeostasis by controlling the balance between bone
    formation and resorption. Elevated DKK1 levels are associated with bone loss disorders,
    while inhibition promotes bone formation, making it a therapeutic target for osteoporosis.
  activity:
    term:
      id: GO:0045124
      label: regulation of bone resorption
    support: []
    description: Modulates bone resorption through osteoblast-osteoclast coupling
  location:
    term:
      id: CL:0000700
      label: dopaminergic neuron
    support: []
    description: Expression in hypothalamus regulates bone mass systemically
  processes:
  - term:
      id: GO:0045780
      label: positive regulation of bone resorption
    support: []
  - term:
      id: GO:0045671
      label: negative regulation of osteoclast differentiation
    support: []
  - term:
      id: GO:0001503
      label: ossification
    support: []
  roles:
  - term:
      id: GO:0070412
      label: R-SMAD binding
    support: []
    description: Cross-talk with BMP signaling pathways in bone
- description: Contributes to cancer progression by promoting tumor growth, invasion,
    and metastasis, particularly to bone. DKK1 is frequently overexpressed in various
    cancers and plays a critical role in cancer-associated bone disease, especially
    in multiple myeloma.
  activity:
    term:
      id: GO:0008283
      label: cell population proliferation
    support: []
    description: Promotes cancer cell growth and survival
  location:
    term:
      id: GO:0005615
      label: extracellular space
    support: []
    description: Secreted by tumor cells into microenvironment
  processes:
  - term:
      id: GO:0001525
      label: angiogenesis
    support: []
  - term:
      id: GO:0007162
      label: negative regulation of cell adhesion
    support: []
  - term:
      id: GO:0043065
      label: positive regulation of apoptotic process
    support: []
  roles:
  - term:
      id: GO:0005125
      label: cytokine activity
    support: []
    description: Acts as tumor-derived factor affecting stromal cells
- description: Modulates embryonic development beyond head formation, including limb
    development, organ morphogenesis, and stem cell fate determination. DKK1-mediated
    Wnt inhibition creates morphogenic gradients essential for proper patterning.
  activity:
    term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Can activate Wnt signaling at low concentrations (biphasic effect)
  processes:
  - term:
      id: GO:0060173
      label: limb development
    support: []
  - term:
      id: GO:0048762
      label: mesenchymal cell differentiation
    support: []
  - term:
      id: GO:0048568
      label: embryonic organ development
    support: []
phenotypes:
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0000238
      label: Hydrocephalus
    description: DKK1 knockout mice exhibit hydrocephalus due to defective head development
  - term:
      id: HP:0001363
      label: Craniosynostosis
    description: Premature fusion of skull sutures from disrupted Wnt signaling
  - term:
      id: HP:0000347
      label: Micrognathia
    description: Underdeveloped jaw structures from impaired craniofacial development
  - term:
      id: MONDO:0019508
      label: Dickkopf-related developmental anomaly
    description: Embryonic lethality with severe head and neural defects
- mutation:
    type: overexpression
    variant: somatic
  effects:
  - term:
      id: HP:0002797
      label: Osteolysis
    description: Bone destruction in multiple myeloma from DKK1 overexpression
  - term:
      id: HP:0002653
      label: Bone pain
    description: Pain from osteolytic lesions in cancer-associated bone disease
  - term:
      id: MONDO:0009693
      label: Multiple myeloma
    description: DKK1 overexpression drives osteolytic bone disease in myeloma
  - term:
      id: HP:0030731
      label: Carcinoma
    description: Elevated DKK1 in various epithelial cancers
- mutation:
    type: polymorphism
    variant: regulatory
  effects:
  - term:
      id: HP:0000939
      label: Osteoporosis
    description: DKK1 promoter variants associated with bone mineral density
  - term:
      id: HP:0002659
      label: Increased susceptibility to fractures
    description: SNPs affecting DKK1 expression linked to fracture risk
---
# DKK1 (Dickkopf WNT Signaling Pathway Inhibitor 1)

## Overview
DKK1 encodes a founding member of the Dickkopf family of secreted proteins that function as potent antagonists of canonical Wnt/β-catenin signaling. Originally identified for its essential role in embryonic head formation, DKK1 has emerged as a master regulator of bone homeostasis, a key player in cancer progression, and a promising therapeutic target for osteoporosis and cancer-associated bone disease. The protein's ability to bind and sequester LRP5/6 co-receptors makes it a crucial negative regulator of Wnt signaling in development and disease.

## Structural Features
DKK1 is a 266 amino acid secreted glycoprotein containing:
- An N-terminal signal peptide (residues 1-31) for secretion
- Two cysteine-rich domains (CRD):
  - CRD1 (N-terminal, residues 97-145): Contains 10 cysteines
  - CRD2 (C-terminal, residues 186-259): Contains 10 cysteines
- A central linker region connecting the two CRDs
- Two N-glycosylation sites at Asn199 and Asn227

The cysteine-rich domains form distinct functional modules:
- **CRD1**: Modulates Wnt signaling activity, may have context-dependent functions
- **CRD2**: Primary binding domain for LRP5/6 interaction (Kd ~0.3-0.5 nM)
- **Linker region**: Provides flexibility and contains regulatory elements

## Mechanism of Wnt Inhibition

### Direct LRP5/6 Antagonism
1. **High-affinity binding**: DKK1 CRD2 binds to the first two β-propeller domains of LRP5/6
2. **Competitive inhibition**: Prevents Wnt proteins from binding to LRP5/6
3. **Complex disruption**: Blocks formation of Wnt-Frizzled-LRP5/6 ternary complex
4. **Signal termination**: Prevents LRP5/6 phosphorylation and downstream signaling

### Kremen-Mediated Internalization
1. **Ternary complex formation**: DKK1 bridges LRP5/6 and Kremen1/2
2. **Receptor endocytosis**: Complex undergoes rapid clathrin-mediated internalization
3. **LRP5/6 depletion**: Reduces surface receptor availability
4. **Lysosomal degradation**: Internalized receptors are degraded

### Biphasic Activity
- **High concentrations (>10 ng/ml)**: Complete Wnt inhibition
- **Low concentrations (<1 ng/ml)**: Can paradoxically enhance Wnt signaling
- **Mechanism**: Low-level DKK1 may stabilize certain receptor conformations

## Biological Functions

### Embryonic Head Development
DKK1 is essential for anterior development:
- **Head induction**: Creates Wnt-free zone necessary for head formation
- **Neural patterning**: Establishes anterior-posterior neural axis
- **Eye development**: Required for proper eye field specification
- **Craniofacial morphogenesis**: Shapes facial structures
- **Brain regionalization**: Defines forebrain territories

Loss of DKK1 results in:
- Absence of head structures anterior to midbrain
- Cyclopia or anophthalmia
- Embryonic lethality

### Bone Homeostasis Regulation
DKK1 is a critical negative regulator of bone mass:

#### Effects on Osteoblasts
- **Differentiation inhibition**: Blocks MSC commitment to osteoblast lineage
- **Function suppression**: Reduces bone matrix production
- **Apoptosis induction**: Promotes osteoblast cell death
- **Proliferation inhibition**: Decreases osteoblast numbers

#### Effects on Osteoclasts
- **Indirect activation**: Increases RANKL/OPG ratio in osteoblasts
- **Enhanced resorption**: Promotes osteoclast differentiation
- **Coupling disruption**: Uncouples bone formation from resorption

#### Clinical Correlations
- **Postmenopausal osteoporosis**: Elevated DKK1 levels
- **Glucocorticoid-induced osteoporosis**: DKK1 upregulation
- **Age-related bone loss**: Increased DKK1 with aging
- **Disuse osteoporosis**: Mechanical unloading induces DKK1

### Role in Cancer Progression

#### Multiple Myeloma
DKK1 is central to myeloma bone disease:
- **Osteoblast suppression**: Blocks bone formation
- **Osteoclast activation**: Enhances bone resorption
- **Tumor support**: Creates permissive microenvironment
- **Biomarker**: Serum DKK1 correlates with bone lesions

#### Solid Tumors
DKK1 affects various cancers:
- **Prostate cancer**: Promotes bone metastasis
- **Breast cancer**: Enhances osteolytic lesions
- **Lung cancer**: Associated with poor prognosis
- **Hepatocellular carcinoma**: Promotes tumor growth
- **Gastric cancer**: Enhances invasion and metastasis

#### Mechanisms in Cancer
- **EMT promotion**: Reduces E-cadherin expression
- **Angiogenesis modulation**: Context-dependent vascular effects
- **Immune evasion**: Affects T-cell infiltration
- **Stem cell maintenance**: Preserves cancer stem cells
- **Metastatic niche**: Prepares bone microenvironment

### Metabolic Functions
Emerging roles in metabolism:
- **Glucose homeostasis**: Affects insulin sensitivity
- **Adipogenesis**: Regulates fat cell differentiation
- **Energy balance**: Influences metabolic rate
- **Inflammation**: Modulates inflammatory responses

## Clinical Significance

### Therapeutic Target in Osteoporosis
Anti-DKK1 strategies show promise:
- **Monoclonal antibodies**: 
  - BHQ880: Phase II trials in myeloma bone disease
  - PF-04840082: Preclinical studies show bone anabolic effects
  - DKN-01: Phase I/II trials in various cancers
- **Small molecule inhibitors**: In development
- **RNA interference**: Experimental approaches

### Biomarker Applications
- **Bone disease**: Serum DKK1 predicts fracture risk
- **Cancer prognosis**: Elevated levels indicate poor outcome
- **Treatment response**: Monitors anti-resorptive therapy
- **Disease activity**: Correlates with bone lesion burden

### Genetic Associations
- **Bone mineral density**: Multiple SNPs affect BMD
- **Osteoarthritis**: Variants linked to joint degeneration
- **Vitiligo**: Associated with autoimmune skin disorder
- **Alzheimer's disease**: Potential role in neurodegeneration

## Regulation

### Transcriptional Control
Multiple pathways regulate DKK1 expression:

#### Positive Regulators
- **p53**: Directly activates DKK1 in stress response
- **Glucocorticoids**: Induce via GR binding to promoter
- **TNF-α**: Activates through NF-κB pathway
- **BMP-2**: Stimulates in osteoblasts
- **Hypoxia**: HIF-1α upregulates DKK1

#### Negative Regulators
- **Wnt signaling**: TCF/LEF represses (negative feedback)
- **PTH**: Suppresses in osteoblasts
- **Mechanical loading**: Reduces expression in bone
- **Estrogen**: Inhibits via ERα

### Post-transcriptional Regulation
- **microRNAs**: miR-335-5p, miR-433 target DKK1
- **RNA stability**: AU-rich elements affect mRNA half-life
- **Alternative splicing**: Tissue-specific isoforms

### Post-translational Modifications
- **N-glycosylation**: Required for secretion and stability
- **Proteolytic processing**: Generates active fragments
- **Disulfide bonds**: Essential for protein folding

## Evolutionary Perspective
The Dickkopf family arose early in metazoan evolution:
- **Conservation**: DKK1 orthologs from cnidarians to humans
- **Functional conservation**: Head formation role preserved
- **Family expansion**: Four DKK genes in vertebrates (DKK1-4)
- **Divergent functions**: DKK3 lost Wnt inhibitory activity
- **Co-evolution**: With Wnt pathway components

The critical role of DKK1 in establishing body axis and skeletal development highlights its fundamental importance in metazoan body plan evolution.

## Key Interactions

### Receptor Binding
- **LRP5**: High-affinity binding (Kd ~0.3 nM)
- **LRP6**: Slightly higher affinity than LRP5
- **Kremen1**: Forms ternary complex with LRP5/6
- **Kremen2**: Alternative internalization co-receptor

### Protein-Protein Interactions
- **CKAP4**: Alternative receptor in cancer cells
- **SOST**: Potential synergistic inhibition
- **Wise/SOSTDC1**: Coordinate Wnt regulation

### Functional Antagonism With
- **Wnt1**: Blocks signaling through LRP5/6
- **Wnt3a**: Prevents canonical pathway activation
- **Wnt10b**: Inhibits osteoblast differentiation signals
- **R-spondin**: Opposes Wnt signal amplification

## Future Directions
Research priorities include:
- **Therapeutic antibodies**: Optimizing for bone anabolism
- **Cancer treatment**: Targeting DKK1 in metastatic disease
- **Biomarker development**: Standardizing clinical assays
- **Mechanistic studies**: Understanding context-dependent effects
- **Combination therapies**: With anti-resorptives or chemotherapy

The dual role of DKK1 in physiology and pathology makes it an attractive therapeutic target, with the potential to address major health challenges in osteoporosis, cancer, and beyond.