---
title: Genomics
author: Hobson Lane
date: July 22, 2019
sansfont: Fira Sans
slide-numbers: true


mainfont: Hoefler Text
biblatex: true
biblatex-chicago: true
biblatexoptions: [notes, noibid]
bibliography: ../sources/genomics-dhds-sources.bib
---

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

