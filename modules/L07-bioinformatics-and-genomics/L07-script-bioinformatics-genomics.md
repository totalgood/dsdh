---
title: Genomics
author: Hobson Lane
date: Jan 6, 2020
# sansfont: Fira Sans
# slide-numbers: true

# mainfont: Hoefler Text
# biblatex: true
# biblatex-chicago: true
# biblatexoptions: [notes, noibid]
# bibliography: ../sources/genomics-dhds-sources.bib
---

# Bioinformatics Spectrumm

- Informatics (Data Science, Statistics, Computer Science)
- Bioinformatics
- Computational Biology
- Biology
- Systems Biology
- Synthetic Biology
- Neuroscience
- AI

# Bioinformatics

- Carl Woese
- Margaret Dayhoff

::: notes


In the 1970's Margaret Dayhoff pioneered the study of protein sequences, how they evolve, and scoring proteins for similarity by measuring their edit distance. She was the first to use PAM substitution matrices to compare protein sequences.
Carl Woes pioneered the study of molecular sequences for explaining phenotype and organism evolution with concepts such as classifying life according to its molecular signature, molecular clocks, inferring phylogeny from ribosomal RNA, and discovered 3rd domain of life, archaea. The other 2 domains are bacteria and eukarya.
:::

# Life

- Eukaryotes (Eukarya)
- Archaea
- Bacteria
- Viruses?

::: notes
Eukaryotes have cell walls and organels within cells.
Viruses are not considered to be alive because they do not have a metabolic system to store and consume energy and cannot replicate on their own without a host organism.
Pandoviruses are so large they can be seen with a normal light microscope and many contain much more DNA than bacteria. So size and complexity is not the dividing line between viruses and life.
:::

# Tree of Life

![Phylogenic Tree of Life based on RNA with 3 broad branches](media/phylogenetic-tree-of-life.svg.png)

::: notes

Phylogenic tree of life based on RNA sequence similarity.

:::

# Self-perpetuating Machinery of Life

DNA -> RNA -> Amino Acids -> Proteins -> Cells -> DNA ->RNC

# Domain Knowledge

- TerraHawk
- Point Cloud

<aside>
    This is the point in microbiology where my expertise begins to peter our.
    I'm not a doctor, and I don't even play one on television.
    Fortunately, even for genomics and bioinformatics, domain knowledge, like understanding microbiology, is not required.
    You just need to understand the inputs and outputs of the model you're trying to build.
    You start with the data.
    You chose a target variable in that data that you'd like to predict.
    And one by one you 
    In fact, sometimes I find that my domain knowledge can prevent me from seeing the most fruitful path forward.
    My background is in physics and robotics.
    So when I first started working on the self-driving car problem in 2004, I focused on giving the machine a 3D picture of the world.
    This is what I knew how to do. 
    I'd hand-craft the kinematics and dynamics models and then see if the machine could fit the real world data into that model.
    That meant we needed 3D data from radar and lidar and stereo scopic cameras to make the system work.
    And we lost the DARPA grand Challenge race across the Mohave desert to the Stanford and Canegie Mellon teams.
    They focused on the Data.
    They knew that humans could recognize objects and estimate their distance using a single image.
    So they knew it would be possible to use conventional machine learning models like logistic regression and linear regression if they could just extract the right features from those images.
    So they tried all the computer vision feature extractors they could think of and fed them into the model.
    And they hit on a combination that worked.
    They used lidar and radar too, to help calibrate the computer vision.
    But their system helped them stumble onto a new computer vision approach that is dominant today.
    It doesn't work at all like the physics models that I used.
    It works like all the other machine learning models.
</aside>
# Genomics

## What is Genomics?

::: notes


:::

# Genomics Data

- 3B+ base pairs
- information-dense (low repetition)

::: notes

The sequencing of the human genome, containing 3B+ basepairs would not have been possible if it weren't for fast comptures with vast storage.
23andme, fitbit spawned a citizen science and self-service medicine trend (quantified self)

:::

# GWAS (Genome Wide Association Studies)

- Correlation between genetic variations and human diseases
- 80% of the variants reported by GWAS are in noncoding regions
- mechanism for noncoding genes to cause disease is unknown

::: notes

Genome Wide Association studies sequence the genome of people suffering from disease.
Their genome is added to a database and annotated with that disease.
After a statistically significant sample set is obtained for a particular disease it's possible to detect genetice variations that  another example of the correlation vs causation challeng of Data Science.

:::

# FDA-Approved Gene Therapies

- Congenital Retinal Blindness
- Spinal Muscular Atrophy

::: Notes

Not only can the genomics detect the cause of disease, it can sometimes be used to cure the disease.
In 2018 the FDA approved Luxturna an AAV virus to deliver a gene that is missing in patients suffering from an inherited eye disease.
This treatment is restoring "functional vision" to the blind.
In 2019 the FDA approved AAV gene therapy, a 2.1 M, single-dose treatment for Spinal Muscular Atrophy (SMA).
Within 5 years there will be 20 therapies approved every year.
And the pace is accelerating.
The more precise editing possibilities of CRISPR are expected to come online in 2030.
:::

# GFF Format

## GFF: [General feature format](https://en.wikipedia.org/wiki/General_feature_format)

1. **sequence**: name of the sequence where the feature is located
2. **source**: source of the feature like "Augustus", "RepeatMasker", "TAIR"
3. **feature**: feature type name, like "gene" or "exon"
4. **start**: Genomic start of the feature, in 1-base offset (unlike 0-offset BED files)
5. **end**: Genomic end of the feature, in 1-base offset
6. **score**: Confidence in  the annotated feature; a "." (dot) indicates a null value.
7. **strand**:  Single character strand of the feature; "+" (5'->3'), "-" (3'->5'), or "." (undetermined).
8  **phase**:   phase of CDS features; 0, 1, 2 or "." (for everything else)
9  **attributes**:  Other information pertaining to this feature

# GFF Clients

- GBrowse (GMOD): [open soruce](http://gmod.org/wiki/Gbrowse)
- IGB (Integrated Genome Browser): [open source](https://igv.org/)
- D3GB (Interactive Genome Browser for Python):

# [.FA](https://en.wikipedia.org/wiki/FASTA_format) (FASTA) File Format

Human-readable [text format](https://en.wikipedia.org/wiki/FASTA_format)
Genomics data file format compatible with natural language processing tools.

# FASTA Amino Acid Sequence Example

```fasta
>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
ADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTID
FPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREA
DIDGDGQVNYEEFVQMMTAK*
```

# FASTA Nucleic Acid Sequence Example

```FASTA
>I:0-62235 within
ccacaccacacccacacacccacacaccacaccacacaccacaccacacc
cacacacacacatcctaacactaccctaacacagccctaatctaaccctg
gccaacctgtctctcaacttaccctccattaccctgcctccactcgttac
cctgtcccattcaaccataccactccgaaccaccatccatccctctactt
actaccactcacccaccgttaccctccaattacccatatccaacccactg
ccacttaccctaccattaccctaccatccaccatgacctactcaccatac
tgttcttctacccaccatattgaaacgctaacaaatgatcgtaaataaca
cacacgtgcttaccctaccactttataccaccaccacatgccatactcac
```


# Public Genomics Data

- [European Variation Archive](https://www.ebi.ac.uk/eva/?Variant-Browser&species=hsapiens_grch37)
- [International Genome Sample Resource](https://www.internationalgenome.org/)

# Private Genomics Data

- [Genomics England](https://www.genomicsengland.co.uk/)
- [NIH Common Fund](https://commonfund.nih.gov/4Dnucleome)

