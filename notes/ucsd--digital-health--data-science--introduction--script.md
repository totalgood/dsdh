# 1: Agenda

::: notes

Welcome to the UCSD Extension Introduction to Digital Health.
In this lecture your going to learn about the upcoming course on Data Science for Healthcare.
First we'll talk about what Data Science is and cut through all the hype.
You'll soon see that a data scientist is more than just a Statistician in Silicon Valley.
And you'll soon see how it takes a bit less skill to make accurate predictions using deep learning than with conventional machine learning models.
You see how and when to use each approach.
After that brief overview I'll describe the syllabus for the Digital Health Data Science course.
Then I'll done into some of the important kernels of knowledge for those lectures that I think will be valuable life skills, even if you never seek to become a data scientist.
And I'll show you how this recently refined understanding of data and statistics is saving thousands of lives each month in the US alone.

:::

# 2: What is data science?

::: notes

Long before data science, there was statistics.
And before that there was science.
But with the invention of the computer after World War II, statistics and data became much more important.
For the first time, machines could process data to model the world.
This allowed statisticians and scientists to begin automating much of their work.

In 1974 Peter Naur recognized the growing importance of data.
He saw in the accumulating data the promise of doing science without performing expensive statistics.
Models of the world could be cleaned from data alone, if we could only develop the right algorithms.
Throughout the first half of the 20th century, scientists were limited in the kinds of models they could convince of and hold in their minds or put down on paper.
Thier models, proofs, and algorithms had to fit within their heads or within a book.
Now, given enough time, there was virtually no limit to the kinds of models could be hypothesized and tested with computers.

And computers brought with them data.
Because we could automate the drudgery of collecting and indexing data, we could gather much more of it.
This in turn fed the growing popularity and success of data analysis and ultimately data science.

So what do these terms mean now.

:::

# 3:

::: Notes

:::

# 4:

::: Notes

:::

# 5: Terminology

::: notes

Peter Naur was a Danish (Denmark not Holland) astronomer turned computer scientist.
Inventor of ALGOL 60, the first computer language with nested function definitions.
Naur is the N in BNF (Backus–Naur form), a grammar specification used in parsing computer languages.

:::

# 6: Automation

::: notes

Prescient astronomers like Peter Naur saw the importance of computers even when they were in their infancy.
But the application of computers to statistics was entirely obvious from the beginning.
After all, the purpose of computers was to compute statistics.
That's where the name came from.
Human statisticians at Blechley Park and NASA embraced the machines because they freed them to do ever higher level thinking about their models and simulations.

Fast forwarding 60 years, computers are now able to perform the work even of radiologists.
This is because they are able to perform detailed statistical analysis on the millions of pixels in an X-ray, far more accurately than the human optical cortex can.

This summer, a Kaggle competition challenged data scientists around the world to train machines to identify pneumothorax (air bubbles in your chest) draw their outline on the X-ray images.
Competitors achieved better than 85% accuracy within the first weeks of announcing the competition and releasing the data.

This rapid progress in the capability of algorithms is making healthcare practiioners nervous.
If machines are able perform diagnoses faster and more accurately than the best doctors, what is left justify a doctors' wages?
A machine only requires days of training on thousands of images rather than 14 years of college, med school and residency.

The precision and complexity of modern deep learning models is also their Achilles' heel.
These models are difficult if not impossible to explain.
They can't point out the patterns they found in an x-ray that helped the neural network identify a light region as pneumothorax as opposed to lung disease.

:::


# 7:

::: notes

:::

# 8:

::: notes

:::


# 9: Explainability

::: notes

In order to effectively employ deep learning and artificial intelligence in healthcare it's helpful to be able to explain the algorithm that produced the prediction.
There are typically many millions of learned parameters in a neural network for high dimensional data like radiology images.
The application that first proved the value of neural networks for image processing (computer vision) was

:::

# 13: Accuracy and Bias

::: notes

DeepMind trained a deep learning model on [700k clinical patient record](https://www.nature.com/articles/s41586-019-1390-1.epdf) at 1200 medical facilities.
AKI (Acute Kidney Injury) 's predictions of AKI (Acute Kidney Injury) and will help UK doctors save lives.
Two days advance notice provides an adequate window to treat or mitigate the causes.
But an accuracy of only 56% means that in 44% of cases the treatments and mitigations will unnecessary, and often harmful.
For example, a friend had a brain tumor removed and was on anti-inflamatories and salt tablets while his brain expanded into the the void left by the removed tumor.
His doctor would take him off some of the anti-inflamatory medications if he thought his kidney was in danger.
But that would  add risk for his brain health and delay his recovery, possibly even reduce his ultimate cognitive capacity.
So this algorithm will likely save more lives than it harms.
But it will nonetheless cause harm and even death to many men and women that would have been better off without the machine's advice.
And what's even more concerning is that the harm is likely to be much greater for women than for men, due to the significant bias in the training set.

:::


# Data Analyst

::: notes

If you're a data analyst you might be exploring a database of healthcare records and hospital outcomes data.
You'll be looking for trends and patterns that can help your hospital or insurer operate more efficiently.
You're looking for "busines-actionable intelligence."
Often you'll have a business or helathcare background and you'll rely a lot on your hunches and intuition and domain knowledge.
You'll be healthcare's version of a Quant (Quantitative Analyst).
You'll be looking for healthcare arbitrage and "alpha" oportunities.

:::

# Statistician

::: notes

If you're a statistician you'll bring to bear your experience with probabilities and proportions and statistics.
You'll show your colleagues where their intuitions are wrong.
You'll use Bayes Rule to refute the prevailing wisdom of performing mastectomy's based solely on mamograms.
And you'll probably know before anyone else that mamograms are a bad idea.
You'll see the world like the Freakonomics authors (Steven Levitt and Stephen Dubner).
You'll help tobacco companies defend their products or you'll help the FDA and the surgeon general find flaws in their logic.
And if you're able to put asside your pre-1980's training you'll probably be onboard with the Causal Revolution.
You'll be able to produce causal models

:::

### Data Scientist

::: notes

Data science is about applying the scientific method to data.
The scientific method is about testing hypotheses.
These hypothese are about new situations, new data that we haven't seen yet.
So Data Science allows us to make predictions about new data based on data that we have.
This isn't necessarily about predictions in the future.
Most of the time it means simply predicting one numerical fact, called the target, based on a bunch of other numerical facts, called features, predictors, or indicators.

If you're a Data Scientist, particularly in the Healthcare industry, you're very likely going to be involved in research.
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

# Healthcare Data Science

- Individual Clinical Healthcare
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






