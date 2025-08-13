---
id: UniProtKB:P29597
symbol: TYK2
primary_functions:
- description: TYK2 is a non-receptor tyrosine kinase that transduces signals from
    type I interferons, IL-12, and IL-23 to mediate antiviral immunity and Th1/Th17
    responses
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
    notes: TYK2 associates with IFNAR1, IL-12Rβ1, IL-10R2, and IL-13Rα1 cytoplasmic
      domains
  upstream:
  - term:
      id: GO:0004896
      label: cytokine receptor activity
    description: Activated by type I IFNs, IL-12, IL-23, IL-10, and IL-13 binding
      to their respective receptors
  downstream:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Phosphorylates STAT proteins (STAT1, STAT2, STAT3, STAT4) to activate
      transcription
  processes:
  - term:
      id: GO:0060337
      name: type I interferon-mediated signaling pathway
    support: []
  - term:
      id: GO:0035722
      name: interleukin-12-mediated signaling pathway
    support: []
  - term:
      id: GO:0070757
      name: interleukin-23-mediated signaling pathway
    support: []
- description: TYK2 coordinates innate antiviral responses and bridges to adaptive
    immunity through IFN and IL-12/IL-23 signaling
  activity:
    term:
      id: GO:0051607
      label: defense response to virus
    support: []
  processes:
  - term:
      id: GO:0002376
      name: immune system process
    is_any_of:
    - term:
        id: GO:0045087
        name: innate immune response
      support: []
    - term:
        id: GO:0002250
        name: adaptive immune response
      support: []
  roles:
  - term:
      id: GO:0042088
      label: T-helper 1 type immune response
    notes: Essential for IL-12-induced Th1 differentiation and IFN-γ production
  - term:
      id: GO:0072539
      label: T-helper 17 cell differentiation
    notes: Required for IL-23-mediated Th17 maintenance and IL-17 production
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: primary immunodeficiency with mycobacterial and viral susceptibility
    mechanism: impaired type I IFN and IL-12/IL-23 signaling reduces antimicrobial
      immunity
    term:
      id: MONDO:0015136
      label: primary immunodeficiency due to a defect in innate immunity
    support: []
  - description: increased susceptibility to mycobacterial infections
    term:
      id: HP:0032251
      label: Increased susceptibility to mycobacterial infections
    support: []
  - description: severe viral infections including HSV encephalitis
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
  - description: normal IgE levels unlike hyper-IgE syndrome (absence of elevated
      IgE)
    mechanism: preserved IL-4 signaling distinguishes TYK2 deficiency from STAT3 defects
    term:
      id: HP:0003212
      label: Increased circulating IgE concentration
    support: []
  - description: chronic mucocutaneous candidiasis
    mechanism: impaired IL-17 production due to defective IL-23 signaling
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
- mutation:
    type: partial_loss_of_function
    variant: P1104A
  effects:
  - description: protection against multiple sclerosis and inflammatory bowel disease
      (reduced risk)
    mechanism: reduced IL-23 and type I IFN signaling decreases pathogenic inflammation
    term:
      id: HP:0002960
      label: Autoimmunity
    support: []
  - description: tuberculosis susceptibility in homozygotes
    term:
      id: HP:0032263
      label: Tuberculosis susceptibility
    support: []
- mutation:
    type: gain_of_function
  effects:
  - description: T cell acute lymphoblastic leukemia
    mechanism: constitutive STAT activation drives T cell transformation
    term:
      id: MONDO:0004963
      label: T-cell acute lymphoblastic leukemia
    support: []
  - description: B cell acute lymphoblastic leukemia
    mechanism: dysregulated STAT3/5 activation in B cell progenitors
    term:
      id: MONDO:0004967
      label: B-cell acute lymphoblastic leukemia
    support: []
---
**TYK2 (Tyrosine Kinase 2)** is a non-receptor tyrosine kinase that mediates signaling from **type I interferons**, **IL-12**, **IL-23**, and **IL-10** family cytokines, bridging innate and adaptive immunity.

## Function

* **Cytokine receptor partnerships:** TYK2 associates with specific receptor chains:
  * **IFNAR1** (type I IFN receptor) → pairs with JAK1 on IFNAR2
  * **IL-12Rβ1** → pairs with JAK2 on IL-12Rβ2
  * **IL-23R** → pairs with JAK2 on IL-12Rβ1
  * **IL-10R2** → pairs with JAK1 on IL-10R1
  * **IL-13Rα1** → pairs with JAK1/JAK2 on IL-4Rα

* **Type I interferon signaling:** TYK2-JAK1 activation leads to:
  * STAT1-STAT2 heterodimer formation
  * Assembly of ISGF3 complex (STAT1-STAT2-IRF9)
  * Transcription of hundreds of interferon-stimulated genes (ISGs)
  * Antiviral state establishment in infected and neighboring cells

* **IL-12/IL-23 axis:** TYK2-JAK2 signaling promotes:
  * **IL-12 signaling:** STAT4 activation → Th1 differentiation → IFN-γ production
  * **IL-23 signaling:** STAT3 activation → Th17 maintenance → IL-17/IL-22 production
  * Critical for immunity against intracellular bacteria and fungi

* **IL-10 family signaling:** TYK2 mediates anti-inflammatory signals:
  * IL-10 → STAT3 activation → suppression of pro-inflammatory cytokines
  * IL-22 → STAT3 activation → epithelial barrier defense
  * IL-26 → antimicrobial peptide production

* **Unique structural features:**
  * Contains FERM domain for receptor association
  * Pseudokinase domain regulates kinase activity
  * Kinase domain with dual tyrosine activation sites (Y1054/Y1055)

* **Selective functions vs other JAKs:**
  * Non-redundant for type I IFN antiviral responses
  * Partially redundant with JAK2 for IL-12/IL-23 signaling
  * Dispensable for development (unlike JAK1/JAK2/JAK3)

* **Regulation:**
  * **SOCS1** - potent inhibitor of TYK2 kinase activity
  * **USP18** - specific negative regulator of type I IFN signaling
  * **Protein phosphatases** (TCPTP, SHP-1)

## Clinical Significance

* **TYK2 deficiency (rare):**
  * <20 reported cases worldwide
  * Autosomal recessive inheritance
  * Increased susceptibility to mycobacteria, viruses, and fungi
  * NO hyper-IgE syndrome (distinguishes from STAT3 deficiency)
  * Relatively mild phenotype compared to JAK3 or STAT1 deficiency
  * Compatible with survival to adulthood

* **TYK2 P1104A variant:**
  * Common protective variant (~4% of Europeans, ~1% globally)
  * Reduces autoimmune disease risk (MS, IBD, psoriasis, SLE)
  * Increases tuberculosis risk in homozygotes
  * Represents evolutionary trade-off between infection and autoimmunity
  * Natural model for TYK2 inhibition safety

* **Therapeutic targeting:**
  * **Deucravacitinib**: Selective TYK2 inhibitor approved for psoriasis
  * Under investigation for SLE, IBD, and other autoimmune diseases
  * **Advantages**: Selective TYK2 inhibition preserves JAK1/2/3 functions
  * **Safety profile**: Based on P1104A variant data

## Phenotypes

### Complete TYK2 Deficiency (Loss-of-function)
**Primary immunodeficiency** without hyper-IgE syndrome:
* **Mycobacterial infections**: 
  - Disseminated BCG infection in infancy
  - Atypical mycobacteria (MAC, M. fortuitum)
  - Tuberculosis susceptibility
  - Salmonella infections
* **Viral infections**:
  - HSV encephalitis and recurrent HSV
  - Severe VZV with complications
  - Prolonged influenza and CMV
  - Impaired antiviral IFN responses
* **Fungal infections**:
  - Chronic mucocutaneous candidiasis
  - Impaired Th17 responses
* **Distinguishing features**:
  - Normal IgE levels (unlike STAT3 deficiency)
  - No eczema or skeletal abnormalities
  - Normal T, B, NK cell development
  - Selective cytokine signaling defects

### Partial TYK2 Deficiency (P1104A variant)
**Balanced immunity-autoimmunity trade-off**:
* **Autoimmune protection**:
  - Reduced multiple sclerosis risk (OR ~0.7)
  - Crohn's disease protection
  - Psoriasis risk reduction
  - SLE protection
* **Infection susceptibility**:
  - Increased tuberculosis risk (homozygotes)
  - Mild mycobacterial susceptibility
  - Generally preserved antiviral immunity
* **Mechanism**: ~75% reduction in TYK2 kinase activity
* **Frequency**: ~4% in Europeans, varies by population

### TYK2 Activation (Gain-of-function)
**Hematological malignancies**:
* **T-cell acute lymphoblastic leukemia**
* **B-cell acute lymphoblastic leukemia** 
* **Mechanism**: Constitutive STAT1/3/4/5 activation
* **Frequency**: Rare driver mutations in lymphoid cancers