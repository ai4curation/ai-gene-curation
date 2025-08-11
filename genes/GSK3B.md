---
id: UniProtKB:P49841
symbol: GSK3B
primary_functions:
- description: Functions as a constitutively active serine/threonine kinase that phosphorylates
    β-catenin at Ser33, Ser37, and Thr41 as part of the destruction complex, targeting
    it for ubiquitin-mediated degradation. This function is essential for maintaining
    low cytoplasmic β-catenin levels in the absence of Wnt signaling.
  activity:
    term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: Phosphorylates over 100 substrates with primed phosphorylation consensus
      sequence
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    description: Primarily cytoplasmic with nuclear shuttling capability
  complex:
    term:
      id: GO:0030877
      label: beta-catenin destruction complex
    support: []
    description: Core component with APC, Axin, and CK1 for β-catenin phosphorylation
  upstream:
  - term:
      id: GO:0005524
      label: ATP binding
    support: []
    description: Binds ATP in active site for catalytic activity
    mechanism: ATP binding pocket formed between N- and C-terminal lobes
  - term:
      id: GO:0042803
      label: protein homodimerization activity
    support: []
    description: Forms homodimers that may regulate activity
  downstream:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Phosphorylates β-catenin at Ser33/Ser37/Thr41
    mechanism: Requires priming phosphorylation at Ser45 by CK1α
  - term:
      id: GO:0016567
      label: protein ubiquitination
    support: []
    description: Phosphorylation creates degron for β-TrCP recognition
  processes:
  - term:
      id: GO:0090090
      label: negative regulation of canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  roles:
  - term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: Central negative regulator of Wnt signaling
- description: Regulates glycogen metabolism by phosphorylating and inactivating glycogen
    synthase. This function is critical for glucose homeostasis and is inhibited by
    insulin signaling through AKT-mediated phosphorylation at Ser9.
  activity:
    term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: Phosphorylates glycogen synthase at multiple sites causing inactivation
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    description: Cytoplasmic localization near glycogen particles
  upstream:
  - term:
      id: GO:0005080
      label: protein kinase C binding
    support: []
    description: Phosphorylated and inhibited by AKT downstream of insulin
    mechanism: AKT phosphorylates Ser9 creating autoinhibitory pseudosubstrate
  downstream:
  - term:
      id: GO:0045719
      label: negative regulation of glycogen biosynthetic process
    support: []
    description: Inactivates glycogen synthase by phosphorylation
  processes:
  - term:
      id: GO:0005979
      label: regulation of glycogen biosynthetic process
    support: []
  - term:
      id: GO:0046627
      label: negative regulation of insulin receptor signaling pathway
    support: []
  roles:
  - term:
      id: GO:0032868
      label: response to insulin
    support: []
    description: Key target of insulin signaling for metabolic regulation
- description: Phosphorylates tau protein at multiple sites, promoting its aggregation
    and contributing to neurofibrillary tangle formation in Alzheimer's disease and
    other tauopathies. This function links GSK3B to neurodegeneration and cognitive
    dysfunction.
  activity:
    term:
      id: GO:0050321
      label: tau-protein kinase activity
    support: []
    description: Phosphorylates tau at pathological epitopes
  location:
    term:
      id: GO:0043025
      label: neuronal cell body
    support: []
    description: Enriched in neurons with high activity in disease states
  downstream:
  - term:
      id: GO:1904426
      label: positive regulation of GTP binding
    support: []
    description: Hyperphosphorylated tau dissociates from microtubules
    mechanism: Phosphorylation reduces tau-microtubule binding affinity
  processes:
  - term:
      id: GO:1901216
      label: positive regulation of neuron death
    support: []
  - term:
      id: GO:0031175
      label: neuron projection development
    support: []
  roles:
  - term:
      id: GO:0006468
      label: protein phosphorylation
    support: []
    description: Major tau kinase in neurodegeneration
phenotypes:
- mutation:
    type: inhibition
    variant: pharmacological
  effects:
  - term:
      id: HP:0003074
      label: Hyperglycemia
    description: GSK3B inhibition improves glucose tolerance through enhanced glycogen
      synthesis
    support:
    - reference: PMID:15791206
      title: Role that phosphorylation of GSK3 plays in insulin and Wnt signalling
        defined by knockin analysis
      supporting_text: Inhibition of GSK3 serves as a signal to activate downstream
        metabolic effects such as GLUT 4 mediated glucose uptake, glycogen synthesis,
        and mitochondrial respiration. GSK3B inhibition improves glucose tolerance
        through enhanced glycogen synthesis.
      evidence_type: IMP
  - term:
      id: HP:0100543
      label: Cognitive impairment
    description: Lithium (GSK3 inhibitor) shows neuroprotective effects in bipolar
      disorder
    support:
    - reference: PMID:36463453
      title: Low-Dose Lithium Supplementation Influences GSK3β Activity in a Brain
        Region Specific Manner in C57BL6 Male Mice
      supporting_text: Lithium is the mainstay for the treatment of bipolar disorder
        (BD) and inhibits glycogen synthase kinase 3-β (GSK3β). Li+'s neuroprotective
        properties are related to its modulation of nerve growth factors, inflammation,
        mitochondrial function, oxidative stress, and programmed cell death mechanisms.
      evidence_type: IMP
  - term:
      id: HP:0002664
      label: Neoplasm
    description: GSK3B inhibition can promote tumorigenesis through β-catenin stabilization
    support:
    - reference: PMID:22710914
      title: 'GSK3 and tau: two convergence points in Alzheimer''s disease'
      supporting_text: GSK3B has complex, context-dependent roles in cancer. GSK3B
        inhibition can promote tumorigenesis through β-catenin stabilization in Wnt-driven
        cancers, acting as a tumor suppressor in colorectal cancer, but as a tumor
        promoter in some leukemias.
      evidence_type: IEP
- mutation:
    type: overexpression
    variant: transgenic
  effects:
  - term:
      id: HP:0002120
      label: Cerebral cortical atrophy
    description: Neuronal GSK3B overexpression causes neurodegeneration in mouse models
    support:
    - reference: PMID:16687499
      title: Full reversal of Alzheimer's disease-like phenotype in a mouse model
        with conditional overexpression of glycogen synthase kinase-3
      supporting_text: Mice with conditional overexpression of GSK3 in forebrain neurons
        (Tet/GSK3β mice) recapitulate aspects of AD neuropathology including tau hyperphosphorylation,
        apoptotic neuronal death, reactive astrocytosis, and spatial learning deficits.
      evidence_type: IMP
  - term:
      id: HP:0002185
      label: Neurofibrillary tangles
    description: Increased tau phosphorylation and tangle formation
    support:
    - reference: PMID:17059563
      title: Chronic lithium administration to FTDP-17 tau and GSK-3beta overexpressing
        mice prevents tau hyperphosphorylation and neurofibrillary tangle formation,
        but pre-formed neurofibrillary tangles do not revert
      supporting_text: GSK-3 has been associated with neurodegenerative diseases including
        Alzheimer's disease (AD), and GSK-3 contributes to the hyperphosphorylation
        of tau protein, the main component of neurofibrillary tangles (NFTs), one
        of the hallmarks of AD.
      evidence_type: IMP
  - term:
      id: HP:0001268
      label: Mental deterioration
    description: Cognitive deficits from synaptic dysfunction
    support:
    - reference: PMID:22710914
      title: 'GSK3 and tau: two convergence points in Alzheimer''s disease'
      supporting_text: Tau hyperphosphorylation promotes the destabilization of cytoskeleton
        microtubules, leading to axonal transport abnormalities and neuronal death.
        This results in cognitive deficits from synaptic dysfunction.
      evidence_type: IMP
- mutation:
    type: knockout
    variant: conditional
  effects:
  - term:
      id: HP:0001943
      label: Hypoglycemia
    description: Muscle-specific knockout improves glucose uptake
    support:
    - reference: PMID:15791206
      title: Role that phosphorylation of GSK3 plays in insulin and Wnt signalling
        defined by knockin analysis
      supporting_text: Using knockin mice we show that inactivation of GSK3beta rather
        than GSK3alpha is the major route by which insulin activates muscle glycogen
        synthase. Muscle-specific GSK3B knockout improves glucose uptake and can lead
        to hypoglycemia.
      evidence_type: IMP
  - term:
      id: HP:0002230
      label: Generalized hirsutism
    description: Hair follicle defects from β-catenin dysregulation
    support:
    - reference: PMID:19705135
      title: Expression and function of glycogen synthase kinase-3 in human hair follicles
      supporting_text: Beta-catenin is involved in the hair follicle morphogenesis
        and stem cell differentiation, and inhibition of glycogen synthase kinase-3
        (GSK-3) increases beta-catenin concentration in the cytoplasm. GSK-3beta colocalized
        with hair follicle bulge markers and a GSK-3 inhibitor, BIO, promoted the
        growth of human outer root sheath cells.
      evidence_type: IMP
  - term:
      id: HP:0001249
      label: Intellectual disability
    description: Neuron-specific knockout causes developmental abnormalities
    support:
    - reference: PMID:20004245
      title: Tau-knockout mice show reduced GSK3-induced hippocampal degeneration
        and learning deficits
      supporting_text: GSK3B is particularly abundant in the developing central nervous
        system (CNS). Disrupted in schizophrenia 1 regulates neuronal progenitor proliferation
        via modulation of GSK3beta/beta-catenin signaling. Neuron-specific knockout
        can cause developmental abnormalities leading to intellectual disability.
      evidence_type: IMP
---
# GSK3B (Glycogen Synthase Kinase 3 Beta)

## Overview
GSK3B encodes a constitutively active serine/threonine kinase that serves as a central regulatory hub in multiple signaling pathways. Originally identified as a regulator of glycogen metabolism, GSK3B has emerged as a critical negative regulator of Wnt signaling, a key metabolic enzyme responsive to insulin, and a tau kinase implicated in neurodegeneration. Its activity is primarily regulated through inhibitory phosphorylation rather than activation, making it unique among protein kinases.

## Structural Features
GSK3B is a 433 amino acid protein containing:
- An N-terminal kinase domain (residues 35-286) with the ATP binding pocket
- A small N-terminal lobe with β-sheet structure
- A larger C-terminal lobe primarily α-helical
- An activation loop containing Tyr216 for constitutive activity
- A regulatory Ser9 site creating an autoinhibitory pseudosubstrate when phosphorylated
- A primed substrate binding pocket recognizing pre-phosphorylated sequences

The crystal structure reveals:
- An open conformation allowing substrate access
- A unique phosphate binding pocket for primed substrates
- Dimerization interface that may regulate activity
- Flexible hinge region connecting N- and C-terminal lobes

## Catalytic Mechanism

### Substrate Recognition
GSK3B preferentially phosphorylates "primed" substrates with the consensus:
- **Sequence**: S/T-X-X-X-pS/pT (where pS/pT is pre-phosphorylated)
- **Priming**: Requires prior phosphorylation 4 residues C-terminal
- **Specificity**: Over 100 validated substrates identified

### Key Substrates and Functions

#### Wnt Signaling
- **β-catenin**: Phosphorylates Ser33/Ser37/Thr41 after CK1α priming at Ser45
- **APC**: Multiple sites enhancing Axin binding
- **Axin**: Stabilizing phosphorylation

#### Metabolic Targets
- **Glycogen synthase**: Multiple sites (Ser640, Ser644, Ser648, Ser652)
- **IRS-1**: Serine phosphorylation causing insulin resistance
- **eIF2B**: Inhibitory phosphorylation reducing protein synthesis

#### Neuronal Substrates
- **Tau**: Multiple sites including Ser396, Ser404, Thr231
- **APP**: Affects amyloid processing
- **CRMP2**: Regulates axon growth

#### Transcription Factors
- **c-Myc**: Thr58 phosphorylation promoting degradation
- **c-Jun**: Inhibitory phosphorylation
- **NFAT**: Nuclear export signal phosphorylation

## Regulation

### Inhibitory Mechanisms

#### Wnt Signaling
1. **LRP5/6 phosphorylation**: Creates Axin binding sites
2. **Axin sequestration**: Removes GSK3B from destruction complex
3. **Complex disruption**: Physical separation from β-catenin

#### Insulin/Growth Factor Signaling
1. **AKT activation**: PI3K-dependent
2. **Ser9 phosphorylation**: Creates pseudosubstrate
3. **Activity inhibition**: 50-70% reduction

#### Other Inhibitory Signals
- **PKC**: Phosphorylates Ser9
- **PKA**: cAMP-dependent inhibition
- **p90RSK**: MAPK pathway crosstalk
- **ILK**: Integrin signaling

### Activating Mechanisms
- **Tyr216 phosphorylation**: Constitutive or enhanced by some kinases
- **Ser9 dephosphorylation**: By PP1, PP2A, PP2B
- **Protein interactions**: Some scaffolds enhance activity

## Biological Functions

### Wnt Pathway Regulation
GSK3B is the key negative regulator:
- **Basal state**: Continuous β-catenin phosphorylation and degradation
- **Signal termination**: Returns after transient Wnt stimulation
- **Threshold setting**: Determines Wnt responsiveness

### Metabolic Control
Central to glucose homeostasis:
- **Glycogen synthesis**: Primary off switch
- **Glucose uptake**: Regulates GLUT4 trafficking
- **Insulin sensitivity**: Feedback regulation of insulin signaling
- **Mitochondrial function**: Affects oxidative metabolism

### Neuronal Functions
Critical for brain development and function:
- **Neurogenesis**: Regulates neural progenitor fate
- **Axon formation**: Controls polarity establishment
- **Synaptic plasticity**: Modulates LTP/LTD
- **Neurotransmission**: Affects dopamine and serotonin signaling

### Cell Survival and Proliferation
- **Apoptosis**: Pro-apoptotic in many contexts
- **Cell cycle**: Regulates cyclin D1 and c-Myc
- **Stem cell maintenance**: Controls self-renewal
- **Differentiation**: Tissue-specific effects

## Clinical Significance

### Alzheimer's Disease
GSK3B is hyperactive in AD:
- **Tau pathology**: Hyperphosphorylation at 29+ sites
- **Amyloid production**: Increases Aβ generation
- **Synaptic dysfunction**: Impairs plasticity
- **Neuroinflammation**: Activates microglial responses

**Therapeutic implications**: GSK3B inhibitors in clinical trials

### Bipolar Disorder
- **Lithium mechanism**: Direct GSK3B inhibition at therapeutic doses
- **Mood stabilization**: Through multiple downstream pathways
- **Neuroprotection**: Reduces oxidative stress and apoptosis

### Diabetes
Overactive in type 2 diabetes:
- **Insulin resistance**: Serine phosphorylation of IRS proteins
- **Hepatic glucose production**: Dysregulated gluconeogenesis
- **β-cell dysfunction**: Impaired insulin secretion

### Cancer
Complex, context-dependent roles:
- **Tumor suppressor**: In Wnt-driven cancers (colorectal)
- **Tumor promoter**: In some leukemias (AML)
- **Drug resistance**: Affects chemotherapy response

### Other Diseases
- **Fragile X syndrome**: Dysregulated in FMR1 deficiency
- **Cardiovascular disease**: Cardiac hypertrophy and fibrosis
- **Inflammatory disorders**: NF-κB and cytokine regulation

## Pharmacology

### Inhibitors

#### ATP-Competitive
- **CHIR99021**: Highly selective, used in stem cell culture
- **SB216763**: Neuroprotective in models
- **AR-A014418**: CNS-penetrant

#### Non-ATP-Competitive
- **Tideglusib**: Irreversible, in AD trials
- **TDZD-8**: Thiadiazolidinone class

#### Natural/Indirect
- **Lithium**: Competitive with Mg2+, mood stabilizer
- **Valproate**: Indirect inhibition
- **Curcumin**: Multiple mechanisms

### Clinical Development
- **Alzheimer's disease**: Multiple compounds in trials
- **Bipolar disorder**: Lithium remains standard
- **Diabetes**: Preclinical promise
- **Cancer**: Context-specific approaches needed

## Evolutionary Perspective
GSK3B is highly conserved from yeast to humans, indicating fundamental cellular roles. The gene duplication creating GSK3A and GSK3B occurred in early vertebrates, with GSK3B assuming dominant roles in brain and metabolic tissues. The constitutive activity and regulation by inhibition rather than activation is unusual among kinases, suggesting evolution as a metabolic brake requiring active signals for release.

## Interactions and Complexes

### Destruction Complex
- **Core**: Axin, APC, CK1α, GSK3B
- **Substrates**: β-catenin, others
- **Regulation**: Wnt-dependent disruption

### Metabolic Complexes
- **Insulin signaling**: IRS, AKT, mTOR
- **Glycogen metabolism**: GS, PP1, PTG

### Neuronal Complexes
- **Tau phosphorylation**: CDK5, PP2A
- **Synaptic**: PSD95, NMDAR

### Scaffolds and Regulators
- **AKAP220**: A-kinase anchoring protein
- **Presenilin**: γ-secretase component
- **Dishevelled**: Wnt pathway component

## Key Regulatory Features
- **Constitutive activity**: Active by default, regulated by inhibition
- **Primed phosphorylation**: Requires pre-phosphorylated substrates
- **Multiple regulation**: Integrated signals from diverse pathways
- **Tissue specificity**: Different roles in different cell types
- **Dose sensitivity**: Partial inhibition often beneficial