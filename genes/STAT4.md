---
id: UniProtKB:Q14765
symbol: STAT4
primary_functions:
- description: STAT4 is a transcription factor that transduces IL-12 and IL-23 signals
    to promote Th1 differentiation and cell-mediated immunity
  activity:
    term:
      id: GO:0003700
      label: DNA-binding transcription factor activity
    support: []
  location:
    term:
      id: GO:0005634
      label: nucleus
    support: []
    notes: STAT4 translocates from cytoplasm to nucleus upon IL-12-induced phosphorylation
  upstream:
  - term:
      id: GO:0035722
      label: interleukin-12-mediated signaling pathway
    description: Activated by JAK2 and TYK2 phosphorylation at Y693 following IL-12
      receptor engagement
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: STAT4 activates transcription of IFN-γ, T-bet, and IL-12Rβ2 genes
  processes:
  - term:
      id: GO:0042088
      name: T-helper 1 type immune response
    support: []
  - term:
      id: GO:0032729
      name: positive regulation of type II interferon production
    support: []
- description: STAT4 mediates IL-23 signaling in Th17 cells and promotes inflammatory
    responses
  activity:
    term:
      id: GO:0070757
      label: interleukin-23-mediated signaling pathway
    support: []
  processes:
  - term:
      id: GO:0072539
      name: T-helper 17 cell differentiation
    support: []
  - term:
      id: GO:0032740
      name: positive regulation of interleukin-17 production
    support: []
  roles:
  - term:
      id: GO:0030101
      label: natural killer cell activation
    notes: STAT4 mediates IL-12-induced NK cell IFN-γ production and cytotoxicity
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: impaired Th1 responses with reduced IFN-γ production
    mechanism: failure to respond to IL-12 prevents Th1 differentiation
    term:
      id: HP:0005419
      label: Decreased T cell activation
    support: []
  - description: enhanced Th2 responses with elevated IgE
    mechanism: absence of Th1 signals allows unopposed Th2 differentiation
    term:
      id: HP:0003212
      label: Increased circulating IgE concentration
    support: []
  - description: increased susceptibility to intracellular pathogens
    term:
      id: HP:0002719
      label: Recurrent infections
    support:
    - reference: PMID:8700209
      title: Impaired IL-12 responses and enhanced development of Th2 cells in Stat4-deficient
        mice
      supporting_text: STAT4-deficient mice have increased susceptibility to infection
        with intracellular organisms such as Listeria monocytogenes
      evidence_type: IMP
  - description: protection from autoimmune diseases (reduced risk)
    mechanism: reduced inflammatory T cell responses
    term:
      id: HP:0002960
      label: Autoimmunity
    support: []
- mutation:
    type: polymorphisms
    variant: rs7574865
  effects:
  - description: increased risk of autoimmune diseases
    mechanism: enhanced STAT4 expression or activity increases inflammatory responses
    term:
      id: MONDO:0007179
      label: autoimmune disease
  - description: rheumatoid arthritis susceptibility
    term:
      id: MONDO:0008383
      label: rheumatoid arthritis
  - description: systemic lupus erythematosus susceptibility
    term:
      id: MONDO:0007915
      label: systemic lupus erythematosus
  - description: primary Sjögren syndrome susceptibility
    term:
      id: MONDO:0010413
      label: Sjögren syndrome
---
**STAT4 (Signal Transducer and Activator of Transcription 4)** is a transcription factor that mediates **IL-12** and **IL-23** signaling to promote **Th1 differentiation** and **cell-mediated immunity** against intracellular pathogens.

## Function

* **IL-12 signal transduction:** Primary mediator of IL-12 responses:
  * IL-12 binding → JAK2/TYK2 activation → STAT4 phosphorylation at Y693
  * STAT4 homodimer formation and nuclear translocation
  * Binding to GAS elements in target gene promoters
  * Essential for Th1 lineage commitment

* **Target gene activation:** STAT4 induces transcription of:
  * **IFN-γ** - signature Th1 cytokine
  * **T-bet (TBX21)** - master Th1 transcription factor
  * **IL-12Rβ2** - positive feedback loop for IL-12 responsiveness
  * **IL-18Rα** - synergizes with IL-12 for IFN-γ production
  * **FASL** - cytotoxic effector molecule
  * **CCR5** - chemokine receptor for Th1 trafficking

* **IL-23 signaling:** Cooperative role with STAT3:
  * IL-23R engagement → STAT4 and STAT3 phosphorylation
  * STAT4-STAT3 heterodimers in certain contexts
  * Promotes IL-17A and IL-17F expression in Th17 cells
  * Maintains pathogenic Th17 phenotype

* **NK cell functions:** STAT4 in NK cells mediates:
  * IL-12-induced IFN-γ production
  * Enhanced cytotoxicity against target cells
  * Memory-like NK cell generation
  * Antiviral and antitumor responses

* **CD8+ T cell responses:** STAT4 promotes:
  * CTL differentiation and effector functions
  * Memory CD8+ T cell formation
  * Type 1 immunity against viruses and tumors

* **Expression pattern:**
  * Restricted to immune cells
  * High in T cells, NK cells, and dendritic cells
  * Low/absent in B cells and non-hematopoietic tissues
  * Expression increases with T cell activation

* **Protein interactions:**
  * Forms homodimers after phosphorylation
  * Can heterodimerize with STAT3 in specific contexts
  * Interacts with p300/CBP coactivators
  * Binds N-CoR corepressor in resting state

* **Regulation:**
  * **SOCS3** - cytokine-induced negative feedback
  * **PIAS proteins** - inhibit DNA binding
  * **Protein phosphatases** (TC45, SHP-2)
  * **Proteasomal degradation** after dephosphorylation

## Clinical Significance

* **STAT4 polymorphisms and autoimmunity:**
  * rs7574865 (T allele) - strongest genetic risk factor after HLA
  * Associated with multiple autoimmune diseases:
    - Rheumatoid arthritis (OR ~1.3)
    - Systemic lupus erythematosus (OR ~1.5)
    - Sjögren syndrome
    - Type 1 diabetes
    - Primary biliary cholangitis
  * Mechanism: Enhanced STAT4 expression → excessive Th1/Th17 responses

* **Protective variants:**
  * Loss-of-function variants protect against autoimmunity
  * Trade-off: Increased infection susceptibility

* **Therapeutic implications:**
  * STAT4 inhibition proposed for autoimmune diseases
  * Challenge: Preserving antimicrobial immunity
  * JAK inhibitors indirectly reduce STAT4 activation

## Phenotypes

* **STAT4 deficiency (mouse models):**
  * Severely impaired Th1 responses
  * Defective IFN-γ production by T and NK cells
  * Enhanced Th2 differentiation
  * Susceptibility to Leishmania, Toxoplasma, and Listeria
  * Resistance to EAE and collagen-induced arthritis

* **Human STAT4 variants:**
  * **Risk alleles:** Increased autoimmune disease susceptibility
  * **Protective alleles:** Reduced inflammatory responses
  * No complete human deficiency reported (likely embryonic lethal or extremely rare)

* **Cellular phenotypes:**
  * Impaired Th1 differentiation
  * Reduced NK cell cytotoxicity
  * Altered Th17 cell plasticity
  * Defective memory T cell formation