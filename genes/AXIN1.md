---
id: UniProtKB:O15169
symbol: AXIN1
primary_functions:
- description: Functions as the rate-limiting scaffold protein organizing the β-catenin
    destruction complex, bringing together APC, GSK3β, CK1, and β-catenin to facilitate
    β-catenin phosphorylation and degradation. This function is essential for maintaining
    low β-catenin levels in the absence of Wnt signals.
  activity:
    term:
      id: GO:0008013
      label: beta-catenin binding
    support: []
    description: Binds β-catenin through central domain facilitating its phosphorylation
  location:
    term:
      id: GO:0005737
      label: cytoplasm
    support: []
    description: Primarily cytoplasmic, concentrated in destruction complex
  complex:
    term:
      id: GO:0030877
      label: beta-catenin destruction complex
    support: []
    description: Central scaffold organizing destruction complex assembly with APC,
      GSK3β, CK1α, and β-catenin
  upstream:
  - term:
      id: GO:0070412
      label: R-SMAD binding
    support: []
    description: Binds APC through RGS domain interaction with SAMP repeats
    mechanism: RGS domain recognizes APC SAMP repeats
  - term:
      id: GO:0019901
      label: protein kinase binding
    support: []
    description: Binds GSK3β and CK1 through distinct sites
    mechanism: Brings kinases in proximity to β-catenin substrate
  downstream:
  - term:
      id: GO:0090090
      label: negative regulation of canonical Wnt signaling pathway
    support: []
    description: Promotes β-catenin phosphorylation and degradation
  - term:
      id: GO:0016567
      label: protein ubiquitination
    support: []
    description: Facilitates β-TrCP-mediated ubiquitination
  processes:
  - term:
      id: GO:0030178
      label: negative regulation of Wnt signaling pathway
    support: []
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0006511
      label: ubiquitin-dependent protein catabolic process
    support: []
  roles:
  - term:
      id: GO:0032947
      label: protein-containing complex scaffold activity
    support: []
    description: Master scaffold of destruction complex
- description: Mediates cross-talk between Wnt and other signaling pathways including
    TGF-β/BMP, JNK, and p53 pathways. This function integrates multiple signals to
    coordinate cellular responses.
  activity:
    term:
      id: GO:0070411
      label: I-SMAD binding
    support: []
    description: Binds Smad3 to facilitate TGF-β signaling
  location:
    term:
      id: GO:0005634
      label: nucleus
    support: []
    description: Shuttles to nucleus upon TGF-β stimulation
  upstream:
  - term:
      id: GO:0005160
      label: transforming growth factor beta receptor binding
    support: []
    description: Interacts with TGF-β receptor complex
  downstream:
  - term:
      id: GO:0060395
      label: SMAD protein signal transduction
    support: []
    description: Facilitates Smad3 phosphorylation and nuclear translocation
  processes:
  - term:
      id: GO:0007179
      label: transforming growth factor beta receptor signaling pathway
    support: []
  - term:
      id: GO:0048511
      label: rhythmic process
    support: []
  - term:
      id: GO:0007254
      label: JNK cascade
    support: []
  roles:
  - term:
      id: GO:0030159
      label: signaling receptor complex adaptor activity
    support: []
    description: Integrates multiple signaling pathways
- description: Acts as a tumor suppressor particularly in hepatocellular carcinoma
    and maintains intestinal epithelial homeostasis. AXIN1 concentration is rate-limiting
    for destruction complex activity, making it a critical control point.
  activity:
    term:
      id: GO:0051438
      label: regulation of ubiquitin-protein transferase activity
    support: []
    description: Promotes β-catenin degradation preventing hepatocyte transformation
  location:
    term:
      id: GO:0005634
      label: nucleus
    support: []
    description: Can shuttle to nucleus for transcriptional regulation
  downstream:
  - term:
      id: GO:0008285
      label: negative regulation of cell population proliferation
    support: []
    description: Suppresses hepatocyte and intestinal epithelial cell proliferation
  - term:
      id: GO:0042127
      label: regulation of cell population proliferation
    support: []
    description: Controls stem cell proliferation in intestinal crypts
  processes:
  - term:
      id: GO:0001889
      label: liver development
    support: []
  - term:
      id: GO:0060729
      label: intestinal epithelial structure maintenance
    support: []
  roles:
  - term:
      id: GO:0051117
      label: ATPase binding
    support: []
    description: Critical tumor suppressor in liver and intestinal tissues
phenotypes:
- mutation:
    type: loss_of_function
    variant: somatic
  effects:
  - term:
      id: HP:0002896
      label: Neoplasm of the liver
    description: AXIN1 mutations found in hepatocellular carcinoma and hepatoblastoma
    support:
    - reference: PMID:29525529
      title: AXIN deficiency in human and mouse hepatocytes induces hepatocellular
        carcinoma in the absence of β-catenin activation
      supporting_text: AXIN1 mutations are observed in approximately 8-10% of hepatocellular
        carcinomas, making it one of the top-mutated genes in HCC. Mice with hepatocyte-specific
        AXIN1 deletion developed HCC in the absence of β-catenin induction.
      evidence_type: IMP
  - term:
      id: MONDO:0007256
      label: Hepatocellular carcinoma
    description: AXIN1 mutations in 8-10% of HCC cases, typically biallelic inactivation
    support: []
  - term:
      id: HP:0003003
      label: Colon cancer
    description: Rare AXIN1 mutations in microsatellite unstable colorectal cancers
    support:
    - reference: PMID:16708370
      title: Mutations within Wnt pathway genes in sporadic colorectal cancers and
        cell lines
      supporting_text: AXIN1 has been reported mutated in a subgroup of MSI colorectal
        tumors. Mutations in the Wnt components AXIN1, AXIN2 and TCF4 have been found
        in microsatellite-unstable colon cancers.
      evidence_type: IEP
  - term:
      id: HP:0100007
      label: Neoplasm of the adrenal medulla
    description: Mutations in medulloblastoma with activated Wnt signaling
    support:
    - reference: PMID:12555076
      title: AXIN1 mutations but not deletions in cerebellar medulloblastomas
      supporting_text: 'In the Wnt pathway-associated subset of medulloblastomas,
        missense AXIN1 mutations were found in two tumours: CCC→TCC at codon 255 (exon
        1, Pro→Ser) and TCT→TGT at codon 263 (exon 1, Ser→Cys). Accumulation of β-catenin
        has been observed in the presence of mutations in genes downstream in the
        Wnt pathway, such as APC and AXIN1.'
      evidence_type: IDA
- mutation:
    type: knockout
    variant: experimental
  effects:
  - term:
      id: HP:0000252
      label: Microcephaly
    description: Axin1 knockout mice show neural tube defects
    support:
    - reference: PMID:16620997
      title: Arsenic-induced gene expression changes in the neural tube of folate
        transport defective mouse embryos
      supporting_text: A mutation in the GSK3-binding domain of Axin results in the
        formation of small brains, mimicking human microcephaly. The Axin gene is
        located in the same chromosomal region (16p13.3–12.1) as genetic mutations
        found in microcephaly patients.
      evidence_type: IMP
  - term:
      id: HP:0002084
      label: Encephalocele
    description: Cranial neural tube closure defects
    support:
    - reference: PMID:31628096
      title: 'Novel mouse model of encephalocele: post-neurulation origin and relationship
        to open neural tube defects'
      supporting_text: Mouse embryos homozygous for several Axin1 alleles exhibited
        recessive phenotypes, including axis duplication, suggesting that Axin1 regulates
        embryonic axis formation. Neural tube defects including encephalocele can
        result from disrupted Wnt signaling.
      evidence_type: IMP
  - term:
      id: HP:0000238
      label: Hydrocephalus
    description: Brain malformations in null embryos
    support:
    - reference: PMID:16620997
      title: Arsenic-induced gene expression changes in the neural tube of folate
        transport defective mouse embryos
      supporting_text: Axin is a multifaceted scaffold protein involved in diverse
        signaling pathways that regulate neural progenitor proliferation and differentiation,
        and its deregulation is associated with brain malformations such as micro-
        and macrocephaly, and potentially hydrocephalus in severe cases.
      evidence_type: IMP
- mutation:
    type: polymorphism
    variant: common
  effects:
  - term:
      id: HP:0003002
      label: Breast carcinoma
    description: SNPs associated with breast cancer risk
    support: []
  - term:
      id: HP:0001513
      label: Obesity
    description: Variants linked to metabolic traits
    support: []
---
# AXIN1 (Axis Inhibition Protein 1)

## Overview
AXIN1 encodes a multidomain scaffold protein that serves as the rate-limiting component of the β-catenin destruction complex. Named for its role in axis formation in Xenopus, AXIN1 is a master regulator of Wnt signaling and a tumor suppressor frequently mutated in hepatocellular carcinoma. Beyond Wnt signaling, AXIN1 acts as a molecular hub integrating multiple signaling pathways including TGF-β, JNK, and p53, making it a critical coordinator of cellular responses to diverse stimuli.

## Structural Features
AXIN1 is an 862 amino acid protein with distinct functional domains:
- **RGS domain** (N-terminal): Binds APC SAMP repeats
- **β-catenin binding domain**: Central region for β-catenin interaction
- **GSK3β binding domain**: Recruits GSK3β to the complex
- **PP2A binding region**: Binds protein phosphatase 2A
- **DIX domain** (C-terminal): Mediates polymerization and DVL binding
- **Multiple phosphorylation sites**: Regulate stability and activity

The modular architecture allows AXIN1 to simultaneously bind multiple proteins, creating a signaling platform where enzymatic reactions occur with high efficiency and specificity.

## Functional Mechanisms

### Destruction Complex Organization
1. **Complex assembly**: Brings together APC, GSK3β, CK1α, and β-catenin
2. **Substrate presentation**: Positions β-catenin for sequential phosphorylation
3. **Catalytic scaffold**: Enhances kinase activity toward β-catenin
4. **Product release**: Facilitates transfer of phospho-β-catenin to E3 ligase
5. **Complex recycling**: Allows multiple rounds of β-catenin processing

### Concentration-Dependent Effects
- **Low levels**: Rate-limiting for destruction complex activity
- **Physiological levels**: ~5000 molecules per cell (much less than other components)
- **Overexpression**: Can paradoxically activate Wnt signaling via DIX polymerization
- **Stoichiometry**: 1:1:1 ratio with other core components optimal

### Wnt-Induced Regulation
Upon Wnt stimulation:
1. Recruited to phosphorylated LRP5/6 at membrane
2. Undergoes dephosphorylation by PP1
3. Forms aggregates (signalosomes) with LRP5/6
4. Sequestered from destruction complex function
5. Eventually degraded via tankyrase-mediated PARsylation

## Biological Functions

### Development
- **Axis formation**: Essential for anterior-posterior patterning
- **Neural development**: Required for neural tube closure
- **Embryonic patterning**: Controls segment polarity
- **Organogenesis**: Regulates liver and kidney development

### Adult Tissue Homeostasis
- **Tumor suppression**: Prevents aberrant Wnt activation
- **Metabolic regulation**: Controls hepatic glucose and lipid metabolism
- **Circadian rhythms**: Regulates clock gene expression
- **Stress responses**: Coordinates p53 and JNK activation

### Cross-Pathway Integration
- **TGF-β signaling**: Facilitates Smad3 activation
- **JNK signaling**: Activates MEKK1-dependent cascades
- **p53 pathway**: Enhances p53 phosphorylation under stress
- **mTOR signaling**: Regulates through AMPK interactions

## Clinical Significance

### Cancer
AXIN1 mutations occur in:
- **Hepatocellular carcinoma**: ~8-10% have inactivating mutations
- **Hepatoblastoma**: Frequent mutations in pediatric liver cancer
- **Colorectal cancer**: Rare mutations in MSI tumors
- **Medulloblastoma**: WNT subgroup tumors
- **Ovarian cancer**: Endometrioid subtype

Mutation characteristics:
- Usually truncating mutations causing loss of function
- Biallelic inactivation typical in HCC
- Mutations throughout gene, no clear hotspots
- Often mutually exclusive with CTNNB1 mutations

### Therapeutic Targeting

#### Tankyrase Inhibitors
- Stabilize AXIN1 by preventing PARsylation
- Restore destruction complex function
- Promising for APC-mutant cancers
- Examples: XAV939, G007-LK

#### AXIN1 Stabilization
- Small molecules preventing AXIN1 degradation
- Allosteric activators of destruction complex
- Peptides mimicking AXIN1 interactions

## Regulatory Mechanisms

### Protein Stability
- **Tankyrase**: PARsylation targets for degradation
- **USP34**: Deubiquitination stabilizes AXIN1
- **SUMOylation**: Enhances stability and nuclear localization
- **Phosphorylation**: GSK3β phosphorylation enhances stability

### Expression Control
- **Transcriptional**: Wnt target gene (negative feedback)
- **Post-transcriptional**: miRNA regulation (miR-34a, miR-103)
- **Translational**: IRES-dependent under stress

### Subcellular Localization
- **Cytoplasmic puncta**: Destruction complex aggregates
- **Membrane**: Recruited to LRP5/6 upon Wnt stimulation
- **Nuclear**: Shuttles for TGF-β and p53 signaling
- **Centrosome**: Minor pool during mitosis

## Evolutionary Perspective
AXIN1 is conserved across metazoans, with homologs in cnidarians but not in unicellular organisms, linking its emergence to multicellularity and complex body patterning. The DIX domain shared with Dishevelled suggests ancient domain shuffling events. Vertebrates have two AXIN genes (AXIN1 and AXIN2/Conductin), with AXIN2 being a Wnt target providing negative feedback. The extremely low cellular concentration of AXIN1 compared to other destruction complex components represents an elegant evolutionary solution for sensitive pathway regulation.

## AXIN1 vs AXIN2
Key differences:
- **Expression**: AXIN1 constitutive, AXIN2 Wnt-inducible
- **Stability**: AXIN1 more stable than AXIN2
- **Function**: Largely redundant but tissue-specific roles
- **Cancer**: AXIN1 mutations more common
- **Development**: AXIN1 essential, AXIN2 dispensable

## Key Interactions
- **Destruction complex**: APC, GSK3α/β, CK1α, β-catenin, PP2A
- **Wnt components**: LRP5/6, DVL1/2/3, BTRC
- **Regulatory proteins**: Tankyrase 1/2, USP34, YAP
- **TGF-β pathway**: Smad3, Smad7, TGF-β receptors
- **Stress signaling**: p53, HIPK2, Pirh2, Daxx
- **Metabolic**: AMPK, LKB1, mTOR components