20190720 UCSD intro to data science 
# manual ds (Excel)

Predicting height, weight, Bmi, gender

# confounders

How can you tell the difference between spurious correlation and true causation?

time?
reproducible?
strong/high correlation?
dose effect?


# smoking and cancer

Even when only 2 smokers out of 67 avoided lung disease, still doubts about "did you inhale" question (nonsmoker's inhaled more often, but subsequent studies did not reproduce this anomaly)
- dose effect
- strong correlation
- reproducible results
- consistent with biology and other studies

# controlling for confounders

- case-control studies (twin studies)
- stratifying
- multivariate modeling
- randomization
- double blind experiment

# abortion -> crime 15 years later

- Leavitt: "data should come first
- statistics, data should suggest the hypothesis, not the other way around, as most scientists do
- confirmed when strong predictions about the future proceed correct, 50-60% of the propensity for crime can be determined by abortion availability

# lead -> crime

- ?% of the propensity for crime can be determined by exposure to lead

- Jessica Wolpaw Reyes wrote about the link between crime and lead pollution

# spurious correlation?

plot of lead in preschoolers and crime rates (shifted 15 years)

https://www.motherjones.com/kevin-drum/2018/02/an-updated-lead-crime-roundup-for-2018/

# time series modeling

shifting samples to predict the future
today vs tomorrow is like height vs weight




# Examples
## clinical decision support
- expert systems
- Watson 
- Manceps summarizer

- chexpert comp
- pneumo comp
## augmentation
- aira
- cognitive assistance
- woebot
- neuralink paralysis aid
## personalized medicine
- cancer genetics kaggle comp
- canvas health, Stephanieqaa
- blood test chips
- neuroscience and ai, neuralink, bmi, brain simulation, mapping of the worm brain, Turing test, iq tests, psychometics
- research with luat vaun UCLA on fly brains and optical processing
## population medicine (epidemiology)
- disease weather forecasts (spatio temporal)
- flu genetics prediction
- bioweapon modeling, design, and countermeasures
- eugenics
## research
- citizen science, quantified self
- Blood test chips
- 23 and me
- counsyl


# abortion -> crime references

## dubner Levitt interview 2018

http://freakonomics.com/podcast/abortion/

## Donnahue-Levitt Hypothesis 2002?

http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CDUQFjAA&url=http%3A%2F%2Fpricetheory.uchicago.edu%2Flevitt%2FPapers%2FDonohueLevittTheImpactOfLegalized2001.pdf&ei=roD0UMqLOcbL0AGymYDgDQ&usg=AFQjCNEfFX4oPJiBZ7qeCfphscTehyyNQQ&sig2=f2AWNuJhIbLacdY7o8P88w&bvm=bv.1357700187,d.dmQ

1) Five states legalized abortion three years before Roe v. Wade. Crime started falling three years earlier in these states, with property crime (done by younger people) falling before violent crime.

2) After abortion was legalized, the availability of abortions differed dramatically across states. In some states like North Dakota and in parts of the deep South, it was virtually impossible to get an abortion even after Roe v. Wade. If one compares states that had high abortion rates in the mid 1970s to states that had low abortion rates in the mid 1970s, you see the following patterns with crime. For the period from 1973-1988, the two sets of states (high abortion states and low abortion states) have nearly identical crime patterns. Note, that this is a period before the generations exposed to legalized abortion are old enough to do much crime. So this is exactly what the Donohue-Levitt theory predicts. But from the period 1985-1997, when the post Roe cohort is reaching peak crime ages, the high abortion states see a decline in crime of 30% relative to the low abortion states. Our original data ended in 1997. If one updated the study, the results would be similar.)

3) All of the decline in crime from 1985-1997 experienced by high abortion states relative to low abortion states is concentrated among the age groups born after Roe v. Wade. For people born before abortion legalization, there is no difference in the crime patterns for high abortion and low abortion states, just as the Donohue-Levitt theory predicts.

4) When we compare arrest rates of people born in the same state, just before and just after abortion legalization, we once again see the identical pattern of lower arrest rates for those born after legalization than before.

5) The evidence from Canada, Australia, and Romania also support the hypothesis that abortion reduces crime.

6) Studies have shown a reduction in infanticide, teen age drug use, and teen age childbearing consistent with the theory that abortion will reduce other social ills similar to crime.
