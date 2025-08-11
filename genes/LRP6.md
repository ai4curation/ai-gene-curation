---
id: UniProtKB:O75581
symbol: LRP6
primary_functions:
- description: Functions as an essential co-receptor for canonical Wnt signaling,
    forming receptor complexes with Frizzled proteins and Wnt ligands. While structurally
    similar to LRP5, LRP6 has broader developmental requirements and is absolutely
    essential for embryonic viability, whereas LRP5 knockout mice survive with bone
    and metabolic phenotypes.
  activity:
    term:
      id: GO:0042813
      label: Wnt-activated receptor activity
    support: []
    description: Co-receptor that binds Wnt proteins and transduces canonical signals
  location:
    term:
      id: GO:0005886
      label: plasma membrane
    support: []
    description: Single-pass type I membrane protein at cell surface
  complex:
    term:
      id: GO:1990851
      label: Wnt signalosome
    support: []
    description: Forms ternary signaling complex with Wnt and Frizzled
  upstream:
  - term:
      id: GO:0017147
      label: Wnt-protein binding
    support: []
    description: Binds multiple Wnt ligands via β-propeller domains
    mechanism: Four β-propeller-EGF repeats provide distinct Wnt binding sites
  - term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: Sequential phosphorylation by CK1 and GSK3
    mechanism: Creates PPPSPxS phospho-clusters for Axin binding
  downstream:
  - term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Essential for β-catenin stabilization
  - term:
      id: GO:1904886
      label: beta-catenin destruction complex disassembly
    support: []
    description: Phosphorylated LRP6 recruits and inactivates Axin
  processes:
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0001701
      label: in utero embryonic development
    support: []
  - term:
      id: GO:0009950
      label: dorsal/ventral axis specification
    support: []
  roles:
  - term:
      id: GO:0038023
      label: signaling receptor activity
    support: []
    description: Essential Wnt co-receptor required for development
- description: Regulates lipid and glucose metabolism through Wnt signaling in metabolic
    tissues. Unlike LRP5, which primarily affects metabolism through central nervous
    system mechanisms, LRP6 directly regulates metabolic processes in peripheral tissues
    including liver, adipose tissue, and pancreas.
  activity:
    term:
      id: GO:0019904
      label: protein domain specific binding
    support: []
    description: Interacts with metabolic regulatory proteins
  location:
    term:
      id: GO:0055037
      label: recycling endosome
    support: []
    description: Cycles between plasma membrane and endosomes
  processes:
  - term:
      id: GO:0010906
      label: regulation of glucose metabolic process
    support: []
  - term:
      id: GO:0042593
      label: glucose homeostasis
    support: []
  - term:
      id: GO:0019216
      label: regulation of lipid metabolic process
    support: []
  roles:
  - term:
      id: GO:0005041
      label: low-density lipoprotein particle receptor activity
    support: []
    description: Contributes to lipid uptake and metabolism
- description: Essential for cardiovascular development and adult cardiac homeostasis.
    LRP6 has more critical cardiovascular functions than LRP5, with null mutations
    causing severe cardiac malformations and embryonic lethality.
  activity:
    term:
      id: GO:0007507
      label: heart development
    support: []
    description: Required for cardiac morphogenesis and valve formation
  location:
    term:
      id: GO:0016020
      label: membrane
    support: []
    description: Expressed in cardiovascular tissues
  processes:
  - term:
      id: GO:0003007
      label: heart morphogenesis
    support: []
  - term:
      id: GO:0001947
      label: heart looping
    support: []
  - term:
      id: GO:0001570
      label: vasculogenesis
    support: []
  roles:
  - term:
      id: GO:0060840
      label: artery development
    support: []
    description: Protects against atherosclerosis
phenotypes:
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0001629
      label: Ventricular septal defect
    description: Homozygous null mutations cause embryonic lethality with cardiac
      defects
    support:
    - reference: PMID:19705442
      title: Cardiac neural crest and outflow tract defects in Lrp6 mutant mice
      supporting_text: Ablation of LRP6 in mice causes conotruncal anomalies including
        double-outlet right ventricle (DORV), outflow tract (OFT) cushion hypoplasia,
        and ventricular septal defect (VSD)
      evidence_type: IMP
  - term:
      id: HP:0001643
      label: Patent ductus arteriosus
    description: Cardiovascular malformations in LRP6-deficient embryos
    support: []
  - term:
      id: HP:0000924
      label: Abnormality of the skeletal system
    description: Delayed ossification and limb defects
    support:
    - reference: PMID:19653321
      title: Generation of Lrp6 conditional gene-targeting mouse line for modeling
        and dissecting multiple birth defects/congenital anomalies
      supporting_text: Homozygotes of LRP6-floxdel mice reproduced typical defects
        as seen in the conventional LRP6-deficient mice, such as defects in eye, limb,
        and neural tube, and die around birth
      evidence_type: IMP
  - term:
      id: HP:0001638
      label: Cardiomyopathy
    description: Adult heterozygotes show cardiac dysfunction
    support:
    - reference: PMID:29344294
      title: Cardiomyocyte-Restricted Low Density Lipoprotein Receptor-Related Protein
        6 (LRP6) Deletion Leads to Lethal Dilated Cardiomyopathy Partly Through Drp1
        Signaling
      supporting_text: Cardiomyocyte-restricted LRP6 deletion causes dilated cardiomyopathy
        partly through Drp1 signaling
      evidence_type: IMP
  - term:
      id: MONDO:0019675
      label: Congenital heart defects
    description: Homozygous null mutations cause complex cardiac malformations
    support:
    - reference: PMID:19705442
      title: Cardiac neural crest and outflow tract defects in Lrp6 mutant mice
      supporting_text: Eight of nine homozygous embryos had both their aorta and pulmonary
        artery originating completely from the right ventricle (double outlet right
        ventricle, DORV), and one exhibited persistent truncus arteriosus (PTA)
      evidence_type: IMP
- mutation:
    type: hypomorphic
    variant: germline
  effects:
  - term:
      id: HP:0003077
      label: Hyperlipidemia
    description: R611C mutation causes elevated LDL and triglycerides
    support:
    - reference: PMID:17332414
      title: LRP6 mutation in a family with early coronary disease and metabolic risk
        factors
      supporting_text: The LRP6 R611C mutation is associated with autosomal dominant
        early coronary artery disease (CAD), features of the metabolic syndrome (hyperlipidemia,
        hypertension, and diabetes), and osteoporosis
      evidence_type: IMP
  - term:
      id: HP:0000855
      label: Insulin resistance
    description: Metabolic syndrome with glucose intolerance
    support: []
  - term:
      id: HP:0002155
      label: Hypertriglyceridemia
    description: Elevated triglycerides in mutation carriers
    support:
    - reference: PMID:17332414
      title: LRP6 mutation in a family with early coronary disease and metabolic risk
        factors
      supporting_text: LRP6 R611C mutation causes dyslipidemia with elevated LDL cholesterol
        and triglycerides
      evidence_type: IMP
  - term:
      id: HP:0001677
      label: Coronary artery disease
    description: Early-onset atherosclerosis in R611C carriers
    support:
    - reference: PMID:17332414
      title: LRP6 mutation in a family with early coronary disease and metabolic risk
        factors
      supporting_text: Mutation carriers have diffuse coronary artery and cerebrovascular
        disease and most often die of cardiovascular disease before age 50
      evidence_type: IMP
  - term:
      id: MONDO:0005148
      label: Type 2 diabetes mellitus
    description: Increased diabetes risk with LRP6 variants
    support:
    - reference: PMID:23703864
      title: Rare nonconservative LRP6 mutations are associated with metabolic syndrome
      supporting_text: LRP6 mutations were screened in two hundred white Americans
        with early onset familial CAD and metabolic syndrome, identifying three novel
        mutations that cosegregated with metabolic traits
      evidence_type: IEP
  - term:
      id: MONDO:0015262
      label: Metabolic syndrome X
    description: R611C mutation causes full metabolic syndrome phenotype
    support:
    - reference: PMID:23703864
      title: Rare nonconservative LRP6 mutations are associated with metabolic syndrome
      supporting_text: Additional mutations identified in LRP6 all reside in the second
        propeller domain, which plays a critical role in ligand binding. These variants
        impair Wnt signaling and act as loss of function mutations
      evidence_type: IMP
- mutation:
    type: polymorphism
    variant: common
  effects:
  - term:
      id: HP:0004349
      label: Reduced bone mineral density
    description: Common variants associated with osteoporosis risk
    support:
    - reference: PMID:33118644
      title: Clinical Phenotype and Relevance of LRP5 and LRP6 Variants in Patients
        With Early-Onset Osteoporosis (EOOP)
      supporting_text: In 50 individuals with early-onset osteoporosis (EOOP), relevant
        variants affecting LRP5 or LRP6 were detected, including 8 LRP6 variants.
        Relevant variants in LRP5 and LRP6 contribute to EOOP in a substantial number
        of individuals
      evidence_type: IEP
  - term:
      id: MONDO:0005298
      label: Osteoporosis
    description: SNPs increase fracture risk in elderly populations
    support: []
  - term:
      id: HP:0001513
      label: Obesity
    description: Variants linked to BMI and fat distribution
    support:
    - reference: PMID:29038835
      title: Interaction between LRP5 and periostin gene polymorphisms on serum periostin
        levels and cortical bone microstructure
      supporting_text: Studies have analyzed SNPs in LRP6 along with other genes including
        LRP5 in postmenopausal women, examining their effects on volumetric BMD and
        bone microstructure
      evidence_type: IEP
  - term:
      id: MONDO:0005044
      label: Hypertension
    description: Associated with blood pressure variation through metabolic effects
    support:
    - reference: PMID:17332414
      title: LRP6 mutation in a family with early coronary disease and metabolic risk
        factors
      supporting_text: The mutation is associated with autosomal dominant early coronary
        artery disease (CAD), features of the metabolic syndrome (hyperlipidemia,
        hypertension, and diabetes), and osteoporosis
      evidence_type: IMP
---
# LRP6 (LDL Receptor-Related Protein 6)

## Overview
LRP6 encodes a single-pass transmembrane protein that serves as an essential co-receptor for canonical Wnt signaling. As the paralog of LRP5, LRP6 arose from an ancient gene duplication event but has evolved distinct and non-redundant functions. While LRP5 primarily regulates bone mass and can be deleted with survival to adulthood, LRP6 has broader developmental requirements and is absolutely essential for embryonic viability. LRP6 knockout mice die at birth with severe developmental defects affecting multiple organ systems, underscoring its more critical role in embryogenesis compared to LRP5.

## Structural Features and Comparison with LRP5
LRP6 is a 1613 amino acid protein (compared to LRP5's 1615 amino acids) with highly conserved domain architecture:
- Four β-propeller/EGF-like domain pairs (PE1-PE4) with 71% sequence identity to LRP5
- Three LDL receptor type A (LA) domains
- Single transmembrane domain
- Cytoplasmic tail with five PPPSPxS motifs and additional regulatory sites

### Key Functional Differences from LRP5:
1. **Wnt Binding Specificity**:
   - LRP6 PE3-PE4: Preferentially binds WNT3A, WNT3
   - LRP5 PE3-PE4: Shows broader Wnt binding including WNT9B, WNT10B
   - Both share similar binding at PE1-PE2 domains

2. **Phosphorylation Sites**:
   - LRP6: Contains additional Ser/Thr sites including S1490 (unique to LRP6)
   - More extensive phosphorylation creates stronger signaling platform
   - T1479 in LRP6 (T1493 in LRP5) shows different kinetics

3. **Antagonist Interactions**:
   - Both bind DKK1 and Sclerostin at PE1
   - LRP6 shows higher affinity for DKK2
   - Different sensitivity to Wise/SOSTDC1

4. **Trafficking Signals**:
   - LRP6 contains unique motifs affecting endocytosis rate
   - Different retromer recognition sequences
   - Distinct caveolin interaction domains

## Signaling Mechanisms

### Signal Initiation
1. **Wnt binding**: Different Wnts bind distinct PE domains
   - PE1-PE2: WNT9B, WNT10B
   - PE3-PE4: WNT3A, WNT3
2. **Receptor clustering**: Wnt induces LRP6 aggregation into signalosomes
3. **Sequential phosphorylation**:
   - T1479 by CK1γ (priming)
   - PPPSPxS motifs by GSK3β
   - Additional sites by multiple kinases
4. **Axin recruitment**: Direct binding to phosphorylated motifs
5. **Signal amplification**: Positive feedback through Axin stabilization

### Signalosome Formation
LRP6 aggregates into membrane-associated platforms:
- Lipid raft association via caveolin
- Clustering enhanced by Dishevelled
- Size correlates with signaling strength
- Dynamic assembly/disassembly regulated

## Biological Functions

### Embryonic Development (Critical Difference from LRP5)
Unlike LRP5, which is dispensable for embryonic survival, LRP6 is absolutely required for:
- **Gastrulation**: Primitive streak formation and mesoderm specification (unique to LRP6)
- **Neural development**: Neural tube closure and brain patterning (LRP5 not required)
- **Heart development**: Outflow tract and valve formation (LRP6-specific)
- **Limb development**: Digit specification and skeletal patterning
- **Placental development**: Labyrinth layer formation (not affected by LRP5 loss)

The embryonic lethality of LRP6 knockouts contrasts sharply with LRP5 knockouts, which survive with primarily skeletal and metabolic phenotypes.

### Metabolic Regulation (Distinct from LRP5 Mechanisms)
While LRP5 affects metabolism primarily through central nervous system serotonin signaling, LRP6 directly regulates:
- **Glucose metabolism**: 
  - Direct enhancement of hepatic insulin sensitivity
  - Pancreatic β-cell proliferation and insulin secretion
  - Peripheral glucose uptake in muscle and adipose tissue
- **Lipid homeostasis**: 
  - Hepatic lipogenesis through SREBP1c regulation
  - VLDL production and LDL clearance
  - Direct effects on cholesterol biosynthesis
- **Energy balance**: 
  - White adipocyte differentiation and lipid storage
  - Brown adipose tissue thermogenesis
  - Mitochondrial biogenesis in metabolic tissues
- **Nutrient sensing**: 
  - mTOR pathway activation in response to nutrients
  - Integration with insulin/IGF signaling

### Cardiovascular Function (More Critical than LRP5)
LRP6 has essential cardiovascular roles not shared by LRP5:
- **Cardiac development**: Required for septation and valve formation
- **Vascular development**: Essential for angiogenesis and vessel patterning
- **Endothelial function**: Maintains vascular barrier and prevents permeability
- **Atherosclerosis protection**: Direct anti-atherosclerotic effects in vessel walls
- **Cardiac homeostasis**: Required for adult myocardial function and survival

### Bone Metabolism (Complementary to LRP5)
While LRP5 is the dominant LRP in bone, LRP6 contributes through:
- **Osteoblast support**: Enhances differentiation in coordination with LRP5
- **Compensatory function**: Can partially compensate for LRP5 loss
- **Fracture healing**: Upregulated during bone repair processes
- **Chondrocyte regulation**: More important than LRP5 in cartilage

## Clinical Significance

### Genetic Syndromes

#### Metabolic Syndrome
The R611C mutation causes:
- Hyperlipidemia (elevated LDL, triglycerides)
- Insulin resistance and diabetes
- Hypertension
- Early coronary artery disease
- Fatty liver disease

Mechanism: Impaired Wnt signaling affects multiple metabolic pathways

#### Developmental Defects
Rare homozygous mutations cause:
- Neural tube defects (spina bifida)
- Congenital heart disease
- Skeletal malformations
- Tooth agenesis

### Disease Associations
- **Type 2 diabetes**: Multiple variants affect disease risk
- **Coronary artery disease**: Causal role through lipid metabolism
- **Osteoporosis**: Variants influence bone density
- **Alzheimer's disease**: Potential role in amyloid clearance
- **Cancer**: Altered expression in various tumors

### Therapeutic Implications

#### Current Strategies
- **Lithium**: GSK3β inhibitor enhancing LRP6 signaling
- **Statins**: May modulate LRP6 expression
- **Anti-DKK1**: Removes pathway inhibition

#### Future Directions
- **LRP6 agonist antibodies**: Enhance signaling for metabolic disease
- **Small molecule modulators**: Target specific domains
- **Gene therapy**: For severe loss-of-function mutations
- **Combination approaches**: With GLP-1 agonists for diabetes

## Evolutionary Perspective
LRP6 and LRP5 arose from gene duplication in early vertebrates approximately 500 million years ago, with the ancestral Arrow gene in invertebrates. Despite 71% sequence identity, evolutionary divergence has created distinct functional specializations:

### LRP6 (Essential Functions):
- Retained broader developmental requirements similar to invertebrate Arrow
- Essential for embryonic viability (conserved ancestral function)
- Broader Wnt ligand responsiveness
- Critical for cardiovascular development (vertebrate innovation)
- Direct peripheral metabolic regulation

### LRP5 (Specialized Functions):
- Evolved specialized bone mass regulation
- Dispensable for embryonic development
- More restricted Wnt specificity
- Central nervous system metabolic control
- Higher expression in bone tissue

The retention of both paralogs despite partial redundancy indicates strong selective pressure for their distinct functions. LRP6's broader essential roles suggest it maintained more ancestral functions, while LRP5 underwent neofunctionalization for specialized skeletal and metabolic regulation. This division of labor allows for more precise developmental and physiological control in complex vertebrate organisms.

## Regulation

### Transcriptional Control
- **HNF4α**: Upregulates in hepatocytes
- **SREBP**: Links to lipid metabolism
- **PPARγ**: Regulates in adipocytes
- **Inflammatory signals**: NF-κB suppresses expression

### Post-translational Modifications
- **Phosphorylation**: Multiple sites regulate activity
- **N-glycosylation**: Required for surface expression
- **Palmitoylation**: Affects membrane localization
- **Ubiquitination**: ZNRF3/RNF43 promote degradation

### Trafficking and Turnover
- **ER quality control**: MESD chaperone required
- **Endocytosis**: Clathrin and caveolin-dependent
- **Recycling**: Retromer complex mediates
- **Degradation**: Lysosomal and proteasomal pathways

## Key Interactions
- **Ligands**: WNT1, WNT3, WNT3A, WNT9B, WNT10B
- **Co-receptors**: FZD1-10, LRP5
- **Antagonists**: DKK1, DKK2, Sclerostin, Wise/SOSTDC1
- **Intracellular**: Axin1/2, GSK3β, CK1γ, Dishevelled
- **Scaffold proteins**: Caveolin-1, MACF1
- **Regulatory**: ZNRF3, RNF43, R-spondins