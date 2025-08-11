---
id: UniProtKB:P52630
symbol: STAT2
primary_functions:
- description: STAT2 is an essential and specific mediator of type I interferon signaling
    that forms the ISGF3 complex with STAT1 and IRF9, binding to ISRE elements to
    activate antiviral gene expression
  activity:
    term:
      id: GO:0000981
      label: DNA-binding transcription factor activity, RNA polymerase II-specific
    support: []
    notes: STAT2 binds DNA exclusively as part of ISGF3 complex, not as homodimers
  location:
    term:
      id: GO:0005634
      label: nucleus
    notes: Translocates to nucleus as part of ISGF3 complex
  complex:
    term:
      id: GO:0070721
      label: ISGF3 complex
    support: []
    notes: Forms trimeric complex with STAT1 and IRF9
  upstream:
  - term:
      id: GO:0042976
      label: activation of Janus kinase activity
    description: TYK2 and JAK1 phosphorylate STAT2 at Tyr690 following type I IFN
      receptor engagement
  downstream:
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support:
    - reference: PMID:24058793
      title: 'STAT heterodimers in immunity: A mixed message or a unique signal?'
      evidence_type: NAS
    description: ISGF3 complex activates transcription of interferon-stimulated genes
      (ISGs) by binding to ISRE elements
  processes:
  - term:
      id: GO:0071357
      name: cellular response to type I interferon
    support: []
  - term:
      id: GO:0035455
      name: response to interferon-alpha
    support: []
  - term:
      id: GO:0035456
      name: response to interferon-beta
    support: []
  - term:
      id: GO:0140374
      name: antiviral innate immune response
    support: []
  roles:
  - term:
      id: GO:0046982
      label: protein heterodimerization activity
    notes: Forms obligate heterodimers with STAT1; cannot form homodimers unlike other
      STATs
  - term:
      id: GO:0005126
      label: cytokine receptor binding
    notes: Recruits USP18 to IFNAR2 for negative feedback regulation
phenotypes:
- mutation:
    type: loss_of_function
  effects:
  - description: severe viral infections including disseminated vaccine-strain measles
    mechanism: impaired type I interferon signaling leads to defective antiviral immunity
    term:
      id: HP:0002719
      label: Recurrent infections
    support:
    - reference: PMID:36976641
      title: Human inherited complete STAT2 deficiency underlies inflammatory viral
        diseases
      supporting_text: Clinical manifestations included severe adverse reactions to
        live attenuated viral vaccines and severe viral infections
      evidence_type: TAS
  - description: primary immunodeficiency with post-measles-mumps-rubella vaccine
      viral infection
    mechanism: selective susceptibility to viral infections particularly after systemic
      challenge with live viral vaccines
    term:
      id: MONDO:0014715
      label: primary immunodeficiency with post-measles-mumps-rubella vaccine viral
        infection
    support:
    - reference: PMID:36976641
      title: Human inherited complete STAT2 deficiency underlies inflammatory viral
        diseases
      supporting_text: Disseminated infection after live attenuated vaccine inoculation
        occurred in 70% of patients receiving any vaccine, especially measles vaccine
      evidence_type: TAS
  - description: increased susceptibility to viral but NOT mycobacterial infections
    mechanism: STAT2 is specific to type I IFN pathway; does not affect IFN-γ signaling
      required for mycobacterial defense
    term:
      id: HP:0002721
      label: Immunodeficiency
    support:
    - reference: PMID:34448086
      title: 'Human Disease Phenotypes Associated with Loss and Gain of Function Mutations
        in STAT2: Viral Susceptibility and Type I Interferonopathy'
      supporting_text: Autosomal recessive STAT2 deficiency results in heightened
        susceptibility to severe and/or recurrent viral disease without other immunodeficiency
        evidence
      evidence_type: TAS
  - description: fatal febrile illness from viral infections
    mechanism: inability to mount effective antiviral response through ISG expression
    term:
      id: HP:0001945
      label: Fever
    support: []
- mutation:
    type: gain_of_function
  effects:
  - description: no known gain-of-function mutations reported
    notes: Unlike STAT1, no pathogenic GOF variants identified in STAT2
---
**STAT2 (Signal Transducer and Activator of Transcription 2)** is an essential and specific mediator of **type I interferon (IFN-α/β)** and **type III interferon (IFN-λ)** signaling that plays a critical role in antiviral immunity.

## Function

* **Type I IFN-specific signaling:** Exclusively activated by type I IFNs (IFN-α, IFN-β) and type III IFNs (IFN-λ), but **NOT by type II IFN (IFN-γ)**, distinguishing it from STAT1.
* **ISGF3 complex formation:** Following phosphorylation at Tyr690 by TYK2 and JAK1, STAT2 forms obligate heterodimers with STAT1 (cannot form homodimers), which then associate with **IRF9** to form the trimeric **ISGF3 (IFN-stimulated gene factor 3)** complex.
* **DNA binding specificity:** The ISGF3 complex binds to **ISRE (IFN-stimulated response elements)** with the consensus sequence 5'-G/ANGAAAN2GAAACT-3', distinct from the GAS elements recognized by STAT1 homodimers.
* **Antiviral gene activation:** Drives expression of hundreds of **interferon-stimulated genes (ISGs)** that establish an antiviral state, including:
  * **2'-5' oligoadenylate synthetases (OAS)** for RNA degradation
  * **Mx proteins** for viral replication inhibition  
  * **PKR (protein kinase R)** for translation inhibition
  * **ISG15** for protein modification and antiviral defense

## Unique Features vs Other STATs

* **No homodimerization capability:** Unlike STAT1, STAT3, and other family members, STAT2 cannot form functional homodimers and requires STAT1 for dimerization.
* **Type I IFN exclusivity:** Does not participate in IFN-γ signaling pathways, making it a specific marker of type I IFN response.
* **Dual regulatory role:** Besides signal transduction, STAT2 uniquely recruits **USP18** to the type I IFN receptor (IFNAR2) to mediate negative feedback, particularly dampening IFN-α responses.
* **DNA binding dependency:** Cannot bind DNA independently; requires both STAT1 and IRF9 partners in the ISGF3 complex.
* **No gain-of-function mutations:** Unlike STAT1 and STAT3, no pathogenic GOF variants have been identified in STAT2.

## Regulation

* **USP18-mediated negative feedback:** STAT2 directly interacts with USP18 and recruits it to IFNAR2, where USP18 interferes with JAK1 binding and receptor dimerization, creating a negative feedback loop specific to type I IFN.
* **Differential IFN subtype regulation:** The STAT2-USP18 interaction preferentially attenuates IFN-α signaling over IFN-β due to differences in receptor binding affinity.
* **Unphosphorylated functions:** Recent evidence suggests STAT2-IRF9 complexes can regulate basal ISG expression even without phosphorylation.

## Phenotypes

* **Loss-of-function mutations (Immunodeficiency 44):**
  * Severe susceptibility to viral infections (measles, influenza, HSV, etc.)
  * Complications from live attenuated viral vaccines
  * **Notably NO increased susceptibility to mycobacterial infections** (unlike STAT1 deficiency)
  * Generally normal adaptive immunity between infections
  * Fatal outcomes possible from otherwise mild viral infections

* **No known gain-of-function phenotype:** Unlike STAT1 GOF causing chronic mucocutaneous candidiasis and autoimmunity, no STAT2 GOF syndrome has been identified.

## Clinical Significance

STAT2 deficiency represents a selective vulnerability to viral pathogens while maintaining normal antibacterial and antifungal immunity, highlighting the specialized role of type I interferon signaling in antiviral defense. This makes STAT2 a potential therapeutic target for enhancing antiviral immunity or modulating inflammatory responses in viral infections and interferonopathies.