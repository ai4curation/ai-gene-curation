---
id: UniProtKB:P51692
symbol: STAT5B
primary_functions:
- description: STAT5B is a transcription factor that transduces signals from growth
    hormone and IL-2 family cytokines to regulate postnatal growth, metabolism, and
    immune cell development
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
    notes: STAT5B translocates to nucleus upon JAK2-mediated phosphorylation
  upstream:
  - term:
      id: GO:0060396
      label: growth hormone receptor signaling pathway
    description: Activated by JAK2 phosphorylation at Y699 following GH pulses
  - term:
      id: GO:0038110
      label: interleukin-2-mediated signaling pathway
    description: JAK1/JAK3-mediated activation downstream of IL-2R
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: STAT5B activates IGF-1, CYP genes, and immune regulatory genes
  processes:
  - term:
      id: GO:0040018
      name: positive regulation of multicellular organism growth
    support: []
  - term:
      id: GO:0060736
      name: prostate gland growth
    support: []
- description: STAT5B mediates IL-2 family cytokine signals essential for regulatory
    T cell development and NK cell maturation
  activity:
    term:
      id: GO:0045591
      label: positive regulation of regulatory T cell differentiation
    support: []
  processes:
  - term:
      id: GO:0030889
      name: negative regulation of B cell proliferation
    support: []
  - term:
      id: GO:0001779
      name: natural killer cell differentiation
    support: []
  roles:
  - term:
      id: GO:0032733
      label: positive regulation of interleukin-10 production
    notes: STAT5B promotes IL-10 production by regulatory T cells
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: growth hormone insensitivity with severe short stature
    mechanism: failure to induce IGF-1 and other GH target genes
    term:
      id: MONDO:0019280
      label: growth hormone insensitivity syndrome
    support: []
  - description: immunodeficiency with recurrent infections
    mechanism: impaired T cell and NK cell development and function
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
  - description: immune dysregulation with autoimmune manifestations
    mechanism: reduced regulatory T cell numbers and function
    term:
      id: HP:0002960
      label: Autoimmunity
    support: []
  - description: severe postnatal growth retardation
    term:
      id: HP:0008897
      label: Postnatal growth retardation
    support: []
  - description: delayed puberty
    mechanism: disrupted GH-IGF-1 axis affecting sexual maturation
    term:
      id: HP:0000823
      label: Delayed puberty
    support: []
  - description: prolactin insensitivity (related phenotype)
    term:
      id: HP:0008202
      label: Prolactin deficiency
    support: []
- mutation:
    type: gain_of_function
    variant: N642H
  effects:
  - description: aggressive T cell and NK cell neoplasms
    mechanism: constitutive STAT5B activation drives lymphoid transformation
    term:
      id: MONDO:0020518
      label: T-cell large granular lymphocyte leukemia
    support: []
  - description: hepatosplenic T cell lymphoma
    term:
      id: MONDO:0019472
      label: hepatosplenic T-cell lymphoma
    support: []
---
**STAT5B (Signal Transducer and Activator of Transcription 5B)** is a transcription factor critical for **growth hormone signaling**, **postnatal growth**, and **immune regulation**, particularly **regulatory T cell** and **NK cell** development.

## Function

* **Growth hormone signaling:** STAT5B is the primary mediator of GH responses:
  * **Pulsatile GH response:** Sexually dimorphic gene expression
  * **IGF-1 production:** Major regulator of hepatic IGF-1 synthesis
  * **Metabolic regulation:** Controls ~30% of sexually dimorphic liver genes
  * **Male-pattern gene expression:** CYP enzymes, MUPs, other sex-specific genes

* **IL-2 family signaling:** STAT5B mediates immune functions:
  * **IL-2:** Regulatory T cell development and maintenance
  * **IL-15:** NK cell maturation and memory CD8+ T cells
  * **IL-7:** T and B cell development and homeostasis
  * **IL-9:** Mast cell and T cell proliferation

* **Target gene programs:**
  * **Growth-related:** IGF-1, ALS, IGFBP-3
  * **Metabolic:** CYP2D9, CYP3A, lipogenic enzymes
  * **Immune:** FOXP3, IL-2Rα, BCL-2, IL-10
  * **Cell survival:** BCL-XL, MCL-1, PIM-1, SOCS genes

* **Regulatory T cell development:** STAT5B is essential for:
  * FOXP3 induction and maintenance
  * IL-2Rα (CD25) expression
  * Treg survival and suppressive function
  * Peripheral tolerance maintenance

* **NK cell functions:** STAT5B controls:
  * Terminal NK cell maturation
  * Cytotoxic granule proteins
  * Cytokine production capacity
  * NK cell memory formation

* **Sexually dimorphic functions:**
  * Males require STAT5B for normal growth patterns
  * Regulates male-specific liver gene expression
  * Controls sex differences in drug metabolism
  * Influences fat distribution and metabolism

* **Protein characteristics:**
  * 96% identical to STAT5A but functionally distinct
  * Y699 phosphorylation site (vs Y694 in STAT5A)
  * Preferential response to GH pulses vs continuous GH
  * Different chromatin binding kinetics than STAT5A

* **Temporal dynamics:**
  * Rapid activation by GH pulses (minutes)
  * Quick dephosphorylation between pulses
  * Circadian regulation of activity
  * Age-dependent expression changes

* **Regulation:**
  * **SOCS2** - primary negative regulator for GH signaling
  * **CIS** - inhibits IL-2 family signaling
  * **Nuclear phosphatases** (TC45, DUSP)
  * **Proteasomal degradation** via ubiquitination

## Clinical Significance

* **STAT5B deficiency syndrome:**
  * Autosomal recessive growth hormone insensitivity
  * Severe proportionate short stature (-5 to -7 SD)
  * Normal/elevated GH, low IGF-1
  * Immune dysfunction with infections
  * Some patients develop autoimmunity
  * ~20 cases reported worldwide

* **Immunological features:**
  * T cell lymphopenia
  * Reduced regulatory T cells
  * Impaired NK cell function
  * Recurrent respiratory infections
  * Opportunistic infections (PCP, CMV)
  * Autoimmune diseases (thyroiditis, ITP)

* **STAT5B and cancer:**
  * N642H mutation in T-LGL leukemia
  * Activated in T-ALL and NK cell lymphomas
  * BCR-ABL activates STAT5B in CML
  * JAK3 mutations activate STAT5B in T-ALL

## Phenotypes

* **Human STAT5B deficiency:**
  * **Growth:** Severe short stature, delayed bone age
  * **Metabolic:** Increased adiposity, insulin resistance
  * **Immune:** Combined immunodeficiency features
  * **Endocrine:** Delayed puberty, prolactin insensitivity
  * **Pulmonary:** Interstitial lung disease (some cases)

* **Mouse STAT5B knockout:**
  * Sexual dimorphism loss in liver gene expression
  * Male growth retardation (females less affected)
  * Loss of male-pattern GH response
  * Reduced NK cells and γδ T cells
  * Normal lactation (unlike STAT5A KO)

* **Constitutive activation:**
  * T cell neoplasms (T-LGL, T-ALL)
  * NK cell lymphomas
  * Cytokine-independent growth
  * Resistance to apoptosis