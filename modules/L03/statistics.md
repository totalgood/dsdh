---
title: Statistics
layout: slides
---

# Statistics

# Agenda

- normal distribution (bell curve)
- simulating normal distribution
- simulating discrete probabilities (die rolls)
- simulating increasing numbers of die rolls summed
- probability is a truth table or possibilities table
- regression to the mean, central limit theorem
- heights/weights
- 2D distribution as 2 dice rolled in confusion matrix
- 2D distribution of height/weight
- normalized 2D distribution and z-scores
- rings of target as 1-sigma bands or z-score increments of .2 or .5
- conditional probability as dungeons and dragons die rolls
- conditional probability as test for disease (continuous = blood test and tumor size)
- accuracy formula and target graphic
- python example (dots on target like wikipedia)
- accuracy of our regression height vs weight
- precision formula and target graphic
- precision of our regression of height vs weight model (accuracy - bias)
- bayes rule
- real world example of bayes rul


# Accuracy

- Continuous numerical predictions (regression):
    - How close to correct are your predictions

<aside class="notes">
    One statistic that you've likely encountered in your daily life is accuracy.
    In the past you've probably used the word accuracy to describe how close your measurements are to the truth.
    In Data Science and Machine Learning we also often talk about the accuracy of a model.
    So in this case your measurements are the predictions that your model makes.
</aside>

### References

- [wiki-accuracy-precision](https://en.wikipedia.org/wiki/Accuracy_and_precision#Common_technical_definition)

# Spurious Correlation

![Cheesy Bedsheet Tanglings](../media/spurious-correlation-tyler-vygen-bedsheet-tangling-deaths.svg)
[tyler vigen](http://tylervigen.com/spurious-correlations)

# Confounding

[NIH guidelines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4017459/)

::: notes
The debate around smoking wasn't entirely the fault of big tobacco lobbying groups. Many doctors and statisticians believed their own statistical analyses that show
At the very end of this long discussion of all the techniques that have been used in the past, and how they are all flawed in one way or another, it finally mentions at the very end that a multivariate model designed with domain knowledge and a causal model are the only way to be sure.
:::

# Causal Revolution

::: notes
Sometimes prediction is not enough. To cure diseases, to save lives, you need a causal model.
:::


# 2: Paradoxes and Fallacies


- Berkson Paradox: why the more attractive people that you date tend to be jerks
- Simpson's Paradox: why politicians can win elections without winning the popular vote (gerymandrring,  electoral college)
- Monty Hall Fallacy: why you should always change your answer in Let's Make a Deal game show

# 3: Monty Hall Fallacy

Real life applications:

- you suspect a patient has one of 3 genes that could cause a disease and you plan to treat based on that one genetic abnormality, then another doctor does a test that confirms the patient does not have one of the others. Should you change your treatment? (must assume that only 1 Gene is present otherwise the abnormality would be greater and the cause obvious, like XOR condition).
- collider on the door chosen to be opened by Monty Hall

# 4: Explain Away Fallacy

- collider where one cause negates the other
- two possible causes of test results then find out that one cause is present, that makes it less likely that the other cause is present

# 5: Berkson's Paradox

- 2 diseases required for admission to hospital (admission's bias) causing `bone disease` and `resperatory disease` to be correlated

                   , general populaiton, general populaiton, general populaiton, hospitalized
resperatory disease, bone disease yes,    bone disease no,   % bone disease,


# 6: Before Cause there was Corroboration

- strength of correlation
- agreement with physics
-

# "Data science"

- Statistics on data
- Epidemiology: Statistics on population data
- Epidemiology was a form of data science in the 20th century

# Bradford Hill Criteria

- English epidemiologist Sir Austin Bradford Hill
- Studies on smoking in the US in the mid 60's
- issued soon after the controversy surrounding the Surgeon General's (Luther L. Terry, M.D) warning against smoking in 1963

# Bayesean vs Frequentist Inference, P-value, and confidence intervals

[github.com/gmj110680/Springboard](https://github.com/gmj110680/Springboard)

# "Do no harm"

- 500 BC: "First, do no harm."
- 1919: "I will not...suffer...Bad Workmanship"
- 1999: "don't be evil"
- 2019: "Hippocratic License (Do No Harm)"

::: Notes


In modern medicine, many physicians around the world contiue to take the Hippocratic Oath when confered their MD or DO degree. In this oath, doctors vow to "First, do no harm."

In the 1920's H. E. T. Haultain, a mining engineering professor at the University of Toronto in Canada proposed that engineers take an ethical oath similar to the Hippocratic Oath of doctors. Legend has it that the oath and ring were inspired by the collapse of the Quebec Bridge due to engineering errors. The text of the oath was written by the English Poet Rudyard Kipling who dubbed it "The Calling".

In 1999 the founders of Google began to appreciate the power and responsibility of information providers and search engines. Amit Patel,  went around the offices of then fledgling Google Corp writing on whiteboards the company's new core value "don't be evil."

In 2019 the Coraline Ada Ehmke's "Hippocratic License" has become the rallying point for software developers concerned about the use of their software to commit human rights violoations.

:::

# Primum non nocere

"Given an existing problem, it may be better not to do something, or even to do nothing, than to risk causing more harm than good."

:::

This "do no harm" ethic is much deeper and more challenging than can be captured in a simple slogan or talking point."
Data Scientists think deeply about cause and effect.
It's natural for this mindfulness of the consequences of machine algorithm decisions to extend to the ethical rammifications of those actions and decisions.
Those of you in the medical field will appreciate the subtlety of the latin phrase "primum non nocere".
It means more than just "do no harm."
Many people elaborate on this interpretation with the idea that:
"given an existing problem, it may be better not to do something, or even to do nothing, than to risk causing more harm than good."

, that  that in healthcare, when the effects can be life changing, problemsour ethical obligations.
It can help to think about the original meaning of the more original, more nuanced, Hippocratic Oath.
It applies to many situations in daily life as well as Data Science in any field or in medicine:

econcretely in the

:::

## References:

[wiki/Iron_Ring](https://en.wikipedia.org/wiki/Iron_Ring)UC
[wiki/Osteopathic_medicine](https://en.wikipedia.org/wiki/Osteopathic_medicine_in_the_United_States)
[wiki/Primum_non_nocere](https://en.wikipedia.org/wiki/Primum_non_nocere)
