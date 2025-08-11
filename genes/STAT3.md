---
id: UniProtKB:P40763
symbol: STAT3
primary_functions:
- description: STAT3 mediates acute phase response in hepatocytes by inducing production
    of acute phase proteins
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
  cell_type:
    term:
      id: CL:0000182
      label: hepatocyte
    notes: Cell-type-specific function in liver hepatocytes
  gross_anatomy:
    term:
      id: UBERON:0002107
      label: liver
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    description: Induces CRP, SAA, fibrinogen, and other acute phase proteins
  processes:
  - term:
      id: GO:0006953
      name: acute-phase response
    support: []
- description: STAT3 promotes Th17 cell differentiation and IL-17 production in CD4+
    T cells
  activity:
    term:
      id: GO:0003700
      label: DNA-binding transcription factor activity
  location:
    term:
      id: GO:0005634
      label: nucleus
    support: []
  cell_type:
    term:
      id: CL:0000899
      label: T-helper 17 cell
    notes: Essential for Th17 lineage commitment with RORγt
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    description: Activates IL17A, IL17F, IL21, and IL22 gene expression
  processes:
  - term:
      id: GO:2000318
      name: positive regulation of T-helper 17 type immune response
- description: STAT3 promotes cell survival and proliferation through anti-apoptotic
    signaling (generic function)
  activity:
    term:
      id: GO:0003700
      label: DNA-binding transcription factor activity
  location:
    term:
      id: GO:0005634
      label: nucleus
    notes: STAT3 shuttles between cytoplasm and nucleus; constitutively nuclear in
      cancer cells
  upstream:
  - term:
      id: GO:0042976
      label: activation of Janus kinase activity
    description: JAK1, JAK2, and TYK2 phosphorylate STAT3 at Tyr705 following cytokine
      receptor engagement
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    description: STAT3 activates transcription of anti-apoptotic genes (BCL2, BCL2L1,
      MCL1), proliferation genes (CCND1, MYC), and inflammatory mediators (IL6, IL10)
  processes:
  - term:
      id: GO:0007259
      name: cell surface receptor signaling pathway via JAK-STAT
  - term:
      id: GO:0070102
      name: interleukin-6-mediated signaling pathway
  - term:
      id: GO:0071222
      name: cellular response to lipopolysaccharide
  - term:
      id: GO:0006915
      name: apoptotic process
    notes: STAT3 negatively regulates apoptosis through BCL2 family activation
  - term:
      id: GO:0006953
      name: acute-phase response
    support: []
    notes: Essential for IL-6-induced expression of acute phase proteins including
      CRP and SAA
  roles:
  - term:
      id: GO:0042803
      label: protein homodimerization activity
    support: []
    notes: Forms homodimers after phosphorylation at Tyr705
  - term:
      id: GO:0019901
      label: protein kinase binding
    support:
    - reference: GO_REF:0000024
      title: Manual transfer of experimentally-verified manual GO annotation data
        to orthologs by curator judgment of sequence similarity
      evidence_type: ISS
    notes: Interacts with JAK1, JAK2, TYK2, and EGFR
phenotypes:
- mutation:
    type: loss_of_function
    variant: dominant_negative
  effects:
  - description: Hyper-IgE syndrome (Job syndrome) with elevated serum IgE (>2000
      IU/ml), eczema, and recurrent infections
    mechanism: dominant-negative mutations in DNA-binding or SH2 domains impair STAT3
      function leading to defective Th17 responses
    term:
      id: HP:0003212
      label: Increased circulating IgE concentration
    support: []
  - description: autosomal dominant hyper-IgE syndrome due to STAT3 deficiency
    mechanism: decreased STAT3 activity causes defective Th17 differentiation and
      impaired antimicrobial peptide production
    term:
      id: MONDO:0007818
      label: hyper-IgE recurrent infection syndrome 1, autosomal dominant
    support: []
  - description: recurrent staphylococcal skin abscesses and pneumonia with pneumatocele
      formation
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
  - description: retained primary dentition and characteristic facial features
    term:
      id: HP:0006297
      label: Enamel hypoplasia
  - description: skeletal abnormalities including scoliosis and pathological fractures
    term:
      id: HP:0002650
      label: Scoliosis
  - description: mucocutaneous candidiasis
    term:
      id: HP:0002728
      label: Chronic mucocutaneous candidiasis
- mutation:
    type: gain_of_function
    variant: somatic
  effects:
  - description: large granular lymphocytic leukemia with clonal T-cell or NK-cell
      expansion
    mechanism: activating mutations in SH2 domain (Y640F, D661V/Y, N647I) enhance
      STAT3 dimerization and transcriptional activity
    term:
      id: HP:0004808
      label: Acute myeloid leukemia
    support: []
  - description: neutropenia and autoimmune manifestations including rheumatoid arthritis
    term:
      id: HP:0001875
      label: Decreased total neutrophil count
    support: []
  - description: constitutive STAT3 activation in various cancers
    notes: STAT3 acts as oncogene when constitutively active, promoting tumor cell
      survival and proliferation
- mutation:
    type: gain_of_function
    variant: germline
  effects:
  - description: early-onset multi-organ autoimmunity with lymphoproliferation
    mechanism: germline GOF mutations cause excessive STAT3 signaling leading to regulatory
      T-cell dysfunction
    term:
      id: HP:0002960
      label: Autoimmunity
  - description: autoimmune cytopenias and lymphadenopathy
    term:
      id: HP:0002716
      label: Lymphadenopathy
  - description: growth delay and short stature
    term:
      id: HP:0004322
      label: Short stature
---
**STAT3 (Signal Transducer and Activator of Transcription 3)** is a transcription factor that serves as a critical mediator of cytokine signaling, particularly for the **IL-6 family**, promoting cell survival, proliferation, and anti-inflammatory responses in contrast to the pro-apoptotic functions of STAT1.

## Function

* **Pro-survival signaling mediator:** Activated by IL-6, IL-10, IL-11, IL-21, IL-23, IL-27, IL-31, OSM, LIF, CNTF, CT-1, and leptin through JAK-mediated phosphorylation. In contrast to STAT1's pro-apoptotic role, STAT3 primarily promotes cell survival and proliferation.

* **Activation mechanism:** Upon cytokine binding to receptors (particularly gp130-containing receptors), JAK1, JAK2, or TYK2 phosphorylate STAT3 at Tyr705, leading to homodimerization via reciprocal SH2-phosphotyrosine interactions and nuclear translocation. Additional phosphorylation at Ser727 enhances transcriptional activity.

* **Transcriptional targets:** In the nucleus, STAT3 binds to GAS elements (TTN5-6AA) to regulate genes involved in:
  * **Anti-apoptotic pathways** (BCL2, BCL2L1/BCL-XL, MCL1, BIRC5/survivin)
  * **Cell proliferation** (CCND1/cyclin D1, MYC, JUN)
  * **Angiogenesis** (VEGF)
  * **Immune regulation** (IL10, IL23R, FOXP3)
  * **Acute phase response** (CRP, SAA, fibrinogen, haptoglobin)
  * **Negative feedback** (SOCS3)

* **Acute phase response:** Essential for IL-6-induced hepatic production of acute phase proteins including C-reactive protein (CRP) and serum amyloid A (SAA), which can increase 1000-fold during inflammation.

* **Th17 differentiation:** Critical for differentiation of naive CD4+ T cells into Th17 cells through induction of RORγt, while suppressing Th1 differentiation. This contrasts with STAT1's role in promoting Th1 responses.

* **Metabolic functions:** Mediates leptin signaling for energy homeostasis, insulin secretion in pancreatic β-cells, and regulation of gluconeogenesis in hepatocytes.

* **Non-canonical functions:** Cytoplasmic STAT3 can regulate autophagy, mitochondrial function, and microtubule dynamics independent of its transcriptional activity.

* **Regulation:** Activity controlled by:
  * **SOCS3** - primary negative feedback inhibitor (not SOCS1 which targets STAT1)
  * **PIAS3** - inhibits DNA binding
  * **Protein phosphatases** (SHP-1, SHP-2, PTPRT, TC-PTP)
  * **Acetylation** by p300/CBP enhances activity
  * **Ubiquitination** targets for proteasomal degradation

## Phenotypes

* **Loss-of-function (dominant-negative) mutations** → Hyper-IgE syndrome (Job syndrome):
  * Serum IgE >2000 IU/ml (often >5000 IU/ml)
  * Recurrent staphylococcal abscesses ("cold" abscesses)
  * Pneumonia with pneumatocele formation
  * Chronic mucocutaneous candidiasis
  * Retained primary teeth
  * Characteristic facial features
  * Skeletal abnormalities (scoliosis, pathological fractures)
  * Vascular complications (aneurysms, thrombosis)

* **Somatic gain-of-function mutations** → Large granular lymphocytic leukemia:
  * Found in 40-70% of T-LGL and 30% of NK-LGL cases
  * Hot spot mutations: Y640F, D661V, D661Y, N647I in SH2 domain
  * Associated with neutropenia and rheumatoid arthritis
  * Enhanced response to JAK inhibitor therapy

* **Germline gain-of-function mutations** → Early-onset autoimmune disease:
  * Multi-organ autoimmunity
  * Autoimmune cytopenias
  * Lymphoproliferation
  * Growth delay

* **Oncogenic role:** Constitutively active in many cancers:
  * Promotes tumor cell survival via BCL2 family proteins
  * Induces angiogenesis through VEGF
  * Suppresses anti-tumor immunity
  * Creates immunosuppressive tumor microenvironment through IL-10 induction