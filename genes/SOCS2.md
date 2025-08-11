---
id: UniProtKB:O14508
symbol: SOCS2
primary_functions:
- description: SOCS2 is a negative feedback regulator that inhibits growth hormone
    and cytokine signaling by targeting receptors and JAKs for proteasomal degradation
  activity:
    term:
      id: GO:0019209
      label: kinase regulator activity
    support: []
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    notes: SOCS2 is recruited to activated cytokine receptors at the plasma membrane
  upstream:
  - term:
      id: GO:0060396
      label: growth hormone receptor signaling pathway
    description: SOCS2 expression is induced by GH-activated STAT5B
  downstream:
  - term:
      id: GO:0046627
      label: negative regulation of insulin receptor signaling pathway
    support: []
    description: SOCS2 promotes degradation of insulin receptor substrate proteins
  processes:
  - term:
      id: GO:0040036
      name: regulation of fibroblast growth factor receptor signaling pathway
    support: []
  - term:
      id: GO:0009968
      name: negative regulation of signal transduction
    support: []
- description: SOCS2 functions as an E3 ubiquitin ligase substrate adapter promoting
    proteasomal degradation of signaling proteins
  activity:
    term:
      id: GO:0031625
      label: ubiquitin protein ligase binding
    support: []
  processes:
  - term:
      id: GO:0016567
      name: protein ubiquitination
    support: []
  - term:
      id: GO:0030163
      name: protein catabolic process
    support: []
  roles:
  - term:
      id: GO:0040014
      label: regulation of multicellular organism growth
    notes: SOCS2 limits body size by attenuating GH signaling
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: gigantism with 30-40% increase in body size
    mechanism: unrestrained growth hormone signaling leads to excessive IGF-1 production
    term:
      id: HP:0000098
      label: Tall stature
    support: []
  - description: increased bone length and density
    mechanism: enhanced GH/IGF-1 signaling in growth plates
    term:
      id: HP:0002652
      label: Skeletal dysplasia
    support: []
  - description: enhanced muscle mass
    mechanism: increased IGF-1 and insulin signaling in skeletal muscle
    term:
      id: HP:0003712
      label: Skeletal muscle hypertrophy
    support: []
  - description: metabolic changes with improved insulin sensitivity (protective against
      diabetes)
    mechanism: altered cross-talk between GH and insulin signaling
    term:
      id: HP:0000831
      label: Insulin-dependent diabetes mellitus
    support: []
  - description: organomegaly with proportional organ enlargement
    mechanism: systemic effects of enhanced GH/IGF-1 signaling on organ growth
    term:
      id: HP:0001548
      label: Overgrowth
    support: []
- mutation:
    type: overexpression
  effects:
  - description: growth retardation
    mechanism: excessive inhibition of GH signaling
    term:
      id: HP:0001510
      label: Growth delay
    support: []
  - description: reduced fertility
    mechanism: disrupted prolactin signaling
    term:
      id: HP:0000144
      label: Decreased fertility
    support: []
---
**SOCS2 (Suppressor of Cytokine Signaling 2)** is a negative feedback regulator that controls **growth hormone signaling** and **body size** by promoting degradation of GH receptor and downstream signaling components.

## Function

* **Growth hormone regulation:** SOCS2 is the primary SOCS limiting GH action:
  * **GH-induced expression:** STAT5B activates SOCS2 transcription
  * **GH receptor binding:** SH2 domain recognizes phospho-Y487 and Y595
  * **Signal termination:** Blocks JAK2 access and STAT5 activation
  * **Receptor degradation:** Targets GH receptor for proteasomal destruction
  * **Body size control:** Fine-tunes postnatal growth rate

* **E3 ubiquitin ligase function:** SOCS2 acts as substrate adapter:
  * **Elongin BC recruitment:** SOCS box binds Elongin B/C complex
  * **Cullin5 assembly:** Forms functional E3 ligase complex
  * **Substrate targeting:** SH2 domain determines specificity
  * **Protein degradation:** K48-linked ubiquitination for proteasome

* **Substrate specificity:** SOCS2 targets multiple proteins:
  * **GH receptor** - primary physiological target
  * **Prolactin receptor** - lactation and reproduction
  * **Erythropoietin receptor** - erythropoiesis regulation
  * **IRS-1/IRS-2** - insulin and IGF-1 signaling
  * **FLT3** - hematopoietic progenitor regulation

* **Cross-regulation of SOCS proteins:**
  * Can target other SOCS family members for degradation
  * Particularly SOCS1 and SOCS3
  * Creates hierarchy of SOCS protein stability
  * Modulates inflammatory responses

* **Tissue expression pattern:**
  * **Liver:** High expression, GH-responsive
  * **Muscle:** Growth and metabolism regulation
  * **Adipose:** Energy homeostasis
  * **Brain:** Hypothalamus and pituitary
  * **Immune cells:** T cells and macrophages

* **Developmental regulation:**
  * Low expression in fetal life
  * Increases postnatally with GH pulses
  * Sexual dimorphism in expression patterns
  * Age-related changes in expression

* **Protein structure:**
  * **N-terminal region:** Variable, regulatory
  * **SH2 domain:** Phosphotyrosine binding
  * **SOCS box:** Elongin BC interaction
  * **185 amino acids** - smallest SOCS protein

* **Regulation of SOCS2:**
  * **Transcriptional:** STAT5-induced, GH-responsive
  * **Post-translational:** Phosphorylation affects stability
  * **Auto-ubiquitination:** Self-limits SOCS2 levels
  * **MicroRNAs:** miR-194 and others regulate expression

## Clinical Significance

* **SOCS2 and growth disorders:**
  * SNPs associated with height variation
  * rs3782415 linked to adult stature
  * Potential therapeutic target for growth disorders
  * Balance between growth promotion and cancer risk

* **Metabolic effects:**
  * SOCS2 deletion improves glucose tolerance
  * Enhanced insulin sensitivity in muscle and liver
  * Protection from diet-induced obesity and diabetes
  * Complex GH-insulin signaling crosstalk
  * Altered adipocyte differentiation and fat distribution

* **Cancer implications:**
  * Frequently methylated/silenced in cancers
  * Loss promotes growth factor signaling
  * May act as tumor suppressor
  * Particularly in hepatocellular carcinoma

* **Inflammatory diseases:**
  * Regulates cytokine responses in immune cells
  * Affects macrophage polarization
  * Modulates T cell differentiation
  * Potential role in autoimmunity

## Phenotypes

### SOCS2 Deficiency (Loss-of-function)
**Gigantism syndrome** with systemic overgrowth:

#### Growth Characteristics
* **Body size**: 30-40% increase in weight and length
* **Proportional growth**: All organs enlarged proportionally
* **Extended growth period**: Prolonged postnatal growth phase
* **Normal lifespan**: Despite large size, no adverse effects on longevity

#### Skeletal System
* **Bone length**: Significantly increased long bone length
* **Bone density**: Enhanced bone mineral density
* **Growth plates**: Extended activity and delayed closure
* **Vertebral growth**: Increased spine length

#### Muscle System
* **Muscle mass**: Enhanced skeletal muscle hypertrophy
* **Fiber size**: Increased myofiber diameter
* **Strength**: Improved muscle function and performance
* **Regeneration**: Enhanced muscle repair capacity

#### Metabolic Benefits
* **Glucose homeostasis**: Improved glucose tolerance
* **Insulin sensitivity**: Enhanced insulin action in tissues
* **Diabetes protection**: Resistance to diet-induced diabetes
* **Fat distribution**: Altered adipogenesis and fat storage

#### Mechanism
* **GH hypersensitivity**: Unrestrained GH receptor signaling
* **IGF-1 elevation**: Sustained high IGF-1 production
* **STAT5 activation**: Prolonged STAT5 phosphorylation
* **Metabolic reprogramming**: Enhanced anabolic pathways

### SOCS2 Overexpression (Gain-of-function)
**Growth retardation syndrome**:
* **Dwarfism**: Severe growth retardation
* **IGF-1 deficiency**: Markedly reduced IGF-1 levels
* **Reproductive dysfunction**: Impaired fertility
* **Metabolic dysfunction**: Insulin resistance

### Clinical Relevance
* **Human height variation**: SOCS2 SNPs associated with adult stature
* **Growth disorders**: Potential therapeutic target
* **Metabolic disease**: Role in diabetes and obesity
* **Cancer**: Tumor suppressor function in some cancers

### Sexual Dimorphism
* **Male-predominant gigantism**: Reflects GH pulse patterns
* **Female fertility**: Better preserved in females
* **Reproductive enhancement**: Improved male fertility parameters
* **Tissue-specific effects**: Variable response by organ system