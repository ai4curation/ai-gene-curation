---
id: UniProtKB:O75197
symbol: LRP5
primary_functions:
- description: Functions as an essential co-receptor for canonical Wnt signaling by
    forming a ternary complex with Wnt ligands and Frizzled receptors. This function
    is critical for β-catenin stabilization and downstream transcriptional activation.
  activity:
    term:
      id: GO:0042813
      label: Wnt-activated receptor activity
    support: []
    description: Acts as co-receptor binding Wnt proteins and transducing signals
  location:
    term:
      id: GO:0005886
      label: plasma membrane
    support: []
    description: Single-pass transmembrane protein at cell surface
  complex:
    term:
      id: GO:1990851
      label: Wnt signalosome
    support: []
    description: Forms ternary complex with Wnt ligands and Frizzled receptors
  upstream:
  - term:
      id: GO:0017147
      label: Wnt-protein binding
    support: []
    description: Binds Wnt proteins through β-propeller domains
    mechanism: Four β-propeller domains provide multiple Wnt binding sites
  - term:
      id: GO:0042803
      label: protein homodimerization activity
    support: []
    description: Dimerizes upon Wnt binding to activate signaling
  downstream:
  - term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Promotes β-catenin stabilization and nuclear translocation
  - term:
      id: GO:0016310
      label: phosphorylation
    support: []
    description: Cytoplasmic tail phosphorylation recruits Axin
    mechanism: GSK3B and CK1 phosphorylate PPPSPxS motifs creating Axin binding sites
  - term:
      id: GO:0051091
      label: positive regulation of DNA-binding transcription factor activity
    support: []
    description: Enables TCF/LEF transcriptional activation through β-catenin
  processes:
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0001649
      label: osteoblast differentiation
    support: []
  - term:
      id: GO:0060346
      label: bone trabecula formation
    support: []
  roles:
  - term:
      id: GO:0038023
      label: signaling receptor activity
    support: []
    description: Essential co-receptor for canonical Wnt signaling
- description: Regulates bone formation and bone mass by controlling osteoblast function
    and differentiation. This function is fundamental for skeletal development and
    maintenance of bone density throughout life.
  activity:
    term:
      id: GO:0045124
      label: regulation of bone resorption
    support: []
    description: Controls balance between bone formation and resorption
  location:
    term:
      id: CL:0000700
      label: dopaminergic neuron
    support: []
    description: Expression in hypothalamic neurons regulates bone mass via serotonin
  processes:
  - term:
      id: GO:0045669
      label: positive regulation of osteoblast differentiation
    support: []
  - term:
      id: GO:0002062
      label: chondrocyte differentiation
    support: []
  - term:
      id: GO:0030282
      label: bone mineralization
    support: []
  roles:
  - term:
      id: GO:0070412
      label: R-SMAD binding
    support: []
    description: Cross-talk with BMP signaling in osteoblasts
- description: Modulates glucose and lipid metabolism through regulation of insulin
    signaling and incretin hormone production. This metabolic function links bone
    metabolism to energy homeostasis.
  activity:
    term:
      id: GO:0005009
      label: insulin-activated receptor activity
    support: []
    description: Influences insulin sensitivity and glucose homeostasis
  location:
    term:
      id: GO:0043025
      label: neuronal cell body
    support: []
    description: Hypothalamic expression affects metabolism
  processes:
  - term:
      id: GO:0042593
      label: glucose homeostasis
    support: []
  - term:
      id: GO:0006629
      label: lipid metabolic process
    support: []
  - term:
      id: GO:0030073
      label: insulin secretion
    support: []
    description: Regulates pancreatic β-cell function
  roles:
  - term:
      id: GO:0070328
      label: triglyceride homeostasis
    support: []
    description: Controls lipid metabolism and storage
phenotypes:
- mutation:
    type: gain_of_function
    variant: germline
  effects:
  - term:
      id: HP:0011001
      label: Increased bone mineral density
    description: Missense mutations (G171V, A214V) cause high bone mass syndrome
    support:
    - reference: PMID:12015390
      title: High bone density due to a mutation in LDL-receptor-related protein 5
      supporting_text: The G171V mutation causes high bone density, a wide and deep
        mandible, and torus palatinus by impairing the action of a normal antagonist
        of the Wnt pathway and thus increasing Wnt signaling
      evidence_type: IMP
  - term:
      id: MONDO:0010918
      label: Worth disease
    description: Autosomal dominant high bone mass due to impaired DKK1/sclerostin
      binding
    support:
    - reference: PMID:12579474
      title: Six novel missense mutations in the LDL receptor-related protein 5 (LRP5)
        gene in different conditions with an increased bone density
      supporting_text: Like the previously reported mutation (G171V) that causes the
        high-bone-mass phenotype, all mutations are located in the aminoterminal part
        of the gene, before the first epidermal growth factor-like domain
      evidence_type: IMP
  - term:
      id: HP:0002757
      label: Recurrent fractures
    description: Paradoxically reduced due to increased bone strength
    support: []
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0000939
      label: Osteoporosis
    description: Osteoporosis-pseudoglioma syndrome with severe juvenile osteoporosis
    support:
    - reference: PMID:15850991
      title: LRP5 mutations in osteoporosis-pseudoglioma syndrome and high-bone-mass
        disorders
      supporting_text: Loss-of-function mutations in LRP5 cause osteoporosis-pseudoglioma
        syndrome characterized by congenital blindness and extremely severe childhood-onset
        osteoporosis
      evidence_type: IMP
  - term:
      id: HP:0000618
      label: Blindness
    description: Persistent fetal vasculature and retinal detachment
    support:
    - reference: PMID:22456437
      title: 'Osteoporosis-pseudoglioma syndrome: three novel mutations in the LRP5
        gene and response to bisphosphonate treatment'
      supporting_text: OPPG manifests as juvenile onset osteoporosis with long-bone
        fractures and congenital or early-onset visual disturbances from ophthalmologic
        problems including retinal detachment and microphthalmia
      evidence_type: IMP
  - term:
      id: MONDO:0008190
      label: Osteoporosis-pseudoglioma syndrome
    description: Autosomal recessive disorder with skeletal fragility and ocular abnormalities
    support:
    - reference: PMID:16679074
      title: A family with osteoporosis pseudoglioma syndrome due to compound heterozygosity
        of two novel mutations in the LRP5 gene
      supporting_text: Two novel missense mutations found in a southern Chinese family
        of non-consanguineous marriage, with mutations W478R and W504C identified,
        where affected subjects were compound heterozygotes for both mutations
      evidence_type: IMP
  - term:
      id: HP:0002659
      label: Increased susceptibility to fractures
    description: Multiple fractures from minor trauma
    support:
    - reference: PMID:20096619
      title: Novel LRP5 gene mutation in a patient with osteoporosis-pseudoglioma
        syndrome
      supporting_text: A novel frameshift mutation identified in a 22-year-old Tunisian
        boy from a consanguineous family, specifically a homozygous 5 base pair insertion
        in exon 5 of the LRP5 gene
      evidence_type: IMP
- mutation:
    type: polymorphism
    variant: common
  effects:
  - term:
      id: HP:0004349
      label: Reduced bone mineral density
    description: Common variants associated with BMD variation and fracture risk
    support:
    - reference: PMID:17505772
      title: The effect of LRP5 polymorphisms on bone mineral density is apparent
        in childhood
      supporting_text: LRP5 polymorphisms A1330V and V667M were associated with low
        BMD in physically active men, but not in sedentary men
      evidence_type: IEP
  - term:
      id: HP:0000819
      label: Diabetes mellitus
    description: Variants associated with type 2 diabetes and glucose metabolism
    support:
    - reference: PMID:24482712
      title: Association of LRP5 gene polymorphism with type 2 diabetes mellitus and
        osteoporosis in postmenopausal women
      supporting_text: Association of LRP5 gene polymorphism with type 2 diabetes
        mellitus and osteoporosis in postmenopausal women has been documented
      evidence_type: IEP
---
# LRP5 (LDL Receptor-Related Protein 5)

## Overview
LRP5 encodes a single-pass transmembrane protein that functions as an essential co-receptor for canonical Wnt signaling. Originally identified through its role in bone mass regulation, LRP5 has emerged as a critical regulator of skeletal homeostasis, glucose metabolism, and vascular development. The protein's large extracellular domain contains multiple binding sites for Wnt ligands and antagonists, making it a key regulatory node in Wnt pathway control.

## Structural Features
LRP5 is a 1615 amino acid protein containing:
- Four β-propeller domains (BP1-4) forming the Wnt binding region
- Three LDL receptor type A (LA) domains
- Three EGF-like domains separating the β-propellers
- A single transmembrane domain
- A cytoplasmic tail with five PPPSPxS motifs for signal transduction

The β-propeller domains create distinct binding surfaces:
- BP1-2: Primary binding site for Wnt1 class ligands
- BP3-4: Binding site for Wnt3a class ligands
- BP1: Binding site for antagonists DKK1 and sclerostin

## Signaling Mechanism

### Canonical Wnt Activation
1. **Ligand binding**: Wnt proteins bind to β-propeller domains
2. **Complex formation**: Associates with Frizzled receptors and Wnt
3. **Receptor clustering**: Dimerization/oligomerization of LRP5
4. **Phosphorylation cascade**: 
   - CK1γ phosphorylates initial sites
   - GSK3B phosphorylates PPPSPxS motifs
5. **Axin recruitment**: Phosphorylated motifs bind Axin directly
6. **Complex inhibition**: Sequestration of destruction complex components

### Negative Regulation
- **DKK1 (Dickkopf-1)**: 
  - Binds BP1 domain with high affinity (Kd ~0.3 nM)
  - Forms ternary complex with Kremen1/2
  - Induces rapid endocytosis and degradation
  - Mutations preventing DKK1 binding cause high bone mass
- **Sclerostin (SOST)**: 
  - Binds BP1 domain to block Wnt binding
  - Secreted by osteocytes in response to mechanical unloading
  - Loss causes sclerosteosis and van Buchem disease
- **SOST-DC1**: Additional antagonist in bone
- **Wise/SOSTDC1**: Context-dependent modulator

## Biological Functions

### Bone Homeostasis
LRP5 is a master regulator of bone mass through multiple mechanisms:
- **Osteoblast differentiation**: Promotes mesenchymal stem cell commitment
- **Osteoblast function**: Enhances bone matrix production
- **Osteocyte mechanosensing**: Responds to mechanical loading
- **Osteoclast regulation**: Indirect control via OPG/RANKL ratio
- **Central regulation**: Hypothalamic effects via serotonin signaling

### Metabolic Functions
LRP5 links skeletal and energy metabolism:
- **Glucose homeostasis**: 
  - Enhances insulin secretion from pancreatic β-cells
  - Improves peripheral insulin sensitivity
  - Regulates hepatic gluconeogenesis
- **Lipid metabolism**: 
  - Reduces plasma LDL cholesterol levels
  - Controls triglyceride synthesis and clearance
  - Affects adipocyte differentiation
- **Energy expenditure**: 
  - Influences brown adipose tissue thermogenesis
  - Regulates mitochondrial oxidative metabolism
- **Gut hormone production**: 
  - Stimulates GLP-1 secretion from intestinal L cells
  - Affects GIP and PYY production
  - Controls gut serotonin synthesis affecting bone

### Vascular Development
- **Retinal angiogenesis**: Essential for hyaloid vessel regression
- **Blood-brain barrier**: Maintains CNS vascular integrity
- **Endothelial function**: Regulates vascular permeability

## Clinical Significance

### Genetic Disorders

#### High Bone Mass Syndromes
Gain-of-function mutations cause:
- **Worth disease**: AD inheritance, torus palatinus, wide mandible
- **Endosteal hyperostosis**: More severe skeletal thickening
- **Van Buchem disease type 2**: Cranial hyperostosis

Mechanism: Mutations in BP1 prevent DKK1/sclerostin binding

#### Osteoporosis-Pseudoglioma Syndrome (OPPG)
Loss-of-function mutations cause:
- **Skeletal**: Severe juvenile osteoporosis, fractures, deformities
- **Ocular**: Congenital blindness, persistent fetal vasculature
- **Metabolic**: Impaired glucose tolerance
- **Neurological**: Intellectual disability in some cases

### Common Disease Associations
- **Osteoporosis**: 
  - SNPs rs3736228 (Ala1330Val) and rs4988321 (Val667Met) affect BMD
  - Population attributable risk ~3-5% for fractures
  - Interaction with vitamin D and calcium intake
- **Type 2 diabetes**: 
  - TCF7L2 interaction affects diabetes risk
  - Variants influence incretin response
  - Association with gestational diabetes
- **Cardiovascular disease**: 
  - Role in atherosclerosis through lipid metabolism
  - Affects vascular calcification
  - Links to metabolic syndrome
- **Obesity**: 
  - Influences adipogenesis through Wnt signaling
  - Affects energy balance and fat distribution
  - Connection to childhood obesity

### Therapeutic Implications
LRP5 pathway components are therapeutic targets:
- **Romosozumab**: Anti-sclerostin antibody for osteoporosis
- **DKK1 antibodies**: In development for bone diseases
- **LRP5 agonists**: Potential diabetes therapeutics
- **Lithium**: GSK3β inhibitor indirectly activating pathway

## Evolutionary Perspective
LRP5 and its paralog LRP6 arose from duplication of an ancestral gene in early vertebrates. While both function as Wnt co-receptors, LRP5 evolved specialized roles in bone and metabolism. The presence of disease-causing mutations affecting antagonist binding sites highlights the evolutionary importance of negative regulation. Conservation of LRP5 function across vertebrates underscores its fundamental role in skeletal biology.

## Regulation

### Transcriptional Control
- **PTH**: Upregulates in osteoblasts
- **Mechanical loading**: Increases expression via mechanosensitive pathways
- **Inflammatory cytokines**: TNF-α and IL-1 modulate expression
- **Metabolic signals**: Insulin and IGF-1 regulate transcription

### Post-translational Regulation
- **Phosphorylation**: Multiple kinases regulate activity
- **Palmitoylation**: Affects membrane localization
- **Proteolytic cleavage**: Regulated intramembrane proteolysis
- **Endocytosis**: Clathrin and caveolin-mediated internalization

## Key Interactions

### Direct Binding Partners
- **Wnt Ligands**: 
  - High affinity: WNT1, WNT3A, WNT10B
  - Moderate affinity: WNT9B, WNT7A, WNT7B
  - Tissue-specific: WNT5A (non-canonical context)
- **Co-receptors**: 
  - Frizzled family: FZD1-10 (especially FZD5, FZD8)
  - LRP6: Functional redundancy and heterodimerization
- **Antagonists**: 
  - DKK1: Kd ~0.3 nM, competitive inhibitor
  - Sclerostin: Kd ~1 nM, non-competitive
  - SOST-DC1: Lower affinity modulator
  - Kremen1/2: DKK1 co-receptors for internalization

### Intracellular Partners
- **Destruction Complex**: 
  - Axin1/2: Direct binding to phosphorylated PPPSPxS motifs
  - GSK3B: Phosphorylates cytoplasmic tail
  - CK1α/γ: Initial phosphorylation events
- **Signaling Proteins**:
  - Dishevelled: Bridge to Frizzled
  - β-catenin: Indirect regulation
- **Trafficking**:
  - Mesd/MESDC2: ER chaperone required for folding
  - Clathrin/AP2: Endocytosis machinery
  - Caveolin-1: Lipid raft association