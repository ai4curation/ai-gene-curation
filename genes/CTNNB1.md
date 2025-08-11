---
id: UniProtKB:P35222
symbol: CTNNB1
primary_functions:
- description: Functions as a key structural component of adherens junctions, mediating
    cell-cell adhesion by linking E-cadherin to the actin cytoskeleton via alpha-catenin.
    This function is essential for maintaining epithelial tissue integrity and barrier
    function.
  activity:
    term:
      id: GO:0045296
      label: cadherin binding
    support: []
    description: Binds directly to the cytoplasmic domain of E-cadherin and other
      classical cadherins
  location:
    term:
      id: GO:0005912
      label: adherens junction
    support: []
    description: Localizes to adherens junctions at the cell membrane where it forms
      part of the cadherin-catenin complex
  complex:
    term:
      id: GO:0016342
      label: catenin complex
    support: []
    description: Forms the core catenin complex with E-cadherin and alpha-catenin
      at adherens junctions
  upstream:
  - term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: Phosphorylation by various kinases regulates adherens junction stability
    mechanism: Tyrosine phosphorylation at Y142 and Y654 weakens binding to cadherins
      and alpha-catenin
  downstream:
  - term:
      id: GO:0051015
      label: actin filament binding
    support: []
    description: Links to actin cytoskeleton via alpha-catenin
    mechanism: Alpha-catenin bound to beta-catenin connects the complex to F-actin
  processes:
  - term:
      id: GO:0034333
      label: adherens junction assembly
    support: []
  - term:
      id: GO:0034334
      label: adherens junction maintenance
    support: []
  - term:
      id: GO:0098609
      label: cell-cell adhesion
    support: []
  roles:
  - term:
      id: GO:0007155
      label: cell adhesion
    support: []
    description: Primary role in mediating homophilic cell adhesion
- description: Acts as a transcriptional co-activator in the canonical Wnt signaling
    pathway. Upon Wnt stimulation, stabilized beta-catenin translocates to the nucleus
    where it forms complexes with TCF/LEF transcription factors to activate target
    gene expression, regulating cell proliferation, differentiation, and stem cell
    maintenance.
  activity:
    term:
      id: GO:0003713
      label: transcription coactivator activity
    support: []
    description: Functions as a coactivator for TCF/LEF family transcription factors
  location:
    term:
      id: GO:0005634
      label: nucleus
    support: []
    description: Translocates to nucleus upon Wnt pathway activation where it exerts
      transcriptional functions
  complex:
    term:
      id: GO:1990907
      label: beta-catenin-TCF complex
    support: []
    description: Forms transcriptionally active complex with TCF/LEF in nucleus
  upstream:
  - term:
      id: GO:0016055
      label: Wnt signaling pathway
    support: []
    description: Activated by Wnt ligands binding to Frizzled/LRP5/6 receptors
  - term:
      id: GO:0004674
      label: protein serine/threonine kinase activity
    support: []
    description: GSK3B and CK1 phosphorylate beta-catenin for degradation
    mechanism: Sequential phosphorylation at S45 by CK1 and S33/S37/T41 by GSK3B targets
      for ubiquitination
  - term:
      id: GO:0061630
      label: ubiquitin protein ligase activity
    support: []
    description: BTRC/beta-TrCP ubiquitinates phosphorylated beta-catenin
    mechanism: Recognition of phospho-degron leads to proteasomal degradation
  downstream:
  - term:
      id: GO:0006357
      label: regulation of transcription by RNA polymerase II
    support: []
    description: Activates transcription of Wnt target genes
  - term:
      id: GO:0045944
      label: positive regulation of transcription by RNA polymerase II
    support: []
    description: Target genes include MYC, CCND1, AXIN2
  processes:
  - term:
      id: GO:0060070
      label: canonical Wnt signaling pathway
    support: []
  - term:
      id: GO:0045893
      label: positive regulation of DNA-templated transcription
    support: []
  - term:
      id: GO:0008283
      label: cell population proliferation
    support: []
  roles:
  - term:
      id: GO:0090263
      label: positive regulation of canonical Wnt signaling pathway
    support: []
    description: Key effector of canonical Wnt signaling
phenotypes:
- mutation:
    type: gain_of_function
    variant: somatic
  effects:
  - term:
      id: HP:0100242
      label: Sarcoma
    description: Desmoid tumors frequently harbor activating CTNNB1 mutations
    support: []
  - term:
      id: HP:0003003
      label: Colon cancer
    description: Activating mutations found in ~10% of colorectal cancers, particularly
      those with microsatellite instability
    support: []
  - term:
      id: HP:0002896
      label: Neoplasm of the liver
    description: Mutations found in hepatocellular carcinoma and hepatoblastoma
    support: []
- mutation:
    type: loss_of_function
    variant: germline
  effects:
  - term:
      id: HP:0001399
      label: Hepatic failure
    description: Germline loss-of-function mutations cause severe hepatic dysfunction
    support:
    - reference: PMID:24668549
      title: A new intellectual disability syndrome caused by CTNNB1 haploinsufficiency
      supporting_text: Patient with CTNNB1 haploinsufficiency developed severe hepatic
        dysfunction as part of the syndrome
      evidence_type: IMP
  - term:
      id: HP:0002300
      label: Mutism
    description: Associated with intellectual disability syndrome
    support:
    - reference: PMID:27915094
      title: Clinical features associated with CTNNB1 de novo loss of function mutations
        in ten individuals
      supporting_text: Severe speech impairment including mutism is commonly observed
        in CTNNB1 syndrome
      evidence_type: TAS
  - term:
      id: HP:0001249
      label: Intellectual disability
    description: CTNNB1 syndrome includes severe intellectual disability
    support: []
---
# CTNNB1 (Catenin Beta-1)

## Overview
CTNNB1 encodes beta-catenin, a multifunctional protein with two distinct and essential roles: as a structural component of adherens junctions mediating cell-cell adhesion, and as a transcriptional co-activator in the canonical Wnt signaling pathway. This dual functionality makes beta-catenin critical for both tissue integrity and cellular signaling, with tight regulation of the balance between these two pools of the protein.

## Functional Dichotomy

### Cell Adhesion Function
At the plasma membrane, beta-catenin serves as an essential linker protein in adherens junctions, connecting E-cadherin to the actin cytoskeleton through its interaction with alpha-catenin. This structural role is fundamental for:
- Epithelial barrier integrity
- Cell-cell communication
- Tissue morphogenesis and maintenance
- Contact inhibition of cell growth

The adhesive function is regulated by phosphorylation, particularly tyrosine phosphorylation at residues Y142 and Y654, which weakens the interaction with cadherins and alpha-catenin, allowing for junction remodeling during development and wound healing.

### Wnt Signaling Function
In the canonical Wnt pathway, beta-catenin acts as the key signal transducer:
- **Without Wnt signals**: Beta-catenin is continuously synthesized but rapidly degraded by the destruction complex (APC, AXIN, GSK3B, CK1), which phosphorylates beta-catenin at specific N-terminal residues (S45 by CK1, then S33/S37/T41 by GSK3B), targeting it for ubiquitination by beta-TrCP and subsequent proteasomal degradation.
- **With Wnt signals**: Ligand binding to Frizzled/LRP5/6 receptors inhibits the destruction complex, allowing beta-catenin to accumulate, translocate to the nucleus, and form complexes with TCF/LEF transcription factors to activate target genes including MYC, CCND1, and AXIN2.

## Clinical Significance

### Cancer
Mutations in CTNNB1 are found in approximately 10% of all sequenced cancer samples:
- **Colorectal cancer**: Particularly common in microsatellite unstable tumors (~25% of MSI-H cancers)
- **Hepatocellular carcinoma and hepatoblastoma**: Frequent driver mutations
- **Desmoid tumors**: Found in ~85% of sporadic cases
- **Other cancers**: Including ovarian, breast, lung, and brain tumors

Most cancer-associated mutations affect the N-terminal phosphorylation sites (codons 33, 37, 41, 45), preventing degradation and causing constitutive Wnt pathway activation.

### Developmental Disorders
Germline loss-of-function mutations cause CTNNB1 syndrome (neurodevelopmental disorder with spastic diplegia and visual defects), characterized by:
- Severe intellectual disability
- Spastic diplegia
- Microcephaly
- Visual impairments
- Behavioral abnormalities

## Evolutionary Perspective
The dual functionality of beta-catenin represents an elegant evolutionary solution linking cell adhesion state to proliferative signaling. This coupling ensures that cells with compromised adhesion (potentially dangerous for tissue integrity) have altered growth properties, providing a mechanism for tissue homeostasis. The protein's conservation across metazoans underscores its fundamental importance in multicellular organization.

## Regulatory Mechanisms
Beta-catenin levels and localization are controlled through multiple mechanisms:
1. **Protein stability**: Destruction complex-mediated degradation
2. **Phosphorylation**: Multiple kinases regulate both adhesive and signaling functions
3. **Protein-protein interactions**: Competition between adhesive and transcriptional binding partners
4. **Nuclear-cytoplasmic shuttling**: Active transport mechanisms control subcellular localization
5. **Transcriptional feedback**: AXIN2 and other Wnt targets provide negative feedback

## Key Interactions
- **Adhesion partners**: E-cadherin, N-cadherin, alpha-catenin, p120-catenin
- **Destruction complex**: APC, AXIN1/2, GSK3B, CK1, beta-TrCP
- **Transcriptional partners**: TCF1/3/4, LEF1, BCL9, Pygopus
- **Regulatory proteins**: ICAT (inhibitor), CBP/p300 (coactivators)