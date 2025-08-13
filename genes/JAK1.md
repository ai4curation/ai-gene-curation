---
id: UniProtKB:P23458
symbol: JAK1
primary_functions:
- description: JAK1 is a non-receptor tyrosine kinase that phosphorylates cytokine
    receptors and STAT proteins to transduce signals from interferons and interleukins
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
    notes: JAK1 associates with the cytoplasmic domain of transmembrane cytokine receptors
  upstream:
  - term:
      id: GO:0004896
      label: cytokine receptor activity
    description: Activated by cytokine binding to receptor complexes (IFNAR, IL-2R,
      IL-10R)
  downstream:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Phosphorylates STAT proteins (STAT1, STAT2, STAT3) and cytokine receptors
      creating docking sites
  processes:
  - term:
      id: GO:0007259
      name: cell surface receptor signaling pathway via JAK-STAT
    support: null
  - term:
      id: GO:0060337
      name: type I interferon-mediated signaling pathway
    support: []
  - term:
      id: GO:0060333
      name: type II interferon-mediated signaling pathway
    support: []
  roles:
  - term:
      id: GO:0030183
      label: B cell differentiation
    notes: Essential for IL-4 mediated B cell responses
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: severe combined immunodeficiency with defective responses to cytokines
    term:
      id: HP:0004430
      label: Severe combined immunodeficiency
    support: []
  - description: increased susceptibility to mycobacterial and viral infections
    mechanism: impaired interferon signaling and defective T cell/NK cell development
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
  - description: defective T cell development and function
    mechanism: impaired IL-7 and IL-15 signaling essential for T cell maturation
    term:
      id: HP:0005403
      label: Decreased total T cell count
    support: []
  - description: impaired NK cell function
    mechanism: defective IL-15 signaling required for NK cell development and cytotoxicity
    term:
      id: HP:0040218
      label: Reduced total natural killer cell count
    support: []
- mutation:
    type: gain_of_function
  effects:
  - description: autoinflammatory syndrome with hepatosplenomegaly
    term:
      id: HP:0001433
      label: Hepatosplenomegaly
    support: []
  - description: hyperinflammation and cytokine storm
    term:
      id: HP:0033041
      label: Cytokine storm
    support: []
  - description: hypereosinophilia
    mechanism: constitutive IL-5 signaling through activated JAK1-STAT5 pathway
    term:
      id: HP:0001880
      label: Increased total eosinophil count
    support: []
  - description: atopic dermatitis-like skin inflammation
    mechanism: aberrant Th2 responses and enhanced IL-4/IL-13 signaling
    term:
      id: HP:0000964
      label: Eczema
    support: []
---
**JAK1 (Janus Kinase 1)** is a non-receptor tyrosine kinase that serves as a critical signal transducer for multiple cytokine receptors, particularly **interferon receptors** and various **interleukin receptors**.

## Function

* **Cytokine receptor signaling:** Essential kinase partner for type I interferon receptor (IFNAR1/IFNAR2), type II interferon receptor (IFNGR1/IFNGR2), IL-2 receptor, IL-4 receptor, IL-7 receptor, IL-9 receptor, IL-10 receptor, and IL-15 receptor complexes.

* **Activation mechanism:** Upon cytokine binding to its receptor, JAK1 undergoes trans-phosphorylation with its partner JAK (JAK2, JAK3, or TYK2), leading to activation of its kinase domain. The conserved activation loop tyrosines Y1038/Y1039 are critical for kinase activity.

* **Substrate phosphorylation:** Activated JAK1 phosphorylates:
  * **Cytokine receptors** on specific tyrosine residues, creating SH2 docking sites
  * **STAT proteins** (STAT1, STAT2, STAT3, STAT5, STAT6) enabling their dimerization and nuclear translocation
  * **Other signaling proteins** including PI3K, SHP-2, and SOCS proteins

* **Signaling specificity:** Different cytokine-JAK combinations activate distinct STAT proteins:
  * IFN-α/β → JAK1/TYK2 → STAT1/STAT2
  * IFN-γ → JAK1/JAK2 → STAT1
  * IL-2/IL-15 → JAK1/JAK3 → STAT5
  * IL-4 → JAK1/JAK3 → STAT6
  * IL-10 → JAK1/TYK2 → STAT3

* **Regulation:** JAK1 activity is controlled by:
  * **SOCS proteins** (SOCS1, SOCS3) - negative feedback inhibitors
  * **Protein phosphatases** (SHP-1, SHP-2, CD45, PTP1B)
  * **PIAS proteins** - inhibit STAT DNA binding
  * **CIS (CISH)** - competes with STAT5 for receptor binding
  * **Protein inhibitors** - PIAS1/3/4 SUMOylate and inhibit STATs

## Phenotypes

### Loss-of-function mutations
Cause **combined immunodeficiency** with:
* **Severe infections**: Particularly mycobacterial (including BCG, NTM) and viral (CMV, EBV)
* **T cell defects**: Profound lymphopenia with impaired IL-2, IL-7, IL-15 responses
* **NK cell dysfunction**: Reduced numbers and cytotoxicity due to defective IL-15 signaling
* **Interferon unresponsiveness**: Complete loss of IFN-α and IFN-γ signaling
* **B cell dysfunction**: Despite normal numbers, poor antibody responses due to lack of T cell help
* **Clinical presentation**: Early-onset severe infections, failure to thrive, often fatal without HSCT

### Gain-of-function mutations
Cause **autoinflammatory syndrome** with:
* **Hypereosinophilia**: Marked eosinophilia with tissue infiltration
* **Atopic features**: Severe eczema, elevated IgE, food allergies
* **Organomegaly**: Hepatosplenomegaly and lymphadenopathy
* **Cytokine storm**: Elevated inflammatory mediators and systemic inflammation
* **Mechanism**: Constitutive STAT1/3/5 activation leading to dysregulated immune responses