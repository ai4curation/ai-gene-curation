---
id: UniProtKB:P52333
symbol: JAK3
primary_functions:
- description: JAK3 is a non-receptor tyrosine kinase specifically expressed in hematopoietic
    cells that transduces signals from cytokines using the common gamma chain receptor
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
    notes: JAK3 exclusively associates with the common gamma chain (γc) of IL-2 family
      receptors
  upstream:
  - term:
      id: GO:0004896
      label: cytokine receptor activity
    description: Activated by IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21 binding to
      receptors containing the common gamma chain
  downstream:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Phosphorylates STAT proteins (STAT3, STAT5A, STAT5B, STAT6) enabling
      lymphocyte development and function
  processes:
  - term:
      id: GO:0007259
      name: cell surface receptor signaling pathway via JAK-STAT
    support: []
  - term:
      id: GO:0038110
      name: interleukin-2-mediated signaling pathway
    support: []
  - term:
      id: GO:0038111
      name: interleukin-7-mediated signaling pathway
    support: []
- description: JAK3 is essential for lymphocyte development and function through common
    gamma chain cytokine signaling
  activity:
    term:
      id: GO:0030217
      label: T cell differentiation
    support: []
  processes:
  - term:
      id: GO:0030098
      name: lymphocyte differentiation
    support: []
  - term:
      id: GO:0042102
      name: positive regulation of T cell proliferation
    support: []
  - term:
      id: GO:0001779
      name: natural killer cell differentiation
    support: []
  roles:
  - term:
      id: GO:0030183
      label: B cell differentiation
    notes: Required for IL-4 and IL-21 signaling in B cell maturation and class switching
  - term:
      id: GO:0045579
      label: positive regulation of B cell differentiation
    notes: Essential for IL-4-mediated B cell responses
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: T-B+NK- severe combined immunodeficiency with absent T cells and
      NK cells but preserved B cells
    mechanism: defective signaling through common gamma chain cytokines blocks T and
      NK cell development
    term:
      id: MONDO:0010316
      label: severe combined immunodeficiency due to JAK3 deficiency
    support: []
  - description: profound T cell lymphopenia
    term:
      id: HP:0005403
      label: Decreased total T cell count
    support: []
  - description: absence of natural killer cells
    term:
      id: HP:0040218
      label: Reduced total natural killer cell count
    support: []
  - description: hypogammaglobulinemia despite presence of B cells
    mechanism: lack of T cell help prevents B cell maturation and antibody production
    term:
      id: HP:0004313
      label: Decreased circulating immunoglobulin concentration
    support: []
  - description: severe opportunistic infections from infancy
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
  - description: failure to thrive and growth retardation
    mechanism: chronic infections and malabsorption due to immunodeficiency
    term:
      id: HP:0001508
      label: Failure to thrive
    support: []
- mutation:
    type: gain_of_function
  effects:
  - description: T cell lymphoproliferative disorders
    mechanism: constitutive JAK3 activation drives uncontrolled T cell proliferation
    term:
      id: HP:0005523
      label: Lymphoproliferative disorder
    support: []
  - description: T cell acute lymphoblastic leukemia
    term:
      id: MONDO:0004963
      label: T-cell acute lymphoblastic leukemia
    support: []
  - description: NK/T cell lymphomas
    term:
      id: MONDO:0020084
      label: NK-T cell lymphoma
    support: []
---
**JAK3 (Janus Kinase 3)** is a non-receptor tyrosine kinase with **restricted expression in hematopoietic cells** that exclusively partners with the **common gamma chain (γc/CD132)** to transduce signals from IL-2 family cytokines.

## Function

* **Common gamma chain signaling:** JAK3 is the dedicated kinase for γc-containing receptors:
  * **IL-2 receptor** → T cell proliferation and Treg development
  * **IL-4 receptor** → Th2 differentiation and B cell class switching
  * **IL-7 receptor** → T cell development and homeostasis
  * **IL-9 receptor** → Mast cell and T cell growth
  * **IL-15 receptor** → NK cell development and CD8+ T cell memory
  * **IL-21 receptor** → B cell maturation and NK cell activation

* **Activation mechanism:** JAK3 constitutively associates with the γc cytoplasmic domain. Upon cytokine binding, JAK3 pairs with JAK1 (bound to the cytokine-specific receptor chain), leading to trans-phosphorylation and activation of both kinases.

* **Substrate specificity:** Activated JAK3-JAK1 complexes phosphorylate:
  * **STAT5A/STAT5B** (IL-2, IL-7, IL-15 signaling)
  * **STAT3** (IL-21 signaling)
  * **STAT6** (IL-4 signaling)
  * **Receptor chains** creating docking sites for SH2-containing proteins

* **Lymphocyte development:** JAK3 is absolutely required for:
  * **T cell development** in thymus (β-selection and positive selection)
  * **NK cell differentiation** from bone marrow progenitors
  * **Peripheral T cell homeostasis** via IL-7 signaling
  * **T cell activation and proliferation** via IL-2 signaling

* **B cell functions:** While B cells develop in JAK3 absence, JAK3 is essential for:
  * IL-4-induced class switch recombination
  * IL-21-mediated plasma cell differentiation
  * Germinal center formation

* **Tissue specificity:** JAK3 expression is restricted to:
  * T cells (all subsets)
  * B cells
  * NK cells
  * Myeloid cells (lower levels)
  * Intestinal epithelial cells (γc-mediated signals)

* **Regulation:** JAK3 activity is controlled by:
  * **SOCS1 and SOCS3** - cytokine-induced negative feedback
  * **CIS** - competes with STATs for receptor binding
  * **SHP-1** - dephosphorylates JAK3 and associated proteins
  * **PIAS proteins** - inhibit STAT-mediated transcription

## Clinical Significance

* **JAK3 deficiency:** Autosomal recessive SCID (T-B+NK-):
  * Clinically identical to X-linked SCID (γc deficiency)
  * ~7-14% of all SCID cases
  * Newborn screening detects low TREC levels
  * Treatable by hematopoietic stem cell transplantation
  * Gene therapy trials showing promise

* **JAK3 as therapeutic target:**
  * Tofacitinib (JAK3/JAK1 inhibitor) - rheumatoid arthritis
  * Ruxolitinib (JAK1/JAK2 > JAK3) - myelofibrosis
  * JAK3-selective inhibitors in development for transplant rejection

## Phenotypes

### JAK3 Deficiency (Loss-of-function)
Classic **T-B+NK- SCID** (7-14% of all SCID cases):
* **T cell defect**: Complete absence due to blocked IL-7 signaling in thymus
* **NK cell defect**: Absent due to defective IL-15 signaling
* **B cell phenotype**: Normal numbers but functionally defective
  - Hypogammaglobulinemia despite adequate B cell counts
  - Poor antibody responses due to lack of T cell help
  - Defective class switching (impaired IL-4/IL-21 responses)
* **Clinical presentation**:
  - Early-onset severe infections (bacterial, viral, fungal, opportunistic)
  - Failure to thrive and growth retardation
  - Chronic diarrhea and malabsorption
  - Fatal outcome without HSCT
* **Inheritance**: Autosomal recessive
* **Treatment**: Hematopoietic stem cell transplantation is curative

### JAK3 Activation (Gain-of-function)
Drives **hematological malignancies**:
* **T-cell acute lymphoblastic leukemia** (T-ALL)
* **T-cell prolymphocytic leukemia** (T-PLL)
* **Natural killer/T-cell lymphomas** (NKTCL)
* **Large granular lymphocyte leukemia** (T-LGL)
* **Mechanism**: Constitutive STAT5 activation promoting cell survival and proliferation