---
id: UniProtKB:Q9UP38
symbol: FZD1
primary_functions:
- description: Functions as a seven-transmembrane receptor for Wnt proteins, initiating
    canonical Wnt/β-catenin signaling upon ligand binding. Forms part of the receptor
    complex with LRP5/6 co-receptors essential for signal transduction.
  activity:
    term:
      id: GO:0017147
      label: Wnt-protein binding
    support: []
    description: Binds multiple Wnt ligands including WNT3A, WNT1, and WNT8 through
      cysteine-rich domain
  location:
    term:
      id: GO:0005886
      label: plasma membrane
    support: []
    description: Localizes to plasma membrane as seven-transmembrane spanning receptor
  complex:
    term:
      id: GO:1990851
      label: Wnt-Frizzled-LRP5/6 complex
    support: []
    description: Forms ternary complex with Wnt ligands and LRP5/6 co-receptors
  upstream:
  - term:
      id: GO:0005102
      label: signaling receptor binding
    support: []
    description: Activated by binding of Wnt ligands to extracellular cysteine-rich
      domain
    mechanism: Wnt binding induces receptor clustering and LRP5/6 recruitment
  downstream:
  - term:
      id: GO:0060071
      label: Wnt signaling pathway, planar cell polarity pathway
    support: []
    description: Can activate both canonical and non-canonical pathways
  - term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Activates β-catenin stabilization through Dishevelled recruitment
  processes:
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0007166
      label: cell surface receptor signaling pathway
    support: []
  - term:
      id: GO:0016055
      label: Wnt signaling pathway
    support: []
  roles:
  - term:
      id: GO:0004888
      label: transmembrane signaling receptor activity
    support: []
    description: Primary Wnt receptor for canonical signaling
- description: Mediates Dishevelled recruitment and activation at the plasma membrane,
    initiating downstream signaling cascades. This scaffolding function is essential
    for both canonical and non-canonical Wnt signaling.
  activity:
    term:
      id: GO:0019901
      label: protein kinase binding
    support: []
    description: Binds Dishevelled proteins through conserved KTxxxW motif in C-terminal
      tail
  location:
    term:
      id: GO:0043234
      label: protein-containing complex
    support: []
    description: Forms signaling complexes at membrane microdomains
  upstream:
  - term:
      id: GO:0051434
      label: BH3 domain binding
    support: []
    description: PDZ domain of Dishevelled binds to FZD1 C-terminus
  downstream:
  - term:
      id: GO:1904886
      label: beta-catenin destruction complex disassembly
    support: []
    description: Dishevelled recruitment leads to Axin sequestration
  processes:
  - term:
      id: GO:0090090
      label: negative regulation of canonical Wnt signaling pathway
    support: []
    description: Receptor internalization provides negative feedback
  roles:
  - term:
      id: GO:0005109
      label: frizzled binding
    support: []
    description: Scaffold for signaling complex assembly
- description: Mediates G protein-coupled receptor signaling through heterotrimeric
    G protein activation. FZD1 can couple to multiple G protein subtypes including
    Gαi/o, Gαq/11, and Gαs to diversify signaling outputs.
  activity:
    term:
      id: GO:0004930
      label: G protein-coupled receptor activity
    support: []
    description: Activates G protein signaling independent of β-catenin pathway
  location:
    term:
      id: GO:0043235
      label: receptor complex
    support: []
    description: Can form receptor oligomers that modulate signaling specificity
  downstream:
  - term:
      id: GO:0007186
      label: G protein-coupled receptor signaling pathway
    support: []
    description: Activates phospholipase C and protein kinase C pathways
  - term:
      id: GO:0051928
      label: positive regulation of calcium ion transport
    support: []
    description: Triggers calcium release from intracellular stores
  processes:
  - term:
      id: GO:0035567
      label: non-canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0060071
      label: Wnt signaling pathway, planar cell polarity pathway
    support: []
  roles:
  - term:
      id: GO:0004930
      label: G protein-coupled receptor activity
    support: []
    description: Functions as an atypical GPCR for Wnt ligands
- description: Regulates planar cell polarity through non-canonical Wnt signaling
    pathways. Activates small GTPases and JNK signaling to control cell polarity and
    directed cell movements.
  activity:
    term:
      id: GO:0090176
      label: microtubule cytoskeleton organization involved in establishment of planar
        polarity
    support: []
    description: Controls cytoskeletal organization for planar polarity
  upstream:
  - term:
      id: GO:0042813
      label: Wnt receptor signaling pathway involved in cell fate specification
    support: []
    description: Activated by non-canonical Wnt ligands
    mechanism: WNT5A/11 binding induces asymmetric receptor localization
  downstream:
  - term:
      id: GO:0032956
      label: regulation of actin cytoskeleton organization
    support: []
    description: Controls actin dynamics through small GTPases
  - term:
      id: GO:0043507
      label: positive regulation of JUN kinase activity
    support: []
    description: Activates JNK cascade for transcriptional responses
  processes:
  - term:
      id: GO:0001736
      label: establishment of planar polarity
    support: []
  - term:
      id: GO:0090179
      label: planar cell polarity pathway involved in neural tube closure
    support: []
  roles:
  - term:
      id: GO:0090176
      label: microtubule cytoskeleton organization involved in establishment of planar
        polarity
    support: []
    description: Key regulator of tissue planar polarity
phenotypes:
- mutation:
    type: overexpression
    variant: somatic
  effects:
  - term:
      id: HP:0003003
      label: Colon cancer
    description: FZD1 overexpression found in 40% of colorectal cancers with activated
      Wnt signaling
    mechanism: Ligand-dependent activation of β-catenin promotes tumor cell proliferation
    support: []
  - term:
      id: HP:0100013
      label: Neoplasm of the breast
    description: Upregulated in triple-negative breast cancer promoting EMT and metastasis
    mechanism: FZD1-mediated Wnt signaling induces epithelial-mesenchymal transition
    support:
    - reference: PMID:22484497
      title: Interference of Frizzled 1 (FZD1) reverses multidrug resistance in breast
        cancer cells through the Wnt/β-catenin pathway
      supporting_text: FZD1 protein is overexpressed in the multidrug resistant breast
        cancer cell subline MCF-7/ADM, coincident with MDR1/P-gp. FZD1 silencing induced
        down-regulation of MDR1/P-gp, restored sensitivity to chemotherapy drugs
      evidence_type: IMP
  - term:
      id: HP:0002861
      label: Melanoma
    description: High FZD1 expression in 60% of melanomas associated with progression
    mechanism: Autocrine Wnt signaling through FZD1 maintains melanoma stem cells
    support: []
  - term:
      id: MONDO:0005575
      label: Colorectal cancer
    description: FZD1 amplification or overexpression drives tumor progression
    mechanism: Enhances Wnt signaling in APC-mutant tumors
    support: []
  - term:
      id: MONDO:0007254
      label: Breast cancer
    description: FZD1 upregulation correlates with poor prognosis and metastasis
    mechanism: Promotes cancer stem cell properties and therapy resistance
    support:
    - reference: PMID:22484497
      title: Interference of Frizzled 1 (FZD1) reverses multidrug resistance in breast
        cancer cells through the Wnt/β-catenin pathway
      supporting_text: FZD1 expression is up-regulated in breast cancer and FZD1 silencing
        significantly decreased β-catenin levels, suggesting FZD1 mediates multidrug
        resistance through the Wnt/β-catenin pathway
      evidence_type: IMP
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0001627
      label: Abnormal heart morphology
    description: FZD1 knockout mice show cardiac outflow tract defects and ventricular
      septal defects
    mechanism: Impaired cardiac neural crest cell migration and differentiation
    support: []
  - term:
      id: HP:0000924
      label: Abnormality of the skeletal system
    description: Reduced bone mass and impaired fracture healing in FZD1-deficient
      mice
    mechanism: Decreased osteoblast differentiation and bone formation
    support:
    - reference: PMID:20051274
      title: Functional and association analysis of frizzled 1 (FZD1) promoter haplotypes
        with femoral neck geometry
      supporting_text: Two common and potentially functional genetic variants (rs2232157,
        rs2232158) in the frizzled-1 (FZD1) promoter region and their haplotypes'
        influence on FZD1 promoter activity in human osteoblast-like cells
      evidence_type: IEP
  - term:
      id: HP:0002011
      label: Morphological central nervous system abnormality
    description: Hippocampal defects and impaired neurogenesis
    mechanism: Reduced neural progenitor proliferation and survival
    support: []
  - term:
      id: MONDO:0019391
      label: Tetra-amelia syndrome
    description: Complete limb absence when combined with other Wnt pathway mutations
    mechanism: Failed limb bud initiation due to absent Wnt signaling
    support: []
- mutation:
    type: regulatory_variant
    variant: germline
  effects:
  - term:
      id: HP:0000939
      label: Osteoporosis
    description: FZD1 promoter variants associated with low bone mineral density
    mechanism: Reduced FZD1 expression impairs osteoblast function
    support:
    - reference: PMID:20051274
      title: Functional and association analysis of frizzled 1 (FZD1) promoter haplotypes
        with femoral neck geometry
      supporting_text: In comparison to the common GG haplotype, promoter activity
        was 3-fold higher for the TC haplotype in both cell lines and FZD1 mRNA and
        protein expression was demonstrated in human osteoblast-like cell lines
      evidence_type: IEP
  - term:
      id: MONDO:0005148
      label: Type 2 diabetes mellitus
    description: Intronic variants linked to insulin resistance
    mechanism: Altered adipocyte differentiation and glucose homeostasis
    support:
    - reference: PMID:19543507
      title: Non-association between polymorphisms of the frizzled receptor genes
        and bone mineral density in postmenopausal Korean women
      supporting_text: SNPs in the FZD1, FZD5, FZD6, FZD7, and FZD9 genes were analyzed
        by direct sequencing in 371 postmenopausal Korean women to study potential
        metabolic associations
      evidence_type: IEP
- mutation:
    type: knockout
    variant: experimental
  effects:
  - term:
      id: HP:0001511
      label: Intrauterine growth retardation
    description: FZD1/FZD2 double knockout causes severe growth restriction
    mechanism: Impaired placental development and nutrient transport
    support: []
  - term:
      id: HP:0000238
      label: Hydrocephalus
    description: Ventricular enlargement in conditional neural knockout
    mechanism: Defective ependymal cell cilia orientation
    support: []
---
# FZD1 (Frizzled Class Receptor 1)

## Overview
FZD1 encodes a member of the Frizzled family of seven-transmembrane receptors that serve as the primary receptors for Wnt proteins. As a core component of the Wnt signaling machinery, FZD1 plays crucial roles in development, tissue homeostasis, and disease. The receptor can activate both canonical (β-catenin-dependent) and non-canonical (β-catenin-independent) Wnt signaling pathways depending on the cellular context and ligand specificity. FZD1 is unique among Frizzled receptors in its broad ligand binding profile and ability to activate multiple downstream signaling cascades simultaneously.

## Structural Features
FZD1 is a 647 amino acid protein containing:
- An N-terminal signal sequence (residues 1-21) for membrane targeting
- A cysteine-rich domain (CRD, residues 22-163) that binds Wnt ligands
- A linker region (residues 164-247) connecting CRD to transmembrane domain
- Seven transmembrane helices (residues 248-525) characteristic of GPCRs
- Three extracellular loops (ECL1-3) contributing to ligand specificity
- Three intracellular loops (ICL1-3) mediating G protein coupling
- A C-terminal cytoplasmic tail containing PDZ-binding motif (KTxxxW) for Dishevelled interaction

The CRD contains 10 conserved cysteines forming 5 disulfide bonds that create a hydrophobic groove accommodating the palmitoleic acid modification of Wnt proteins. This lipid-binding pocket is essential for high-affinity ligand recognition (Kd ~10-100 nM for WNT3A). The seven-transmembrane architecture allows for both G protein-dependent and independent signaling mechanisms, with distinct conformational changes triggering different downstream pathways.

## Signaling Mechanisms

### Canonical Wnt/β-Catenin Signaling
1. **Ligand recognition**: Wnt proteins (WNT3A, WNT1, WNT8) bind to the CRD of FZD1 with nanomolar affinity
2. **Co-receptor recruitment**: Forms ternary complex with LRP5/6 co-receptors through Wnt bridging
3. **Receptor clustering**: Induces FZD1-LRP5/6 heterodimerization and signalosome formation
4. **Dishevelled activation**: Recruits DVL proteins via C-terminal KTxxxW motif binding to DVL PDZ domain
5. **Destruction complex inhibition**: DVL polymers sequester Axin, disrupting the β-catenin destruction complex
6. **β-catenin stabilization**: Prevents GSK3β-mediated phosphorylation and proteasomal degradation
7. **Nuclear translocation**: Accumulated β-catenin enters nucleus
8. **Transcriptional activation**: β-catenin displaces Groucho from TCF/LEF, activating target genes (c-Myc, Cyclin D1, Axin2)

### Non-canonical Planar Cell Polarity (PCP) Pathway
- **Ligand specificity**: Activated by WNT5A, WNT11 binding
- **Dishevelled recruitment**: DVL localizes asymmetrically without β-catenin activation
- **Small GTPase activation**: Stimulates RhoA through DAAM1, Rac1 through DVL
- **JNK cascade**: Activates c-Jun N-terminal kinase via RAC1-MKK4/7
- **Cytoskeletal reorganization**: Controls actin polymerization and microtubule orientation
- **Cellular outputs**: Directs convergent extension, neural tube closure, hair follicle orientation

### G Protein-Coupled Signaling
- **Gαq/11 pathway**: Activates phospholipase C-β → IP3/DAG → Ca2+ release and PKC activation
- **Gαi/o pathway**: Inhibits adenylyl cyclase → decreased cAMP → modulates PKA activity
- **Gαs pathway**: Stimulates adenylyl cyclase → increased cAMP (context-dependent)
- **β-arrestin recruitment**: Mediates receptor desensitization and endocytosis

## Biological Functions

### Embryonic Development
- **Gastrulation**: Controls cell movements during primitive streak formation and mesoderm specification
- **Neural development**: 
  - Specifies dorsal neural tube fate through high Wnt signaling
  - Promotes neural crest induction at the neural plate border
  - Regulates neuronal differentiation and axon guidance
- **Cardiac morphogenesis**: 
  - Required for second heart field development
  - Controls cardiac neural crest migration
  - Essential for outflow tract septation
- **Limb development**: 
  - Maintains apical ectodermal ridge signaling
  - Establishes dorsal-ventral limb polarity
  - Regulates digit number and identity
- **Somitogenesis**: Controls segmentation clock and somite boundary formation

### Adult Tissue Homeostasis
- **Intestinal stem cells**: Maintains Lgr5+ crypt base columnar cells
- **Hair follicle cycling**: Activates bulge stem cells for anagen initiation
- **Hematopoietic stem cells**: Balances self-renewal versus differentiation
- **Neural stem cells**: Supports adult neurogenesis in hippocampus and subventricular zone
- **Bone homeostasis**: Promotes osteoblast differentiation and bone formation
- **Wound healing**: Activated in keratinocytes and fibroblasts during repair

### Physiological Regulation
- **Glucose metabolism**: Enhances insulin sensitivity in adipocytes
- **Lipid homeostasis**: Regulates adipocyte differentiation and lipogenesis
- **Immune function**: 
  - Controls T cell differentiation (Th1/Th2 balance)
  - Regulates dendritic cell maturation
  - Modulates inflammatory responses
- **Vascular biology**: Maintains blood-brain barrier integrity

## Ligand Specificity and Binding

### Wnt Ligand Affinities
- **High affinity (Kd 10-50 nM)**: 
  - WNT3A: Primary canonical pathway activator
  - WNT1: Strong β-catenin signaling inducer
  - WNT8: Potent in developmental contexts
- **Moderate affinity (Kd 50-200 nM)**: 
  - WNT2: Tissue-specific functions
  - WNT9B: Kidney and bone development
  - WNT7A: Synaptic development
- **Context-dependent binding**: 
  - WNT5A: Activates PCP pathway preferentially but can trigger canonical signaling with appropriate co-receptors
  - WNT11: Primarily non-canonical, convergent extension movements
  - WNT4: Switches between pathways based on receptor context

### Factors Determining Ligand Selectivity
- **Co-receptor expression**: 
  - LRP5/6 presence favors canonical signaling
  - ROR1/2 or RYK promote non-canonical pathways
  - Glypicans modulate ligand presentation
- **Receptor oligomerization**: 
  - FZD1 homodimers show different ligand preferences than heterodimers
  - Clustering affects signaling amplitude and duration
- **Extracellular modulators**:
  - Heparan sulfate proteoglycans concentrate Wnt ligands
  - sFRP proteins compete for Wnt binding
  - R-spondins enhance signaling through ZNRF3/RNF43 inhibition
- **Post-translational modifications**:
  - N-glycosylation affects ligand binding affinity
  - Phosphorylation modulates receptor trafficking

## Clinical Significance

### Cancer Association

#### Colorectal Cancer
- **Prevalence**: FZD1 overexpressed in 40-50% of CRC cases
- **Mechanism**: Enhances Wnt signaling even in APC-mutant tumors
- **Prognosis**: High expression correlates with advanced stage and poor survival
- **Therapeutic relevance**: FZD1 inhibition reduces tumor growth in xenografts

#### Breast Cancer
- **Subtype specificity**: Particularly elevated in triple-negative breast cancer (TNBC)
- **Functions**: Promotes epithelial-mesenchymal transition and metastasis
- **Stem cells**: Maintains breast cancer stem cell population
- **Resistance**: Contributes to chemotherapy and radiation resistance

#### Melanoma
- **Expression**: Upregulated in 60% of metastatic melanomas
- **BRAF interaction**: Cooperates with BRAF mutations to drive progression
- **Immune evasion**: FZD1 signaling suppresses anti-tumor immunity

#### Other Malignancies
- **Glioblastoma**: Maintains glioma stem cells
- **Hepatocellular carcinoma**: Promotes tumor initiation and progression
- **Acute myeloid leukemia**: Required for leukemia stem cell function
- **Pancreatic cancer**: Enhances desmoplastic reaction and therapy resistance

### Therapeutic Targeting

#### Antibody-Based Therapies
- **Vantictumab (OMP-18R5)**: 
  - Targets FZD1/2/5/7/8
  - Phase Ib trials in solid tumors
  - Bone toxicity limits dosing
- **OTSA101**: 
  - FZD10-specific antibody
  - Radiolabeled for synovial sarcoma
- **Bispecific antibodies**: 
  - FZD-CD3 bispecifics in development
  - Enhanced tumor cell killing

#### Small Molecule Inhibitors
- **CRD-binding compounds**: 
  - Carbamazepine derivatives
  - Natural products (e.g., niclosamide)
- **Transmembrane domain inhibitors**: 
  - PORCN inhibitors (upstream target)
  - LGK974, ETC-159 in clinical trials
- **Allosteric modulators**: 
  - Target conformational changes
  - Improved specificity

#### Novel Approaches
- **Peptide antagonists**: 
  - Soluble CRD domains
  - Wnt-mimetic peptides
- **RNA-based therapies**: 
  - siRNA/shRNA delivery systems
  - Antisense oligonucleotides
- **CAR-T cells**: 
  - FZD1-targeted CAR-T in development
- **Combination strategies**: 
  - With checkpoint inhibitors
  - With conventional chemotherapy

## Regulation

### Transcriptional Control
- **Developmental regulation**:
  - SOX family transcription factors induce during neural development
  - TCF/LEF creates positive feedback loop in Wnt-active cells
  - HOX genes control segment-specific expression
- **Pathological regulation**:
  - c-Myc amplification drives overexpression in cancer
  - NF-κB activation in inflammation
  - HIF-1α induction under hypoxia
- **Epigenetic mechanisms**:
  - Promoter hypomethylation in colorectal cancer
  - Histone acetylation by CBP/p300
  - Chromatin remodeling by SWI/SNF complexes

### Post-transcriptional Regulation
- **MicroRNA targeting**:
  - miR-21: Downregulates FZD1 in normal cells, often lost in cancer
  - miR-27a/b: Targets 3'UTR, reduced in tumors
  - miR-204: Suppresses FZD1 in epithelial cells
- **RNA-binding proteins**:
  - HuR stabilizes mRNA in cancer cells
  - AUF1 promotes decay in differentiated cells
- **Alternative splicing**:
  - Exon skipping generates dominant-negative isoforms
  - Tissue-specific splice variants

### Protein-level Regulation
- **Quality control**:
  - ER chaperones (BiP, calnexin) ensure proper folding
  - ERAD pathway degrades misfolded receptors
- **Trafficking**:
  - Wntless required for initial surface delivery
  - AP-2 mediates clathrin-coated pit localization
  - Retromer complex involved in recycling
- **Post-translational modifications**:
  - N-glycosylation at 3 sites affects stability
  - Phosphorylation by CK1/2 modulates activity
  - Palmitoylation enhances membrane association
- **Turnover**:
  - ZNRF3/RNF43 ubiquitinate for degradation
  - USP6/USP8 deubiquitinases counteract
  - Half-life ~4-6 hours at cell surface
- **Endocytosis and recycling**:
  - Clathrin-mediated endocytosis predominant
  - Caveolin-mediated uptake in lipid rafts
  - ~60% recycled to surface, 40% degraded

## Tissue Expression and Function

### High Expression Tissues
- **Brain**: Cortex, hippocampus, cerebellum - neuronal development and synaptic plasticity
- **Heart**: Myocardium, valves - cardiac development and adult homeostasis
- **Intestine**: Crypt base - stem cell maintenance and epithelial renewal
- **Bone**: Osteoblasts, osteocytes - bone formation and remodeling
- **Skin**: Hair follicles, interfollicular epidermis - stem cell regulation

### Moderate Expression
- **Lung**: Alveolar epithelium - repair and regeneration
- **Kidney**: Tubular epithelium - nephron development and function
- **Liver**: Hepatocytes, stellate cells - regeneration and fibrosis
- **Muscle**: Satellite cells - muscle regeneration
- **Immune system**: T cells, dendritic cells - immune regulation

### Cell Type-Specific Functions
- **Stem cells**: Self-renewal and multipotency maintenance
- **Progenitor cells**: Proliferation and lineage commitment
- **Epithelial cells**: Polarity establishment and barrier function
- **Neurons**: Axon guidance and synapse formation
- **Endothelial cells**: Angiogenesis and barrier integrity

## Evolutionary Perspective

### Ancient Origins
- **Sponges**: Proto-Frizzled receptors present in Amphimedon queenslandica
- **Cnidarians**: Functional Wnt signaling in Hydra and Nematostella
- **Emergence**: Frizzled-Wnt system predates bilateral symmetry by >600 million years

### Vertebrate Evolution
- **Gene duplication**: Whole-genome duplications created 10 mammalian FZD genes
- **Functional divergence**: FZD1 retained broad ligand specificity
- **Conservation**: 
  - CRD domain: 85-90% identity across mammals
  - Transmembrane regions: 80-85% conservation
  - C-terminal motif: KTxxxW perfectly conserved

### Species-Specific Features
- **Human**: 647 amino acids, chromosome 7q21.13
- **Mouse**: 647 amino acids, 97% identity to human
- **Zebrafish**: Two orthologs (fzd1a, fzd1b) from teleost duplication
- **Drosophila**: Single Frizzled performs FZD1-like functions

### Evolutionary Advantages
- **Signaling versatility**: Ability to activate multiple pathways
- **Tissue adaptability**: Broad expression allows diverse functions
- **Regulatory complexity**: Multiple control mechanisms enable fine-tuning
- **Disease resistance**: Redundancy with other FZDs provides robustness

## Key Molecular Interactions

### Direct Protein Interactions
- **Wnt ligands**: 
  - WNT3A (Kd ~20 nM): Primary canonical activator
  - WNT1 (Kd ~30 nM): Development and stem cells
  - WNT8 (Kd ~25 nM): Embryonic patterning
  - WNT5A (Kd ~100 nM): Context-dependent signaling
- **Co-receptors**:
  - LRP5/6: Essential for canonical signaling
  - ROR1/2: Non-canonical pathway activation
  - RYK: Convergent extension movements
  - Glypican-3/4: Ligand presentation
- **Intracellular partners**:
  - Dishevelled (DVL1/2/3): PDZ domain interaction
  - Gαi/o, Gαq/11, Gαs: G protein coupling
  - β-arrestin 1/2: Desensitization and trafficking
  - AP-2: Endocytic adaptor

### Regulatory Interactions
- **Negative regulators**:
  - ZNRF3/RNF43: E3 ubiquitin ligases
  - DKK1: Blocks LRP5/6 (indirect)
  - sFRP1-5: Competitive Wnt binding
  - WIF1: Wnt sequestration
  - SOST/Sclerostin: LRP5/6 antagonist
- **Positive modulators**:
  - R-spondin 1-4: Enhance through LGR4/5/6
  - Norrin: Wnt mimetic for FZD4
  - USP6/8: Deubiquitinases
  - VPS35: Retromer-mediated recycling

### Functional Complexes
- **Wnt-Frizzled-LRP5/6 complex**: FZD1-LRP5/6-Wnt-DVL
- **Destruction complex**: Interaction via DVL
- **PCP complex**: FZD1-DVL-DAAM1-RhoA
- **G protein complex**: FZD1-Gα-Gβγ
- **Endocytic complex**: FZD1-AP2-clathrin

## Future Directions

### Research Priorities
- Structure-based drug design targeting specific conformations
- Development of FZD1-selective modulators
- Understanding tissue-specific signaling contexts
- Biomarker development for therapy selection
- Combination therapy optimization

### Therapeutic Opportunities
- Cancer stem cell targeting
- Regenerative medicine applications
- Bone anabolic therapies
- Neurodegeneration treatment
- Immunomodulation strategies

### Technical Advances Needed
- Real-time signaling biosensors
- Single-cell signaling analysis
- Tissue-specific delivery systems
- Reversible FZD1 modulators
- Patient stratification methods