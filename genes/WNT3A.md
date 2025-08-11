---
id: UniProtKB:P56704
symbol: WNT3A
primary_functions:
- description: Functions as a secreted signaling protein that activates the canonical
    Wnt/β-catenin signaling pathway by binding to Frizzled receptors and LRP5/6 co-receptors.
    This function is essential for embryonic development, stem cell maintenance, and
    tissue homeostasis.
  activity:
    term:
      id: GO:0005102
      label: signaling receptor binding
    support: []
    description: Binds to Frizzled family receptors and LRP5/6 co-receptors to form
      active signaling complex
  location:
    term:
      id: GO:0005576
      label: extracellular region
    support: []
    description: Secreted as a lipid-modified morphogen that acts in autocrine and
      paracrine manner
  complex:
    term:
      id: GO:1990851
      label: Wnt signalosome
    support: []
    description: Forms ternary complex with Frizzled and LRP5/6 receptors
  upstream:
  - term:
      id: GO:0016055
      label: Wnt signaling pathway
    support: []
    description: Initiates signaling by binding to receptor complex
  - term:
      id: GO:0018359
      label: protein O-linked glycosylation via serine
    support: []
    description: Palmitoylation by Porcupine is required for secretion and activity
    mechanism: Palmitoleic acid modification at S209 essential for receptor binding
  downstream:
  - term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Stabilizes β-catenin by inhibiting destruction complex
  - term:
      id: GO:0045893
      label: positive regulation of DNA-templated transcription
    support: []
    description: Activates TCF/LEF-dependent transcription of target genes
  processes:
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0045165
      label: cell fate commitment
    support: []
  - term:
      id: GO:0008283
      label: cell population proliferation
    support: []
  roles:
  - term:
      id: GO:0048018
      label: receptor ligand activity
    support: []
    description: Primary ligand for canonical Wnt signaling
- description: Regulates stem cell self-renewal and maintenance in various tissue
    compartments including intestinal crypts, hair follicles, and hematopoietic system.
    This function is critical for tissue regeneration and homeostasis.
  activity:
    term:
      id: GO:0008083
      label: growth factor activity
    support: []
    description: Acts as a stem cell growth factor maintaining stemness
  location:
    term:
      id: GO:0055037
      label: recycling endosome
    support: []
    description: Can be packaged in exosomes for long-range signaling
  processes:
  - term:
      id: GO:0098727
      label: maintenance of cell number
    support: []
  - term:
      id: GO:0019827
      label: stem cell population maintenance
    support: []
  - term:
      id: GO:0060349
      label: bone morphogenesis
    support: []
  roles:
  - term:
      id: GO:0048018
      label: receptor ligand activity
    support: []
    description: Induces transcriptional programs for stem cell maintenance through
      receptor activation
- description: Promotes osteoblast differentiation and bone formation through activation
    of osteogenic transcription factors. Essential for skeletal development and bone
    homeostasis.
  activity:
    term:
      id: GO:0045669
      label: positive regulation of osteoblast differentiation
    support: []
    description: Stimulates osteoblast differentiation from mesenchymal progenitors
  processes:
  - term:
      id: GO:0001649
      label: osteoblast differentiation
    support: []
  - term:
      id: GO:0045778
      label: positive regulation of ossification
    support: []
- description: Controls dorsal-ventral patterning in the developing neural tube and
    promotes neural crest formation. Critical for proper nervous system development.
  activity:
    term:
      id: GO:0021915
      label: neural tube development
    support: []
    description: Essential for dorsal neural tube specification and neural crest formation
  processes:
  - term:
      id: GO:0014033
      label: neural crest cell differentiation
    support: []
  - term:
      id: GO:0021915
      label: neural tube development
    support: []
phenotypes:
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0000924
      label: Abnormality of the skeletal system
    description: Reduced bone mass and skeletal abnormalities due to impaired osteoblast
      differentiation
    mechanism: Loss of canonical Wnt signaling in osteoblast progenitors
  - term:
      id: HP:0002084
      label: Encephalopathy
    description: Severe brain malformations including absent hippocampus and dentate
      gyrus
    mechanism: Defective dorsal neural tube patterning during development
  - term:
      id: HP:0001392
      label: Abnormality of the liver
    description: Impaired liver regeneration capacity
    mechanism: Reduced hepatic progenitor cell proliferation
  - term:
      id: HP:0002664
      label: Neoplasm
    description: Reduced tumor formation in mouse models of intestinal cancer
    mechanism: Decreased intestinal stem cell proliferation
  - term:
      id: MONDO:0019391
      label: Tetra-amelia syndrome
    description: Complete absence of all four limbs when combined with other Wnt pathway
      mutations
    mechanism: Failure of limb bud initiation and outgrowth
- mutation:
    type: gain_of_function
    variant: somatic
  effects:
  - term:
      id: HP:0100013
      label: Neoplasm of the breast
    description: WNT3A overexpression in breast cancer promotes metastasis and therapy
      resistance
    mechanism: Constitutive β-catenin activation drives epithelial-mesenchymal transition
  - term:
      id: HP:0012125
      label: Prostate cancer
    description: Elevated WNT3A associated with prostate cancer progression and bone
      metastasis
    mechanism: Paracrine signaling promotes cancer stem cell self-renewal
  - term:
      id: MONDO:0005575
      label: Colorectal cancer
    description: Aberrant WNT3A expression in colorectal tumors with intact APC
    mechanism: Ligand-driven activation of Wnt signaling independent of APC mutations
  - term:
      id: HP:0002669
      label: Osteosarcoma
    description: WNT3A overexpression promotes osteosarcoma growth and metastasis
    mechanism: Autocrine Wnt signaling maintains cancer stem cells
- mutation:
    type: polymorphism
    variant: regulatory
  effects:
  - term:
      id: HP:0000939
      label: Osteoporosis
    description: WNT3A promoter polymorphisms associated with reduced bone mineral
      density
    mechanism: Decreased WNT3A expression leads to impaired osteoblast function
  - term:
      id: MONDO:0005148
      label: Type 2 diabetes mellitus
    description: Variants affecting WNT3A expression linked to insulin resistance
    mechanism: Altered adipocyte differentiation and glucose metabolism
---
# WNT3A (Wnt Family Member 3A)

## Overview
WNT3A encodes a member of the Wnt family of secreted signaling proteins that function as morphogens regulating cell fate, proliferation, and differentiation. As a prototypical activator of the canonical Wnt/β-catenin pathway, WNT3A plays essential roles in embryonic development, adult stem cell maintenance, and tissue homeostasis. The protein requires lipid modification for its activity and can signal both locally and at a distance through various transport mechanisms.

## Structural Features
WNT3A is a 352 amino acid protein containing:
- A signal peptide for secretion
- 24 conserved cysteine residues forming a characteristic Wnt fold
- A palmitoleic acid modification at Ser209 essential for activity
- Multiple glycosylation sites affecting protein stability and range

The lipid modification by the enzyme Porcupine in the endoplasmic reticulum is absolutely required for WNT3A secretion and biological activity. This hydrophobic modification necessitates specialized secretion machinery (Wntless/Evi) and affects the protein's signaling range.

## Signaling Mechanism
WNT3A activates canonical Wnt signaling through:
1. **Receptor binding**: Forms a ternary complex with Frizzled receptors and LRP5/6 co-receptors
2. **Signal transduction**: Induces LRP5/6 phosphorylation and Dishevelled recruitment
3. **Destruction complex inhibition**: Prevents β-catenin degradation by sequestering Axin
4. **Transcriptional activation**: Stabilized β-catenin activates TCF/LEF target genes

The signaling output is highly context-dependent, influenced by:
- Receptor expression levels and combinations
- Presence of antagonists (DKK, sFRP, WIF)
- Extracellular matrix components that modulate ligand distribution
- Cell type-specific transcriptional cofactors

## Biological Functions

### Embryonic Development
- **Neural development**: Specifies dorsal neural tube and promotes neural crest formation
- **Limb development**: Maintains apical ectodermal ridge and controls digit patterning
- **Body axis formation**: Contributes to anterior-posterior patterning
- **Organogenesis**: Required for kidney, lung, and mammary gland development

### Adult Tissue Homeostasis
- **Intestinal crypts**: Maintains Lgr5+ stem cells essential for epithelial renewal
- **Hair follicles**: Regulates hair follicle stem cells and cycling
- **Hematopoiesis**: Supports hematopoietic stem cell self-renewal
- **Bone**: Promotes osteoblast differentiation and bone formation

## Clinical Significance

### Therapeutic Target
WNT3A represents a promising therapeutic target for:
- **Regenerative medicine**: Enhancing tissue repair and stem cell expansion
  - Ex vivo expansion of hematopoietic stem cells for transplantation
  - Intestinal organoid culture for disease modeling and therapy
  - Neural stem cell activation for neurodegenerative diseases
- **Cancer therapy**: Blocking aberrant Wnt signaling in tumors
  - Small molecule inhibitors targeting WNT3A-receptor interactions
  - Antibodies neutralizing WNT3A in tumor microenvironment
  - Combination therapies with checkpoint inhibitors
- **Bone diseases**: Promoting bone formation in osteoporosis
  - WNT3A mimetics to enhance osteoblast differentiation
  - Gene therapy approaches for severe bone disorders
  - Combination with anti-resorptive agents
- **Neurodegenerative diseases**: Supporting neural stem cells
  - Alzheimer's disease: enhancing neurogenesis in hippocampus
  - Parkinson's disease: promoting dopaminergic neuron survival
  - Spinal cord injury: activating endogenous repair mechanisms

### Disease Associations
- **Cancer**: 
  - Overexpressed in colorectal cancer (30-40% of cases)
  - Triple-negative breast cancer driver in 25% of tumors
  - Prostate cancer bone metastasis promoter
  - Glioblastoma stem cell maintenance factor
- **Bone disorders**: 
  - Osteoporosis risk variants (rs752107, rs3801387)
  - Osteogenesis imperfecta modifier gene
  - Paget's disease of bone susceptibility locus
- **Metabolic disease**: 
  - Type 2 diabetes association through adipocyte dysfunction
  - Non-alcoholic fatty liver disease progression
  - Metabolic syndrome via altered lipid metabolism
- **Aging**: 
  - Decreased expression in aged stem cell niches
  - Contributor to immunosenescence
  - Sarcopenia through satellite cell exhaustion
- **Developmental disorders**:
  - Tetra-amelia syndrome (in combination with other mutations)
  - Neural tube defects (rare variants)
  - Craniofacial abnormalities (regulatory variants)

## Evolutionary Perspective
WNT3A is highly conserved across vertebrates, reflecting its fundamental role in body plan organization and stem cell biology. The canonical Wnt pathway it activates represents one of the oldest metazoan signaling systems, with homologs present in cnidarians and sponges. The evolution of lipid modification and specialized transport mechanisms highlights the importance of controlled morphogen distribution in complex multicellular organisms.

## Regulation
WNT3A expression and activity are regulated at multiple levels:
1. **Transcriptional**: 
   - Induced by Wnt signaling itself (positive feedback loop)
   - Activated by BMP signaling during development
   - Suppressed by p53 in response to DNA damage
   - Enhanced by hypoxia through HIF-1α
2. **Post-translational**: 
   - Palmitoleic acid modification at Ser209 by Porcupine (essential)
   - N-glycosylation affecting stability and secretion
   - Cleavage by TIKI proteases (negative regulation)
3. **Secretion**: 
   - Requires Wntless/Evi for ER to Golgi transport
   - Retromer complex mediates Wntless recycling
   - Can be packaged into exosomes for long-range signaling
4. **Extracellular**: 
   - Sequestered by heparan sulfate proteoglycans
   - Antagonized by secreted Frizzled-related proteins (sFRPs)
   - Blocked by Dickkopf proteins (DKK1/2) at LRP level
   - Stabilized by R-spondins through LGR4/5/6 receptors
5. **Transport**: 
   - Diffusion limited by lipid modification
   - Cytonemes enable directed long-range transport
   - Exosomes protect from degradation
   - Lipoprotein particles facilitate systemic distribution

## Key Interactions
- **Receptors**: 
  - Primary: FZD1-10 (Frizzled family receptors)
  - Co-receptors: LRP5/6 (essential for canonical signaling)
  - Alternative: ROR1/2, RYK (non-canonical pathways)
- **Antagonists**: 
  - DKK1/2 (LRP5/6 inhibitors)
  - sFRP1-5 (competitive Wnt binding)
  - WIF1 (Wnt inhibitory factor)
  - Cerberus, Sclerostin (context-specific)
- **Enhancers**:
  - R-spondins (RSPO1-4) via LGR4/5/6
  - Norrin (retinal-specific Wnt mimetic)
  - SOST (paradoxical enhancer in some contexts)
- **Transport machinery**: 
  - Wntless/Evi (ER to plasma membrane)
  - Retromer complex (VPS35/26/29)
  - SWIM/Secreted Wnt-interacting molecule
- **Downstream effectors**:
  - β-catenin (primary mediator)
  - TCF1/3/4, LEF1 (transcription factors)
  - Dishevelled (DVL1/2/3)
  - Axin1/2, APC, GSK3β (destruction complex)

## Tissue-Specific Functions

### Intestinal Epithelium
- Maintains Lgr5+ crypt base columnar stem cells
- Drives Paneth cell differentiation for stem cell niche
- Controls epithelial renewal every 3-5 days
- Dysregulation leads to colorectal cancer

### Hematopoietic System
- Expands hematopoietic stem cells (HSCs) in bone marrow
- Balances HSC self-renewal vs differentiation
- Regulates T-cell development in thymus
- Modulates B-cell proliferation in germinal centers

### Bone
- Promotes mesenchymal stem cell commitment to osteoblast lineage
- Inhibits osteoclastogenesis indirectly via OPG/RANKL
- Enhances bone formation and mineralization
- Target for anabolic bone therapies

### Neural System
- Specifies dorsal neural tube fate during development
- Maintains adult neural stem cells in hippocampus
- Regulates blood-brain barrier integrity
- Promotes axon guidance and synapse formation

### Skin and Hair Follicles
- Controls hair follicle stem cell activation
- Regulates hair cycle (anagen/catagen/telogen)
- Maintains interfollicular epidermis homeostasis
- Involved in wound healing response