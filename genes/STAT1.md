---
id: UniProtKB:P42224
symbol: STAT1
primary_functions:
- description: STAT1 is translocated to the nucleus where it transduces signals from
    cytokine and growth factor receptors by binding to specific DNA sequences and
    activating transcription of target genes
  activity:
    term:
      id: GO:0003700
      label: DNA-binding transcription factor activity
    support: []
  location:
    term:
      id: GO:0005634
      label: nucleus
    support:
    - reference: GO_REF:0000033
      title: Annotation inferences using phylogenetic trees
      evidence_type: IBA
    notes: STAT1 is shuttled between cytoplasm and nucleus, but has primary function
      in nucleus
  upstream:
  - term:
      id: GO:0042976
      label: activation of Janus kinase activity
    description: JAK1 and JAK2 phosphorylate STAT1 at Tyr701 following cytokine receptor
      engagement
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: STAT1 activates transcription of interferon-stimulated genes (ISGs)
      by binding to GAS or ISRE elements
  processes:
  - term:
      id: GO:0007259
      name: cell surface receptor signaling pathway via JAK-STAT
    support:
    - reference: GO_REF:0000033
      title: Annotation inferences using phylogenetic trees
      evidence_type: IBA
  - term:
      id: GO:0019221
      name: cytokine-mediated signaling pathway
    is_any_of:
    - term:
        id: GO:0060337
        name: type I interferon-mediated signaling pathway
      support:
      - reference: GO_REF:0000024
        title: Manual transfer of experimentally-verified manual GO annotation data
          to orthologs by curator judgment of sequence similarity
        evidence_type: ISS
    - term:
        id: GO:0060333
        name: type II interferon-mediated signaling pathway
      support: []
  roles:
  - term:
      id: GO:0001937
      label: negative regulation of endothelial cell proliferation
    category: over-annotation
    notes: one of the many downstream effects of JAK-STAT pathway
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: increased susceptibility to viral and mycobacterial infections
    mechanism: impaired interferon signaling leads to defective innate and adaptive
      immunity against intracellular pathogens
    term:
      id: HP:0002719
      label: Recurrent infections
    support:
    - reference: PMID:34183371
      title: Genetic, Immunological, and Clinical Features of 32 Patients with Autosomal
        Recessive STAT1 Deficiency
      supporting_text: Fifty-four severe viral episodes occurred in sixteen patients,
        mainly caused by Herpesviridae viruses. Twenty-four patients suffered from
        mycobacterial disease
      evidence_type: TAS
  - description: Mendelian susceptibility to mycobacterial diseases
    mechanism: partial defect in the interferon-gamma pathway leading to selective
      vulnerability to mycobacterial infections
    term:
      id: MONDO:0013956
      label: Mendelian susceptibility to mycobacterial diseases due to partial STAT1
        deficiency
    support:
    - reference: PMID:28521627
      title: Disseminated Bacillus Calmette-Guérin Osteomyelitis in Twin Sisters Related
        to STAT1 Gene Deficiency
      supporting_text: Twin sisters with disseminated BCG osteomyelitis due to compound
        heterozygous STAT1 mutations
      evidence_type: IMP
- mutation:
    type: gain_of_function
  effects:
  - description: chronic mucocutaneous candidiasis - recurrent or persistent superficial
      Candida infections
    term:
      id: HP:0002728
      label: Chronic mucocutaneous candidiasis
    support:
    - reference: PMID:29702748
      title: Chronic mucocutaneous candidiasis due to gain-of-function mutation in
        STAT1
      supporting_text: STAT1 gain-of-function mutations are the most common genetic
        cause of chronic mucocutaneous candidiasis
      evidence_type: TAS
  - description: STAT1 gain-of-function immunodeficiency
    mechanism: enhanced STAT1 phosphorylation and prolonged activation leading to
      excessive IFN responses and impaired IL-17 immunity
    term:
      id: MONDO:0013427
      label: immunodeficiency 31B
    support:
    - reference: PMID:32852681
      title: 'Human STAT1 Gain-of-Function Heterozygous Mutations: Chronic Mucocutaneous
        Candidiasis and Type I Interferonopathy'
      supporting_text: STAT1 GOF mutations lead to impaired dephosphorylation, prolonged
        nuclear retention, and excessive type I interferon signaling
      evidence_type: IMP
  - description: autoimmune manifestations including thyroiditis, hepatitis, and diabetes
    term:
      id: HP:0002960
      label: Autoimmunity
    support:
    - reference: PMID:26981552
      title: Clinical and immunological data of nine patients with chronic mucocutaneous
        candidiasis disease
      supporting_text: Patients developed autoimmune disorders including vitiligo,
        thyroid disease, type I diabetes, and autoimmune hepatitis
      evidence_type: TAS
  - description: chronic inflammation of the thyroid gland, often autoimmune
    term:
      id: HP:0100646
      label: Thyroiditis
    support:
    - reference: PMID:22847544
      title: Autosomal-dominant chronic mucocutaneous candidiasis with STAT1-mutation
        can be complicated with chronic active hepatitis and hypothyroidism
      supporting_text: STAT1 gain-of-function mutations can lead to hypothyroidism
        and autoimmune thyroid disease
      evidence_type: TAS
  - description: inflammatory liver disease with autoimmune features
    term:
      id: HP:0200123
      label: Chronic hepatitis
    support:
    - reference: PMID:22847544
      title: Autosomal-dominant chronic mucocutaneous candidiasis with STAT1-mutation
        can be complicated with chronic active hepatitis and hypothyroidism
      supporting_text: Chronic active hepatitis is a rare but serious complication
        of autosomal dominant chronic mucocutaneous candidiasis
      evidence_type: TAS
---
**STAT1 (Signal Transducer and Activator of Transcription 1)** is a transcription factor that plays a central role in mediating responses to cytokines and growth factors, particularly **interferons (IFNs)**.

## Function

* **Cytokine signaling mediator:** Activated mainly by type I IFNs (IFN-α, IFN-β) and type II IFN (IFN-γ), as well as some interleukins (e.g., IL-27) and growth factors.
* **Activation mechanism:** Upon cytokine binding to its receptor, associated Janus kinases (**JAKs**) phosphorylate STAT1 at Tyr701, leading to dimerization (STAT1–STAT1 homodimers or STAT1–STAT2 heterodimers) and nuclear translocation.
* **Transcriptional regulation:** In the nucleus, STAT1 binds specific DNA sequences (GAS or ISRE elements) to regulate genes involved in:

  * **Antiviral defense** (e.g., upregulation of ISGs — interferon-stimulated genes)
  * **Antimicrobial immunity**
  * **Cell growth inhibition**
  * **Pro-apoptotic pathways** in infected or damaged cells
* **Immune system role:** Essential for Th1-type immune responses, macrophage activation, and host defense against intracellular pathogens.
* **Regulation:** Activity is tightly controlled by phosphatases (e.g., TC45), SOCS proteins, and proteasomal degradation to prevent excessive inflammation.

## Phenotypes

* **Loss-of-function mutations** → increased susceptibility to viral and mycobacterial infections.
* **Gain-of-function mutations** → chronic mucocutaneous candidiasis, autoimmune disorders due to excessive IFN signaling.


