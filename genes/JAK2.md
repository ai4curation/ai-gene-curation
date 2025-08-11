---
id: UniProtKB:O60674
symbol: JAK2
primary_functions:
- description: JAK2 is a non-receptor tyrosine kinase that phosphorylates cytokine
    receptors and STAT proteins to transduce signals from hematopoietic cytokines
    and growth factors
  activity:
    term:
      id: GO:0004713
      label: protein tyrosine kinase activity
    support: []
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    notes: JAK2 associates with the cytoplasmic domain of cytokine receptors including
      EPO-R, TPO-R, GH-R, and IL-3R
  upstream:
  - term:
      id: GO:0004896
      label: cytokine receptor activity
    description: Activated by erythropoietin, thrombopoietin, growth hormone, prolactin,
      IL-3, IL-5, and GM-CSF binding to their receptors
  downstream:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Phosphorylates STAT proteins (STAT1, STAT3, STAT5A, STAT5B) and cytokine
      receptors at specific tyrosine residues
  processes:
  - term:
      id: GO:0007259
      name: cell surface receptor signaling pathway via JAK-STAT
    support: []
  - term:
      id: GO:0038163
      name: erythropoietin signaling pathway
    support: []
  - term:
      id: GO:0060333
      name: type II interferon-mediated signaling pathway
    support: []
- description: JAK2 regulates erythropoiesis and megakaryopoiesis through EPO and
    TPO receptor signaling
  activity:
    term:
      id: GO:0030218
      label: erythrocyte differentiation
    support: []
  processes:
  - term:
      id: GO:0038162
      name: erythropoietin-mediated signaling pathway
    support: []
  - term:
      id: GO:0030219
      name: megakaryocyte differentiation
    support: []
  roles:
  - term:
      id: GO:0045648
      label: positive regulation of erythrocyte differentiation
    notes: Essential for EPO-induced red blood cell production
  - term:
      id: GO:0045654
      label: positive regulation of megakaryocyte differentiation
    notes: Required for TPO-mediated platelet production
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: embryonic lethality due to absence of definitive erythropoiesis
    mechanism: complete failure of erythroid progenitor differentiation beyond the
      proerythroblast stage
    term:
      id: HP:0001903
      label: Anemia
    support: []
  - description: defective cytokine signaling affecting multiple hematopoietic lineages
    term:
      id: HP:0005528
      label: Bone marrow hypocellularity
    support: []
- mutation:
    type: gain_of_function
    variant: V617F
  effects:
  - description: myeloproliferative neoplasms including polycythemia vera
    mechanism: constitutive JAK2 activation leads to cytokine-independent STAT5 phosphorylation
      and erythroid proliferation
    term:
      id: MONDO:0009817
      label: polycythemia vera
    support: []
  - description: essential thrombocythemia with elevated platelet counts
    term:
      id: MONDO:0005170
      label: essential thrombocythemia
    support: []
  - description: primary myelofibrosis with bone marrow fibrosis
    term:
      id: MONDO:0009692
      label: primary myelofibrosis
    support: []
  - description: increased red blood cell mass
    term:
      id: HP:0001900
      label: Increased hemoglobin
    support: []
  - description: thrombosis risk due to hyperviscosity
    term:
      id: HP:0001907
      label: Thromboembolism
    support: []
---
**JAK2 (Janus Kinase 2)** is a non-receptor tyrosine kinase that serves as the primary signal transducer for **erythropoietin (EPO)**, **thrombopoietin (TPO)**, and **growth hormone (GH)** receptors, making it essential for hematopoiesis.

## Function

* **Hematopoietic cytokine signaling:** Central kinase for homodimeric cytokine receptors including:
  * **EPO receptor** → erythrocyte production
  * **TPO receptor (MPL)** → megakaryocyte/platelet production
  * **Growth hormone receptor** → growth and metabolism
  * **Prolactin receptor** → lactation and reproduction
  * **IL-3/IL-5/GM-CSF receptors** → myeloid cell development

* **Activation mechanism:** JAK2 exists as a preformed dimer bound to receptor cytoplasmic domains. Cytokine binding induces receptor dimerization, bringing JAK2 molecules into proximity for trans-phosphorylation of activation loop tyrosines (Y1007/Y1008), fully activating kinase activity.

* **Substrate phosphorylation:** Activated JAK2 phosphorylates:
  * **Cytokine receptors** creating SH2 domain docking sites for STATs and adaptors
  * **STAT5A/STAT5B** (primary substrates for EPO/TPO/GH signaling)
  * **STAT3** (IL-6 family cytokines when partnered with JAK1)
  * **STAT1** (IFN-γ signaling when partnered with JAK1)
  * **Signal adaptors** including SHC, GAB1, IRS proteins

* **Erythropoiesis regulation:** JAK2 is absolutely required for:
  * EPO-induced survival signals in erythroid progenitors
  * STAT5-mediated transcription of anti-apoptotic genes (BCL-XL)
  * GATA-1 activation for erythroid differentiation program

* **Metabolic functions:** Through GH receptor signaling:
  * Regulates IGF-1 production in liver
  * Controls lipid metabolism and adipocyte function
  * Influences glucose homeostasis via hepatic gluconeogenesis

* **Regulation:** JAK2 activity is controlled by:
  * **SOCS proteins** (SOCS1, SOCS3) - cytokine-induced negative feedback
  * **LNK/SH2B3** - negative regulator in hematopoietic cells
  * **Protein phosphatases** (SHP-1, SHP-2, CD45, PTP1B)
  * **PIAS proteins** - inhibit STAT transcriptional activity

## Clinical Significance

* **JAK2 V617F mutation** (~95% of polycythemia vera, ~60% of essential thrombocythemia and primary myelofibrosis):
  * Located in pseudokinase domain, disrupts autoinhibition
  * Results in constitutive kinase activation
  * Cytokine-independent growth of hematopoietic progenitors
  * Hypersensitivity to cytokine stimulation

* **Other JAK2 mutations:**
  * **Exon 12 mutations** in V617F-negative polycythemia vera
  * **Germline mutations** causing hereditary thrombocytosis

## Phenotypes

* **Loss-of-function:** Embryonic lethal (E12.5) due to complete absence of definitive erythropoiesis

* **Gain-of-function (V617F):** Philadelphia chromosome-negative myeloproliferative neoplasms with:
  * Elevated hematocrit and hemoglobin (polycythemia vera)
  * Thrombocytosis (essential thrombocythemia)
  * Bone marrow fibrosis (primary myelofibrosis)
  * Increased thrombotic risk
  * Potential transformation to acute myeloid leukemia