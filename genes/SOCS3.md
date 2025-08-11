---
id: UniProtKB:O14543
symbol: SOCS3
primary_functions:
- description: SOCS3 is a negative feedback regulator that inhibits IL-6, leptin,
    and G-CSF signaling by binding to phosphorylated receptors and inhibiting JAK
    activity
  activity:
    term:
      id: GO:0004860
      label: protein kinase inhibitor activity
    support: []
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    notes: SOCS3 is recruited to activated cytokine receptors containing phospho-Y757
      on gp130
  upstream:
  - term:
      id: GO:0070102
      label: interleukin-6-mediated signaling pathway
    description: SOCS3 expression is rapidly induced by IL-6-activated STAT3
  - term:
      id: GO:0033210
      label: leptin-mediated signaling pathway
    description: Leptin induces SOCS3 as negative feedback
  downstream:
  - term:
      id: GO:0046627
      label: negative regulation of insulin receptor signaling pathway
    support: []
    description: SOCS3 inhibits insulin signaling contributing to insulin resistance
  processes:
  - term:
      id: GO:0050728
      name: negative regulation of inflammatory response
    support: []
  - term:
      id: GO:0001959
      name: regulation of cytokine-mediated signaling pathway
    support: []
- description: SOCS3 controls inflammatory responses and metabolic homeostasis by
    selectively inhibiting specific cytokine pathways
  activity:
    term:
      id: GO:0019221
      label: cytokine-mediated signaling pathway
    support: []
  processes:
  - term:
      id: GO:0045444
      name: fat cell differentiation
    support: []
  - term:
      id: GO:0030335
      name: positive regulation of cell migration
    support: []
  roles:
  - term:
      id: GO:0032868
      label: response to insulin
    notes: SOCS3 mediates cytokine-induced insulin resistance in obesity
  - term:
      id: GO:0014070
      label: response to organic cyclic compound
    notes: Mediates leptin resistance in hypothalamus
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: embryonic lethality at E12-16 due to placental insufficiency
    mechanism: uncontrolled LIF signaling disrupts trophoblast differentiation
    term:
      id: HP:0001511
      label: Intrauterine growth retardation
    support: []
  - description: systemic inflammation in conditional knockouts
    mechanism: prolonged STAT3 activation and excessive inflammatory cytokines
    term:
      id: HP:0012649
      label: Increased inflammatory response
    support: []
  - description: enhanced G-CSF signaling leading to neutrophilia
    mechanism: loss of negative feedback on G-CSF receptor
    term:
      id: HP:0011897
      label: Neutrophilia
    support: []
  - description: inflammatory arthritis in conditional knockouts
    mechanism: unrestrained IL-6 signaling in joints
    term:
      id: HP:0001369
      label: Arthritis
    support: []
  - description: protection from diet-induced obesity (resistance to weight gain)
    mechanism: enhanced leptin sensitivity in hypothalamus
    term:
      id: HP:0001513
      label: Obesity
    support: []
  - description: enhanced insulin sensitivity and glucose tolerance
    mechanism: reduced inflammatory interference with insulin signaling
    term:
      id: HP:0000855
      label: Insulin resistance
    support: []
- mutation:
    type: overexpression
  effects:
  - description: insulin resistance and glucose intolerance
    mechanism: inhibition of insulin receptor signaling
    term:
      id: HP:0000855
      label: Insulin resistance
    support: []
  - description: leptin resistance and obesity
    mechanism: blocks leptin signaling in hypothalamic neurons
    term:
      id: HP:0001513
      label: Obesity
    support: []
  - description: impaired liver regeneration
    mechanism: blocks IL-6-mediated hepatocyte proliferation
    term:
      id: HP:0001399
      label: Hepatic failure
    support: []
  - description: increased susceptibility to inflammatory diseases
    mechanism: impaired resolution of inflammation due to prolonged STAT3 signaling
    term:
      id: HP:0012649
      label: Increased inflammatory response
    support: []
---
**SOCS3 (Suppressor of Cytokine Signaling 3)** is a critical negative regulator of **IL-6**, **leptin**, and **G-CSF** signaling that controls **inflammation**, **metabolism**, and **hematopoiesis**.

## Function

* **IL-6 family regulation:** SOCS3 specifically controls gp130-dependent signaling:
  * **IL-6:** Binds phospho-Y757 on gp130
  * **LIF:** Placental development and stem cell maintenance
  * **OSM:** Inflammatory responses
  * **IL-11:** Hematopoiesis and bone metabolism
  * **CNTF:** Neuroprotection and metabolism
  * **CT-1:** Cardiac function

* **Mechanism of inhibition:**
  * **Receptor binding:** SH2 domain recognizes gp130 pY757
  * **JAK inhibition:** KIR (kinase inhibitory region) blocks JAK activity
  * **Unique specificity:** Only SOCS1 and SOCS3 have functional KIR
  * **Pseudo-substrate:** KIR acts as JAK pseudosubstrate
  * **Signal duration control:** Limits STAT3 activation to ~30-60 minutes

* **Metabolic regulation:**
  * **Leptin resistance:** Central mechanism of obesity
  * **Insulin resistance:** Links inflammation to diabetes
  * **Hepatic metabolism:** Controls glucose production
  * **Adipocyte function:** Regulates differentiation and inflammation
  * **Energy homeostasis:** Hypothalamic appetite control

* **Inflammatory control:**
  * **Acute phase response:** Limits duration and magnitude
  * **Macrophage polarization:** Promotes M2 anti-inflammatory phenotype
  * **T cell differentiation:** Inhibits Th17, promotes Treg
  * **Dendritic cell function:** Controls maturation and cytokine production
  * **Emergency granulopoiesis:** Regulates G-CSF responses

* **SOCS3 vs SOCS1 specificity:**
  * SOCS3: gp130 cytokines, leptin, G-CSF
  * SOCS1: interferons, IL-2, IL-7
  * Different receptor binding sites
  * Non-redundant physiological roles

* **Tissue-specific functions:**
  * **Hypothalamus:** Leptin sensitivity, feeding behavior
  * **Liver:** Acute phase response, regeneration
  * **Adipose:** Insulin sensitivity, inflammation
  * **Immune cells:** Cytokine responsiveness
  * **Placenta:** Trophoblast differentiation

* **Transcriptional regulation:**
  * **STAT3-induced:** Primary mechanism, rapid (15-30 min)
  * **NF-κB-induced:** During inflammation
  * **STAT1-induced:** IFN-γ stimulation
  * **HIF-1α-induced:** Hypoxic conditions
  * **MicroRNA regulation:** miR-155, miR-19a, miR-203

* **Protein characteristics:**
  * 225 amino acids
  * KIR domain (residues 22-29)
  * Extended SH2 subdomain (ESS)
  * SOCS box for E3 ligase function
  * Short half-life (~1-2 hours)

## Clinical Significance

* **SOCS3 and obesity:**
  * Elevated in obesity-induced inflammation
  * Mediates leptin resistance in hypothalamus (key mechanism)
  * Links adipose tissue inflammation to systemic insulin resistance
  * Central hub connecting inflammation and metabolic dysfunction
  * Therapeutic target for metabolic syndrome and type 2 diabetes

* **Inflammatory diseases:**
  * **Rheumatoid arthritis:** Elevated in synovium
  * **IBD:** Dysregulated in intestinal inflammation
  * **Psoriasis:** Overexpressed in skin lesions
  * **Multiple sclerosis:** Affects Th17/Treg balance

* **Cancer:**
  * Frequently silenced by methylation
  * Loss promotes STAT3-driven tumors
  * Particularly in hepatocellular carcinoma
  * May enhance response to immunotherapy

* **Therapeutic implications:**
  * SOCS3 mimetics for inflammation
  * SOCS3 inhibitors for improving leptin sensitivity
  * Cell-specific targeting crucial
  * Balance between metabolic and immune effects

## Phenotypes

### SOCS3 Complete Deficiency (Loss-of-function)
**Embryonic lethality** (E12-16) due to:
* **Placental insufficiency**: Defective trophoblast giant cell differentiation
* **Excessive LIF signaling**: Uncontrolled STAT3 activation
* **Vascular defects**: Impaired placental vascularization
* **Erythrocytosis**: Embryonic polycythemia
* **Growth defects**: Severe developmental abnormalities

### Conditional SOCS3 Deficiency (Tissue-specific)

#### Neuronal SOCS3 Deletion
* **Leptin hypersensitivity**: Enhanced satiety signaling
* **Obesity resistance**: Protection from high-fat diet
* **Improved metabolism**: Enhanced energy expenditure
* **Neuroprotection**: Reduced neuroinflammation

#### Hepatocyte SOCS3 Deletion
* **Enhanced regeneration**: Improved liver repair capacity
* **Prolonged STAT3 signaling**: Extended hepatocyte proliferation
* **Improved insulin sensitivity**: Reduced hepatic glucose production
* **Enhanced acute phase response**: Increased cytokine responses

#### Myeloid SOCS3 Deletion
* **Fatal inflammatory disease**: Severe systemic inflammation
* **Neutrophilia**: Excessive G-CSF responses
* **Enhanced M1 polarization**: Pro-inflammatory macrophages
* **Autoimmune features**: Multi-organ inflammation

#### T Cell SOCS3 Deletion
* **Enhanced Th17 differentiation**: Increased IL-17 production
* **Prolonged IL-6 responses**: Sustained STAT3 activation
* **Autoimmune susceptibility**: Enhanced inflammatory responses
* **Reduced Treg function**: Impaired immune tolerance

#### Adipocyte SOCS3 Deletion
* **Improved insulin sensitivity**: Enhanced glucose uptake
* **Reduced inflammation**: Decreased adipose macrophages
* **Metabolic protection**: Resistance to diet-induced dysfunction
* **Enhanced lipolysis**: Improved fat mobilization

### SOCS3 Overexpression (Gain-of-function)

#### Metabolic Dysfunction
* **Severe insulin resistance**: Blocked insulin signaling
* **Glucose intolerance**: Impaired glucose homeostasis
* **Leptin resistance**: Hypothalamic leptin insensitivity
* **Diet-induced obesity**: Enhanced weight gain
* **Fatty liver disease**: Hepatic steatosis

#### Inflammatory Consequences
* **Impaired liver regeneration**: Blocked IL-6 responses
* **Enhanced susceptibility to infection**: Reduced immune responses
* **Delayed wound healing**: Impaired tissue repair
* **Increased cancer risk**: Reduced tumor surveillance

### Human Clinical Associations
* **Type 2 diabetes**: SOCS3 polymorphisms affect diabetes risk
* **Obesity**: Variants influence BMI and leptin sensitivity
* **Inflammatory diseases**: SNPs associated with RA, IBD severity
* **Hepatitis C treatment**: SOCS3 levels predict IFN response
* **Metabolic syndrome**: Central role in inflammation-metabolism axis