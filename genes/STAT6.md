---
id: UniProtKB:P42226
symbol: STAT6
primary_functions:
- description: STAT6 is a transcription factor that transduces IL-4 and IL-13 signals
    to promote Th2 differentiation, B cell class switching, and allergic responses
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
    notes: STAT6 translocates from cytoplasm to nucleus upon IL-4-induced phosphorylation
  upstream:
  - term:
      id: GO:0038094
      label: interleukin-4-mediated signaling pathway
    description: Activated by JAK1/JAK3 phosphorylation at Y641 following IL-4R engagement
  - term:
      id: GO:0038095
      label: interleukin-13-mediated signaling pathway
    description: JAK1/JAK2/TYK2-mediated activation via IL-13R
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: STAT6 activates GATA3, IL-4Rα, and immunoglobulin germline transcripts
  processes:
  - term:
      id: GO:0042092
      name: type 2 immune response
    support: []
  - term:
      id: GO:0045064
      name: T-helper 2 cell differentiation
    support: []
- description: STAT6 mediates B cell class switch recombination to IgE and IgG1 through
    IL-4 signaling
  activity:
    term:
      id: GO:0016446
      label: somatic hypermutation of immunoglobulin genes
    support: []
  processes:
  - term:
      id: GO:0048289
      name: isotype switching to IgE
    support: []
  - term:
      id: GO:0048291
      name: isotype switching to IgG1
    support: []
  roles:
  - term:
      id: GO:0043372
      label: positive regulation of CD4+ T cell differentiation
    notes: Essential for Th2 lineage commitment via GATA3 induction
  - term:
      id: GO:0002230
      label: positive regulation of defense response to virus
    notes: Required for alternative macrophage activation
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: impaired Th2 responses with reduced IL-4, IL-5, and IL-13 production
    mechanism: failure to induce GATA3 and Th2 differentiation program
    term:
      id: HP:0005374
      label: Abnormality of cellular immune system
    support: []
  - description: defective IgE class switching
    mechanism: absence of germline Cε transcription
    term:
      id: HP:0410242
      label: Decreased circulating IgE level
    support: []
  - description: resistance to allergic inflammation (protective effect)
    mechanism: inability to mount Th2 and IgE responses
    term:
      id: HP:0012384
      label: Rhinitis
    support: []
  - description: enhanced susceptibility to helminth infections
    mechanism: impaired type 2 immunity required for worm expulsion
    term:
      id: HP:0002719
      label: Recurrent infections
    support: []
- mutation:
    type: gain_of_function
    variant: polymorphisms
  effects:
  - description: increased risk of allergic diseases
    mechanism: enhanced IL-4/IL-13 responsiveness
    term:
      id: MONDO:0005271
      label: allergic disease
    support: []
  - description: atopic dermatitis susceptibility
    term:
      id: MONDO:0011292
      label: atopic dermatitis
    support: []
  - description: asthma susceptibility
    term:
      id: MONDO:0004979
      label: asthma
    support: []
  - description: elevated IgE levels
    term:
      id: HP:0003212
      label: Increased circulating IgE level
    support: []
---
**STAT6 (Signal Transducer and Activator of Transcription 6)** is the essential transcription factor for **IL-4** and **IL-13** signaling, orchestrating **Th2 differentiation**, **IgE class switching**, and **allergic responses**.

## Function

* **IL-4/IL-13 signal transduction:** STAT6 is the sole STAT mediating:
  * **IL-4 signaling:** Via IL-4Rα/γc (Type I) or IL-4Rα/IL-13Rα1 (Type II) receptors
  * **IL-13 signaling:** Via IL-4Rα/IL-13Rα1 (Type II) receptor only
  * JAK1/JAK3 (IL-4) or JAK1/JAK2/TYK2 (IL-13) phosphorylate STAT6 at Y641
  * STAT6 homodimers bind N4 GAS sites (TTCN₄GAA)

* **Th2 differentiation program:** STAT6 induces:
  * **GATA3** - master Th2 transcription factor
  * **IL-4Rα** - positive feedback amplification
  * **IL-4, IL-5, IL-13** - Th2 effector cytokines
  * **CCR4, CCR8** - Th2 homing receptors
  * **c-MAF** - IL-4 transcriptional activator

* **B cell functions:** STAT6 controls:
  * **Germline transcription:** Iε and Iγ1 promoters
  * **IgE class switching:** Essential for allergic antibody production
  * **IgG1 class switching:** Mouse equivalent of human IgG4
  * **CD23 expression:** Low-affinity IgE receptor
  * **MHC class II upregulation:** Antigen presentation

* **Alternative macrophage activation (M2):** STAT6 drives:
  * **Arginase-1** - L-arginine metabolism
  * **FIZZ1/RELMα** - tissue remodeling
  * **YM1/YM2** - chitinase-like proteins
  * **Mannose receptor** - pathogen recognition
  * **IL-10** - anti-inflammatory cytokine

* **Epithelial and tissue responses:**
  * **Mucus production:** MUC5AC, MUC5B genes
  * **Goblet cell hyperplasia:** SPDEF, FOXA3 induction
  * **Smooth muscle:** Contractility and proliferation
  * **Fibroblasts:** Collagen production and remodeling
  * **Barrier function:** Tight junction proteins

* **Target gene binding specificity:**
  * Recognizes N4 GAS motifs (longer spacer than other STATs)
  * Often binds as homodimers to palindromic sites
  * Can form enhanceosomes with GATA3, PU.1, C/EBPβ
  * Pioneer factor activity at some loci

* **Protein domains and regulation:**
  * N-terminal domain - protein interactions
  * Coiled-coil - nuclear import/export
  * DNA-binding domain - N4 GAS recognition
  * SH2 domain - phosphotyrosine binding
  * C-terminal transactivation domain
  * Arginine methylation modulates activity

* **Negative regulation:**
  * **SOCS1** - inhibits JAK activity
  * **SOCS5** - specific STAT6 inhibitor
  * **SHP-1** - dephosphorylates STAT6
  * **PIAS proteins** - block DNA binding

## Clinical Significance

* **STAT6 and allergic diseases:**
  * Central to pathogenesis of asthma, atopic dermatitis, allergic rhinitis
  * Polymorphisms associated with IgE levels and atopy
  * rs324011 variant increases allergic disease risk
  * Target for anti-allergic therapies

* **STAT6 in cancer:**
  * Activated in Hodgkin lymphoma
  * Follicular lymphoma (subset)
  * Promotes tumor-associated macrophage polarization
  * May suppress anti-tumor immunity

* **Therapeutic targeting:**
  * **Dupilumab** - IL-4Rα antibody blocks STAT6 activation
  * **JAK inhibitors** - reduce STAT6 phosphorylation
  * STAT6 inhibitors in development for allergy/asthma

* **Parasitic immunity:**
  * Essential for helminth expulsion
  * Coordinates type 2 immunity against worms
  * Trade-off between allergy and parasite resistance

## Phenotypes

* **STAT6 deficiency (mouse):**
  * **Immune:** Absent Th2 responses, no IgE production
  * **Infection:** Susceptible to Nippostrongylus, Schistosoma
  * **Protection:** Resistant to allergic airway inflammation
  * **Macrophages:** Defective M2 polarization
  * **Wound healing:** Impaired tissue repair

* **Human STAT6 variants:**
  * **Loss-of-function:** Rare, associated with:
    - Reduced IgE levels
    - Protection from atopy
    - Increased helminth susceptibility
  * **Gain-of-function variants:**
    - Elevated IgE
    - Atopic diseases
    - Asthma severity

* **Cellular phenotypes:**
  * Failed Th2 differentiation
  * Absent IgE class switching
  * Defective eosinophil recruitment
  * Impaired mast cell activation
  * Reduced mucus production