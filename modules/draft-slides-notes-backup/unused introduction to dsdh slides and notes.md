

# Data Analyst

::: notes

If you're a data analyst you might be exploring a database of health-care records and hospital outcomes data.
You'll be looking for trends and patterns that can help your hospital or insurer operate more efficiently.
You're looking for "business-actionable intelligence."
Often you'll have a business or healthcare background and you'll rely a lot on your hunches and intuition and domain knowledge.
You'll be health care's version of a Quant (Quantitative Analyst).
You'll be looking for health-care arbitrage and "alpha" opportunities.

:::

# Statistician

::: notes

If you're a statistician you'll bring to bear your experience with probabilities and proportions and statistics.
You'll show your colleagues where their intuitions are wrong.
You'll use Bayes Rule to refute the prevailing wisdom of performing mastectomy's based solely on mamograms.
And you'll probably know before anyone else that mamograms are a bad idea.
You'll see the world like the Freakonomics authors (Steven Levitt and Stephen Dubner).
You'll help tobacco companies defend their products or you'll help the FDA and the surgeon general find flaws in their logic.
And if you're able to put aside your pre-1980's training you'll probably be onboard with the Causal Revolution.
You'll be able to produce causal models

:::

### Data Scientist

::: notes

Data science is about applying the scientific method to data.
The scientific method is about testing hypotheses.
These hypotheses are about new situations, new data that we haven't seen yet.
So Data Science allows us to make predictions about new data based on data that we have.
This isn't necessarily about predictions in the future.
Most of the time it means simply predicting one numerical fact, called the target, based on a bunch of other numerical facts, called features, predictors, or indicators.

If you're a Data Scientist, particularly in the health-care industry, you're very likely going to be involved in research.
You're going to be testing hypotheses by looking at data.
And you'll use those tests to recommend trials, and A/B testing to back up your claims.
And you'll invariably be disappointed that the "lift" you predicted didn't pan out once you implement your hypothesis in the real world (unintended consequences).

:::

### Machine Learning Engineer

If you're a Machine Learning Engineer, you're likely to be writing software to test hundreds of hypotheses.
And you won't care much about things like confounding variables, causality, or bias.
Like an engineer building anything else, you are just going to be interested in if the model works.
You're not going to care why.
More importantly, your boss and customers aren't going to care why.
They just want a drug or diet or treatment recommendation.




# What's different?

- more data
- new algorithms
- faster computers

::: notes

Moore's law and the Internet have produced a virtuous cycle of exponential growth in data, computational power, and medical technology.

:::

# Virtuous cycle

diagram of arrows of computer tech feeding back into medical tech and spinoff technologies radiating out from that virtuous cycle

## technology <-> science

- neuroscience -> deep learning -> lstm, attention
- gene sequencing -> encoder/decoder -> NLP -> human genome -> 23andme (genetics)
- 2D gene sequencing -> topology, deep learning -> 3D gene sequencing
- MRI -> optical cortex neuroscience -> computer vision architectures -> FMRI
- psychometrics -> goal-based reasoning
- psychology/philosophy -> fuzzy logic -> bayesean networks -> causal diagrams
- BMI -> steven hawking -> physics and math -> better BMI
- wikipedia, pub med -> more educated patients and doctors -> self-help medicine
- embedded processes -> insulin pumps and pace makers -> more data -> treatments for computer scientists

::: notes

Faster and faster computers have enabled computer scientists, physicicists, chemists, and biologists to test and experiment with more and more efficient models and algorithms for biological systems.
And those algorithms have helped scientists generate and record more and more data about biology.
And surprisingly, that data about human biology has spawned new biomimicing algorithms that are better than engineered algorithms for solving many computer science problems.
For example, as we learn more and more about the human brain and neurobiology we are able to apply more and more of that architecture insight into thinking machines, like artificial neural networks.
It's that one advancement, often called deep learning that has
and advance medical technology which have in turned generated more data and life-saving technologies to motivate additional investment and growth in technology.

:::

# Gene Sequencing

::: notes

The sequencing of the human genome, containing 3B base would not have been possible if it weren't for fast comptures with vast storage.
23andme, fitbit spawned a citizen science and self-service medicine trend (quantified self)

:::

# What is a data scientist

- A statistician that can program
- A computer programmer than understand statistics
- A statstician that lives in Silicon Valley

::: notes

So you want to be a data scientist so you can help save lives?


:::

# Digital Health Data Science

- Individual Clinical Health Care
- Occupational Health and Safety
- Population Health

::: notes

Clin health -- individual patient diagnosis and treatment
Occ health -- monitoring and design of the workplace for worker health and safety
Pop health or Epi -- Epidemiology and spatio-temporal data modeling

:::

# Spatiotemporal data

Epidemology data often has

- a place (location in space)
- time (when the data was observed)

This adds 3 dimensions (latitude, longitude, time) to data that is already probably high dimensional.
For most predictive models these discretized locations and and times often become additional dimensions.
Predictive models must deal with extremely high dimensional features.

note{

Epidemiology and populaiton health data is usually recorded over time and the geographic information is critical to the model.
A GIS system is often used to store and visualize spatiotemporal data.
Layers are added/modified over time to show the evolving geography of a phenomenon.
The end result is a "spy satellite" movie.
The past history of all the events nearby are all relevant feature for the prediction of what is about to happen at a particular location at a particular time.

:::

# Epidemiology

Simulations are a special kind of data science modeling, typically used to forecast spatiotemporal data.
A python exercise in simulation of an epidemic.

MIT Intro to Computational Thinking [Problem Set 4: Simulating the Spread of Disease and Bacteria Population (ZIP)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/assignments/PS4.zip)

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






