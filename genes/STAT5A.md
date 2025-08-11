---
id: UniProtKB:P42229
symbol: STAT5A
primary_functions:
- description: STAT5A is a transcription factor that transduces signals from growth
    hormone, prolactin, and cytokines to regulate mammary gland development, metabolism,
    and hematopoiesis
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
    notes: STAT5A shuttles between cytoplasm and nucleus, with nuclear accumulation
      upon activation
  upstream:
  - term:
      id: GO:0060396
      label: growth hormone receptor signaling pathway
    description: Activated by JAK2 phosphorylation at Y694 following GH receptor engagement
  - term:
      id: GO:0038161
      label: prolactin signaling pathway
    description: JAK2-mediated phosphorylation downstream of prolactin receptor
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: STAT5A activates genes for milk proteins, IGF-1, and anti-apoptotic
      factors
  processes:
  - term:
      id: GO:0060749
      name: mammary gland alveolus development
    support: []
  - term:
      id: GO:0007595
      name: lactation
    support: []
- description: STAT5A mediates cytokine signals essential for hematopoietic cell survival
    and proliferation
  activity:
    term:
      id: GO:0038110
      label: interleukin-2-mediated signaling pathway
    support: []
  processes:
  - term:
      id: GO:0030218
      name: erythrocyte differentiation
    support: []
  - term:
      id: GO:0050731
      name: positive regulation of peptidyl-tyrosine phosphorylation
    support: []
  roles:
  - term:
      id: GO:0043066
      label: negative regulation of apoptotic process
    notes: STAT5A induces BCL-XL and BCL-2 expression for cell survival
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: female infertility due to corpus luteum dysfunction
    mechanism: impaired prolactin signaling disrupts progesterone production
    term:
      id: HP:0000144
      label: Decreased fertility
    support: []
  - description: lactation failure (related phenotype)
    mechanism: defective mammary alveolar development and milk protein gene expression
    term:
      id: HP:0100783
      label: Breast aplasia
    support: []
  - description: growth retardation
    mechanism: reduced IGF-1 production in response to growth hormone
    term:
      id: HP:0001510
      label: Growth delay
    support: []
  - description: mild anemia
    mechanism: partially redundant with STAT5B in erythropoiesis
    term:
      id: HP:0001903
      label: Anemia
    support: []
- mutation:
    type: gain_of_function
  effects:
  - description: myeloproliferative disorders
    mechanism: constitutive STAT5A activation drives hematopoietic cell proliferation
    term:
      id: MONDO:0020076
      label: myeloproliferative neoplasm
    support: []
  - description: acute lymphoblastic leukemia
    term:
      id: MONDO:0004967
      label: acute lymphoblastic leukemia
    support: []
  - description: chronic myeloid leukemia progression
    mechanism: BCR-ABL activates STAT5A contributing to CML pathogenesis
    term:
      id: MONDO:0011996
      label: chronic myeloid leukemia
    support: []
---
**STAT5A (Signal Transducer and Activator of Transcription 5A)** is a transcription factor essential for **mammary gland development**, **lactation**, and **hematopoietic cell survival**, primarily activated by **prolactin**, **growth hormone**, and **cytokines**.

## Function

* **Prolactin signaling:** STAT5A is the primary mediator of prolactin responses:
  * **Mammary development:** Alveolar differentiation during pregnancy
  * **Lactogenesis:** Activation of milk protein genes (β-casein, WAP, α-lactalbumin)
  * **Corpus luteum function:** Progesterone production maintenance
  * Female-specific reproductive functions

* **Growth hormone signaling:** STAT5A mediates metabolic effects:
  * **IGF-1 production:** Hepatic synthesis of IGF-1 and ALS
  * **Lipid metabolism:** Regulation of fatty acid synthesis
  * **Body growth:** Postnatal growth via GH-IGF-1 axis
  * **Sexual dimorphism:** Sex-specific gene expression patterns

* **Cytokine signaling:** STAT5A responds to multiple cytokines:
  * **IL-2/IL-15:** T cell proliferation and survival
  * **IL-3/GM-CSF:** Myeloid cell development
  * **IL-7:** B and T cell development
  * **EPO:** Erythroid progenitor survival (with STAT5B)
  * **TPO:** Megakaryocyte development

* **Target gene specificity:** STAT5A activates:
  * **Survival genes:** BCL-XL, BCL-2, MCL-1, PIM-1
  * **Cell cycle genes:** Cyclin D1, D2, D3, c-MYC
  * **Metabolic genes:** PEPCK, G6Pase, FAS
  * **Milk proteins:** β-casein, WAP, α-lactalbumin
  * **Negative regulators:** SOCS2, SOCS3, CIS

* **Protein structure and activation:**
  * Phosphorylation at Y694 by JAKs
  * Forms homodimers or heterodimers with STAT5B
  * Contains N-terminal, coiled-coil, DNA-binding, SH2, and transactivation domains
  * C-terminal truncated isoforms act as dominant-negatives

* **STAT5A vs STAT5B distinctions:**
  * 96% amino acid identity but distinct functions
  * STAT5A: Female reproduction, mammary development
  * STAT5B: Male-specific growth, immune regulation
  * Different DNA binding preferences and target genes
  * Tissue-specific expression patterns

* **Chromatin interactions:**
  * Binds GAS motifs (TTCN₃GAA)
  * Forms enhanceosomes with glucocorticoid receptor
  * Recruits p300/CBP and NCoA coactivators
  * Can act as pioneer factor opening chromatin

* **Regulation:**
  * **SOCS proteins** (CIS, SOCS1, SOCS2, SOCS3)
  * **Protein phosphatases** (SHP-1, SHP-2, PTP1B)
  * **PIAS3** - inhibits DNA binding
  * **Nuclear export** and proteasomal degradation

## Clinical Significance

* **STAT5A and cancer:**
  * Frequently activated in hematologic malignancies
  * BCR-ABL → STAT5A activation in CML
  * JAK2 V617F → STAT5A activation in MPNs
  * FLT3-ITD → STAT5A activation in AML
  * Promotes survival and proliferation of cancer cells

* **Breast cancer:**
  * Loss of STAT5A associated with poor prognosis
  * Maintains mammary epithelial differentiation
  * Paradoxical tumor suppressor role in breast tissue

* **Growth disorders:**
  * Contributes to GH insensitivity syndromes
  * Sexual dimorphism in growth patterns

## Phenotypes

* **STAT5A deficiency (mouse):**
  * **Females:** Lactation failure, corpus luteum defects, infertility
  * **Males:** Mild phenotype, normal fertility
  * Partial growth retardation
  * Mild anemia (compensated by STAT5B)
  * Normal immune system development

* **STAT5A/STAT5B double knockout:**
  * Perinatal lethality in most mice
  * Severe anemia
  * Absent T regulatory cells
  * Female infertility
  * Dwarfism

* **Constitutive activation:**
  * Myeloid and lymphoid leukemias
  * Increased cell survival and proliferation
  * Resistance to apoptosis
  * Cytokine independence