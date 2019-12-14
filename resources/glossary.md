---
title: Data Science for Digital Health Glossary
path: ~/code/teaching/ucsd/dsdh/resources/glossary.md
---
# Data Science for Digital Health Glossary

To make room for new concepts we compress complex concepts into words.
And then we can compress several words into acronyms to consolidate multiple complex concepts under one "umbrella" concept. Smart people can think analogously across domains. **IDEA**: Can you imagine a neural network structure that would allow analogies and generalizations to encode themselves in the edges/weights of an Artificial Neural Network or the signals within a "meatspace" neural network (collection of neurons in a brain)?

```yaml
ACP (American College of Physicians): Publish guidelines such as bi-annual mammograms after the age of 60. #healthcare #healthcare #L1
AKI (Acute Kidney Injury): DeepMind can predict kidney injury (damage to the kidney from mediations or diabetes or kidney disease) 2 days in advance with 56% accuracy according to [this article](https://www.technologyreview.com/f/614046/deepminds-algorithm-can-predict-serious-kidney-injury-48-hours-before-it-happens/). #healthcare #L1
Allele: A variant form of a given gene, a version of a known mutation at the same place as the original unmodified gene within a chromosome. #genomics #healthcare
CBE (Clinical Breast Exam): The American College of Physicians no longer recommend breast exams, as of 2019. Mammograms continue to be recommended, but less frequently and later in life than earlier recommendations. #healthcare #L1
Chromosome: DNA molecule with part or all of the genetic material (genome) of an organism often including packaging proteins which help maintain the 3D structure of the lengthy sequence of nucleic acids and chaperone proteins which aid in accurate transcription of the DNA into RNA and proteins. #genomics #healthcare
CV (Computer Vision): "Processing images for classification, segmentation, or object detection or processing video for object tracking and SLAM. This term is often used to referred to "classical" computer vision algorithms based on human-crafted algorithms like HOG and SIFT, rather than machine learning or deep learning models like VGG16, ImageNet, or SSD neural networks." #data-science #deep-learning #computer-vision #L1
Degeneracy (of genetic code): some SNPs and SNVs do not significantly change the amino acid sequence (protein) produced by that gene. #healthcare #genomics
DNA (Deoxyribonucleic Acids): Genetic code (sequence) usually composed of the four nucleotides Guanine (G), Cytosine (C), Adenine (A), and Thymine (T). #genomics #healthcare #L2
Explainability: Deep learning models are difficult to interpret or explain because they have millions of traininable parameters across many layers. Tensorflow-Explain is a package that implements simplified visualizations. See [this blog post, bit.ly/ucsdexplain](https://blog.sicara.com/tf-explain-interpretability-tensorflow-2-9438b5846e35) for more info. #data-science #deep-learning #computer-vision #data-science #NLP #L1 #deep-learning #data-science #L5 #L9
Gap Analsyis: Examining scoping review results to look for oportunities for additional research.  #data-science #healthcare  #healthcare #data-science #L8
Genotype: All the genes or genetic variations from a refence gene sequence that determine the phenotype (bilological structure and function) of an individual organism. #genomics #healthcare
GIS (Geographic Information System): Mapping software and and geographic location data analysis and visualization tools. #data-science #GIS #L7 #L3
GMM (Gaussian Mixture Model): Statistical model that the target is a linear combination of gaussian-distributed variables (see GMM). #data-science #deep-learning #computer-vision #NLP #L2 #L9
Grad-CAM (Gradient-weighted Class Activation Mapping): "A measure of pixel importance based on the gradient of the activation for the class label of the image/region. See [this page](http://gradcam.cloudcv.org/) for more info. #data-science #deep-learning #computer-vision" #deep-learning #data-science #L5 #L9
HHS (Health and Human Services): Publishes guidelines and standards regulating the electronic exchange of health information including _Standards for Privacy of Individually Identifiable Health Information_ #healthcare #L3
HIPPA (The Health Insurance Portability and Accountability Act): In 2003 US Congress passed HIPPA which regulates insurance companies. #healthcare #L3
Missense SNPs: Modifications to a genetic code that causes it to produce functionally different or malfunctioning amino acids and proteins. #genomics #healthcare #data-science #L10
MLE (Maximum Liklihood Estimator): Statistical model that assumes the target is a linear combination of randomly-distributed variables (see GMM) and computes predictions from the mean of the conditional probability distribution for the target variable. #data-science #L2 #L3 #deep-learning
Nonsynonymous SNPs: Missense or nonsense SNPs that cause malfunctioning or misfunctioning of the amino acids and proteins produced with this gene. #genomics #healthcare
Nonsense SNPs: Modifications to a gene that causes it to produce nonfunctional amino acids and proteins. #genomics #healthcare
Nucleotide: The basic building blocks of DNA and RNA, molecules consisting of both a nucleoside and a phosphate group. The most common nucleodtides in DNA are Guanine (G), Cytosine (C), Adenine (A), and Thymine (T). #genomics #healthcare
PII (Personally Identifiable Information): Information like birtdates, names, and social security numbers which can be used alone or in combination with other pieces of information to identify an individual. An age over 80 in hospital records is considered PII all by itself. #healthcare #L1 #L2
SaMD (Software as a Medical Device):  The FDA has proposed to regulate AI and ML technology used in medicine as a medical device. #data-science #healthcare
Scoping Review: Paper study, literature review, metadata analysis. #data-science #healthcare
SLAM (Simultaneous Localization and Mapping): A computer vision model (usually a classical human-crafted algorithm) that is designed to estimate the location plus orientation of the camera and also simultaneously estimate the location and pose of objects in the scene in a real-time video feed. Deep learning approaches are beginning to compete favorably with classical computer vision for in accuracy, but they still far less efficient (slower to compute). #computer-vision #data-science #robotics
SmoothGrad (Smoothed Gradient): In [a 2017 paper](https://arxiv.org/pdf/1705.05598.pdf) Smilkov invented a technique for smoothing the gradient by perturbing the input image with weak noise. It produces a better estimate of pixel importances, the "leverage" they have to affect the predictions. #computer-vision #data-science #deep-learning #data-science #L5 #L9
SNP (Single Nucleotide Polymorphism): Substitution at a single nucleotide position that occurs in at least 1% of the population, e.g. rs6311 and rs6313 Serotonin 5-HT2A receptor genes on chromosome 13. #genomics #healthcare #L10
SNV (single nucleotide variation): A single nucleotide substitution that may not meet the 1% population threshold of SNPs. #healthcare #genomics #L10
Synonymous SNPs: SNPs that produce the same amino acid sequence and functionally identical proteins. #data-science #healthcare #genomics #L10
Xiaoice: Microsoft chatbot that serves 100M+ Chinese users. Provides companionship, mental health support, and preventive healthcare advice. #nlp #L9 #L7
```

# Notes

Genome regions
    - coding gene region SNPs
    - noncoding gene SNPs
    - intergenic region of DNA (between genes)

