# 0: (Talking Head)

::: notes

Welcome to the UCSD Extension Introduction to Digital Health.
My name is Hobson Lane and I’ll be your guest instructor for this module.

I will also be your primary instructor for Data Science for Digital Health, the second course in the certificate.

In this lecture you are going to learn about some of the key topics we will cover in the upcoming course on Data Science for Digital Health.
First, we'll talk about what Data Science is.
You'll soon see that a data scientist is more than just a Statistician in Silicon Valley.
I’ll cut through all the hype and help you see the difference between Machine Learning, Neural Networks, Deep Learning, and AI.
In this module you will see how Deep Learning is automating some of the trial and error work of conventional Data Science.
And you will learn about the Data Science tools you need to solve real health care problems to improve people’s lives, including your own.
Then you may be able to appreciate all the enthusiasm about Deep Learning and AI and how it’s accelerating progress in health care.
You’ll see how and when to use each tool in your Data Science toolbox.
After that overview I'll describe the syllabus for the Data Science for Digital Health course.
Then I'll dive into some of the important kernels of knowledge from that syllabus that I think will be valuable life skills, even if you never seek to become a Data Scientist.
And lastly I'll show you how this recently refined understanding of data and statistics is saving thousands of lives each month in the US alone.
Let’s get started!

:::

# 1: Introduction to Digital Health Data Science (first slide)

::: notes

This is the UCSD Extension Introduction to Digital Health.

I'm Hobson Lane.

First I'll talk about what Data Science is all about.

Then I'll give you an overview of what's in the upcoming Digital Health Data Science course.

Then we'll go through some examples of how to apply Data Science to health care.

:::

# 2: Agenda

::: notes

For this module, we'll first talk about what data science is and how it applies to health care.
Then we'll talk about recent trends in data science towards automation, like machine learning and AI.
I'll share the syllabus for the upcoming Digital Health Data Science course, so you know what to expect.
Then you'll learn about a new AI algorithm in the UK that can detect kidney failure two days in advance.
And you'll learn about two important metrics for measuring a machine learning algorithm's performance.
After that you'll learn about the correlation coefficient and its power and peril.
One way to harness the power of correlation is by understanding Bayes Rule.
This is the most important Data Science concept you'll learn today.
Data scientists and health-care practitioners that use Bayes' Rule correctly can save lives.
You'll finish your tour of Digital Health Data Science with a brief introduction to Deep Learning.
You'll even get to build and train your own neural network in an interactive online "playground".
Finally I'll leave you with some quiz and homework assignments.

:::

# 3: What is data science? How does it apply to Health care?

::: notes

So what is data science?

And how does it apply to health care?

Long before data science, there was statistics.
And before that there was science.
But with the invention of the computer after World War II, statistics and data became much more important.
For the first time, machines could process data to model the world and make predictions.
This allowed statisticians and scientists to begin automating much of their work.
And it enabled statisticians to perform science experiments on data, without putting on gloves and getting their hands dirty.
I'll show you how in a bit.

In 1974 Peter Naur recognized the growing importance of data.
He saw in the accumulating data the promise of doing science without performing tedious hand calculation of statistics and without performing physical real world experiments.
Existing data could yield new insights if we just set the machines working on a computational problem to find patterns in the data.

Models of the world could be gleaned from data alone, if we could only develop the right algorithms.
Throughout the first half of the 20th century, scientists were limited in the kinds of models they could conceive of by what they could hold in their minds or put down on paper.
Their models, proofs, and algorithms had to fit within their heads or within a book.
Now, given enough time, there is virtually no limit to the kinds of models that can be hypothesized and tested with computers.

And computers brought with them data.
Because we could automate the drudgery of collecting and indexing data, we could gather much more of it.
This in turn fed the growing popularity and success of data analysis and ultimately data science.

:::

[levitt-2018-accidental-experiment]: http://theboothexp.com/2018/11/modern-data-science-vs-traditional-economics-from-steven-levitt-of-freakonomics/ "Booth Lecture by Steven Levitt on causal models and traditional economics approaches to modeling (natural and randomized experiments) vs data science."

# 4:  What is data science?

::: notes

So how can we do science on health-care data?

Well, like all science, Data Science has traditionally begun with a hypothesis.
But often data is available before the hypothesis.
In the modern world, data keeps flowing in whether or not you've planned an intentional experiment.
And sometimes a nice accidental experiment can be found in the data.
These accidental experiments can reveal relationships no human ever considered.

Accidental experiments are the subject of _Freakonomics_ and _Superfreakonomics_ by Steven Levitt and Stephen Dubner.
For example they used the abrupt legalization of abortion in different US states at different times to determine it's responsibility for the dramatic reduction in violent crime over subsequent decades.
Similarly Jessica Reyes studied the rollout of the ban on leaded gasoline in North America and Europe and found that the resulting reduction in childhood lead exposure was responsible for a large on reduction in crime 15 years later (when those children became teens).

Accidental experiments often reveal a new influencer, a new cause or pattern that we would have never dreamed up on our own.

This is one reason why statisticians and economists like Steven Levitt insist that the data should do the talking before the scientist.
Scientists tend to impose their view of the world on the data.
We can often be led astray by what we believe to be true about the world.
So let's take a look at the process of science.

Science on data is a continuous cycle.

* You can propose a hypothesis
* Run an experiment
* Then gather data
* Then look for patterns in the data that refute or confirm the hypothesis
* And finally use those patterns found in the data to propose a new hypothesis

But it's a cycle, so you can begin with the data just as easily as you could begin with the hypothesis or the experiment.
In fact, if the data already exists, you don't even need to run an intentional experiment or gather new data.
You just need to mine the data for insight.
Look for patterns and see what hypotheses it suggests.
Then you can test it on some other portion of the data or wait for new data to arrive to see if it confirms your hypothesis or not.


:::

[levitt-]: https://pubs.aeaweb.org/doi/pdfplus/10.1257/089533004773563485 "Understanding Why Crime Fell in the1990s: Four Factors that Explain theDecline and Six that Do Not. _Journal of Economic Perspectives_, Volume 18, Number 1, Winter 2004, p 163–190"

[reyes-2007]: https://www.nber.org/papers/w13097.pdf "Environmental Policy as Social Policy? The Impact of Childhood Lead Exposure on Crime. Jessica Wolpaw Reyes, May 2007, NBER Working Paper 13097"

[reyes-2014]: https://www.nber.org/papers/w20366.pdf "LEAD EXPOSURE AND BEHAVIOR: EFFECTS ON ANTISOCIAL AND RISKY BEHAVIOR AMONG CHILDREN AND ADOLESCENTS. Reyes, Jessica Wolpaw. NBER Working Paper 20366"

[reyes-2012]: https://elibrary.ru/item.asp?id=5281613 "Reyes,  Jessica  Wolpaw. 2012. The Impact of Childhood Lead Exposure on Crime. Harvard Department of Economics."

# 5: Advantages of the Data Science Approach

::: notes

So what are the advantages of the accidental experiments of Data Science?

Often it's just cheaper and faster to mine existing data than it is to set up an experiment.
An RCT (Randomized Controlled Trial) or experiment takes a lot of resources and time to recruit subjects, formulate protocols, and collect data.
So if the data is already available you can eliminate the time and expense of the experiment.

And because experiments are so expensive and time-consuming they often collect much less data than is available for a natural experiment.
So natural experiments are often just better.

And sometimes accidental experiments are the only ethical way to perform large scale studies of public health.
You can't ask parents to participate in a study where they are going to be randomly selected to expose their children to toxins like lead and smoke.

:::

# 6: Smoking -> Lung Disease

::: notes

Here's an example Data Science accidental expiment on the effects of smoking.

On the left you can see a map of the smoking rate by state in the US.
You can see from the map on the left that there are some pairs of neighboring states where smoking rates are vastly different on either side of the border.

In Nevada roughly 28% of the population smokes daily.
Across the border to the east, in Utah, the daily smoking rate is approximately 4%.
This provides a nice accidental or natural experiment.

On the right you can see a map of lung disease annual deaths per 100 thousand in the US.
Because smoking causes lung disease you can see a strong correlation in these numbers.
Smoking goes down from 28% in Nevada to 4% in Utah, and death rates go down too, from 43 per 100 thousand in Nevada to 19 per 100 thousand in Utah.

But correlation isn't enough to prove causility.
State borders can create big differences in many other factors that contribute to cancer.
Cultural and religious ideas might encourage healthy activities like outdoor exercise or discourage unhealthy activities like drinking.
And health-care insurance, education, regulation and facilities availability could affect lung cancer detection and treatment.
So the citizens of Utah might be healthier for reasons other than their low smoking rate.

And smoking is a self-selecting trial.
Statisticians argued that smokers might have a genetic "constitution" which caused them to develop lung disease later in life.
Smokers might just be risk takers that participate in a variety of activities that cause cancer.
Statisticians argued that smoking might actually be a preventive measure that partially compensates for other risk factors.

These are called confounding factors.
It takes a lot of work to normalize for all these various possible contributors especially for a disease as complicated as lung cancer.
Can you think of some other factors that might contribute to lung disease?

Back in the 60's and 70's when this debate was raging, Data Science and computers weren't yet a thing, so this analysis took a lot of work and was fraught with human error and bias.

So it wasn't just the Tobacco company lobbyists that held up the Surgeon General's warning about smoking.
It was the lack of Data Science knowhow and tools.

:::

[blog.kaggle.com]: http://blog.kaggle.com/2016/11/30/seventeen-ways-to-map-data-in-kaggle-kernels/ "Seventeen Ways to Map Data in Kaggle Kernels. Megan Risdal, 11/30/2016."

[cancer.gov]: https://statecancerprofiles.cancer.gov/map/map.withimage.php?00&state&001&047&00&0&02&0&1&5&0#results "Lung & Bronchus death rates US Map"

[poison-bottles]: https://pixabay.com/illustrations/poison-bottle-skull-chemical-684990/ "Pixabay poison bottle images"

[moderskeppet-rocket-turtle]: https://vimeo.com/20055097 "Video of rocket-proppelled turtle/tortoise named *Om Adobe Camera Raw* from Moderskeppet.se on vimeo.com"

# 7: Trial and Error

::: Notes

Building and a Data Science model from natural experiment data is a trial and error process.

Your hypothesis suggests some function that relates the input data to the output or target data.
Your input data is usually a row in a table, a vector of *features* or *indicator variables*.
Your output data or *target* is a label for that row that you would like to be able to predict.
Your model needs to learn what multiplications and additions it needs to do on the feature vector to predict the target label.

At each step of the training process your model performs this math on the feature vector to guess the value of the target.
Your model then compares each prediction to the true values from the original training data set.
This helps you see how far and in what direction you need to adjust all the model parameters.
You may be familiar with linear regression where these parameters are just the slopes or weights that are multiplied by each of your feature variables.

Then you just do that prediction again and again on more and more training examples.
After several passes through your dataset you can eventually converge on a set of weights or parameters that gives the best possible predictions of your target.

Once you have a trained model, all that remains is to run a "test set" or "hold out set" through the function to see how well it does.
You can compute your accuracy on new data that your model hasn't been trained on.
This helps you know if your model is going to be useful in the real world.

:::

# 8: Data science on "statistics"

::: notes

Let's do some data science on the word "statistics".

You can see here that usage of the word "statistics" in books and journals peaked in about 1980.
The terms "artificial intelligence", "data science", and "data analysis" started to become more popular in the 80's and 90's as the word "statistics" became less and less popular.

# 9: Statistics about "data science"

::: notes

So let's do some statistics on the term "data science" and some related words.

Peter Naur was a Danish (Denmark not Holland) astronomer turned computer scientist.
Naur is the inventor of ALGOL 60, the first computer language with nested function definitions.
Naur is also the N in BNF (Backus–Naur form), a grammar specification used in parsing computer languages.

Naur was the first to recognize the growing importance of data.
In 1974 as the first personal computers were being sold by Apple and Radio Shack, Naur coined the terms "dataology" and "data science".
Fortunately "dataology" never caught on.
And it took many decades before Data Science finally became a thing.
Usage of the word "statistics" in books and articles began to be replaced by terms like "data science" and "artificial intelligence" in the 80's and 90's.

However an around 1995 AI fell out of favor during an "AI winter", as it was called.
Nonetheless the use of the terms "data science" and "artificial intelligence" resumed their growth around 2010.

:::

[brownlee-2016]: https://machinelearningmastery.com/what-is-deep-learning/ "Deep Learning and Artificial Neural Networks"

# 10: Web search trends

::: notes

Take a look at this plot of web search statistics in recent years.
You can see that the usage of the term "artificial intelligence" is on the rise again.
"Deep learning" and "machine learning" also experienced rapid growth in popularity around 2012.
It was in 2012 that Geoffrey Hinton brought back deep learning by blowing away the accuracy benchmarks of previous machine learning approaches.

:::

[trends.google.com]: https://trends.google.com/trends/explore?date=2008-07-18%202019-08-18&q=artificial%20intelligence,deep%20learning,machine%20learning "Comparison: Machine Learning, Deep Learning, and AI"

# 11: Automation

::: notes

You may have noticed trends in the statistics of data science terminology popularity.
There seems to be growing interest in the automation of data science.
Machines are able to perform more and more Data Science tasks with less and less human thinking and supervision.

Prescient astronomers like Peter Naur saw the importance of computers even when they were in their infancy.
But the application of computers to statistics and science makes sense.
After all, the purpose of computers was to compute statistics.
That's where the word "computer" came from.
It was originally a name for the mathematicians, usually women, who calculated statistics from data.
Code breakers at Blechley Park and statisticians at NASA embraced computers because they freed them to do ever higher level thinking about their models and simulations.

Fast forwarding 60 years, computers are now able to perform the work even of radiologists.
This is because they are able to perform detailed statistical analysis on the millions of pixels in an X-ray, far more accurately than the human optical cortex can.

This summer, a Kaggle competition challenged data scientists around the world to train machines to identify *pneumothorax*.
Pneumothorax is a condition where air bubbles form in your chest near your lungs.
For the Pneumothorax Kaggle Competition, computer algorithms were trained to highlight those regions of chest X-ray images where air pockets had formed.
Within the first weeks of announcing the competition the leader board showed competitors correctly identifing more than 85% of the pneumothorax pixels correctly.
Towards the end of the competition accuracies above 91% were common.

As you can imagine, this rapid progress in the capability of algorithms is making some health-care practitioners nervous.
If machines are able perform diagnoses faster and more accurately than the best doctors, what is left to justify doctors' rigorous training and hard work?
A machine requires only days to training.
A human doctor requires 14 years of expensive training in college, med school and residency.
Of course human doctors learn a lot more than how to read X-ray images and detect pneumothorax.
This general understanding and broad knowledge gives doctors a big advantage over AI.
Nonetheless research into General AI or AGI is underway at places like DeepMind, Elemental Cognition, and IBM Watson.

The precision, speed, and complexity of modern deep learning models is also their Achilles' heel.
These models are difficult if not impossible to explain.
They can't point out the patterns they found in an x-ray that helped the neural network identify the pneumothorax pixels.
These pixels may be slightly darker or lighter, but the machine can't explain why it chose pneumothorax as the diagnosis.
These regions of miscolored pixels could have been lung disease, lung cancer, or even normal tissue and organs in the chest.

We'll talk about the challenge of interpretting and explaining Data Science models in the upcoming course Digital Health Data Science.

:::


# 12: Syllabus

::: notes

In the Digital Health Data Science course next quarter you'll learn about the applications of data science to health care.
In each lecture you'll learn how to solve a new kind of health care problem using data science.

1: In the first lecture you'll get an overview of the terminology and techniques of data science as we discuss some applications and challenges of applying data science to health care.

2: In week two you'll use spreadsheets to perform some data science on tabular data like height, weight, gender, and BMI (body mass index).
Spreadhseets are particularly handy for cleaning and visualizing smaller standalone tables of data.

3: In week three you learn how to build statistical models like maximum likelihood estimators.
And you'll learn about all the lies that statistics told us over the past century, before the causal revolution.
We'll play some serious games with your view of cause and effect.
Your eyes will be opened to a new more correct way of seeing the world.
This new way of analyzing patterns in data will help you save lives.

4: In week four we'll save lives one at a time, with diagnostic models and clinical record data science.
You'll learn the difference between descriptive and prescriptive models.
And you'll learn how to use hospital records to predict diabetes or even kidney failure days or even years in advance.

5: In week five you'll tackle high dimensional data like x-ray images and MRI data.

6: In week six you'll use your data science tools to help hospitals improve their financial performance and patient outcomes.
Logs of activity in a hospital system are called time series data.
Patterns in these logs can be used to improve outcomes for patients at those hospitals lucky enough to have a data scientist mining their data.

7: In week seven you'll expand into higher dimensional datasets that combine both time and geospatial data.
You'll learn about how data science tools are revolutionizing epidemiology and are helping combat Ebola and mosquito-born diseases like Malaria and West Nile virus.

8-10: In weeks eight through 10 we'll dive into special applications of Data Science to health care, including gap analyses, occupational health, and natural language processing for clinical assistance.

11: In week 11 you'll wrap up your understanding of data science by exploring the ethical dilemas that we all face in the coming decades.
You'll learn about privacy and public policy issues that some scientists fear could determine the survival of humanity as a species.

Proj: At the end of the course you'll be given the oportunity to participate in a data science project of your own chosing.
This will be much like a real world data science project that you can tailor to an application that interests you.

:::

# 13: Example Application: Predict Kidney Injury

::: notes

Let's dive into an exciting recent development in data science.

DeepMind trained a deep learning model on 700 thousand clinical medical records at 1200 medical facilities in the UK.
The goal was to detect AKI (Acute Kidney Injury), called the "silent killer".
AKI is hard for doctors to detect or even diagnose in time to do anything about it.
The new system is able to predict serious AKI, two days in advance, with 90% accuracy.

But for less serious conditions the system achieved only 56% accuracy.
This means that in many cases the treatments and mitigations will be unnecessary, and often harmful.
Even worse 44% of AKI will progress without detection by the system.

Nonetheless, this algorithm will likely save more lives than it harms.
Similar to self-driving car technology, some people will be harmed and many more will be saved.
But what's concerning is the imbalance in the demographics of the lives it will save.
Just as pedestrians and cyclists will likely bear the brunt of the mistakes of self-driving cars, women may take the brunt of clinical AI mistakes.
The training set for DeepMind's model consisted of young men in the military.
Women represented only 10% of the data.
This means it is fine tuned to protect men and will not be as effective for women.

:::

[deepmind-2019-aki]: https://www.nature.com/articles/s41586-019-1390-1.epdf) "DeepMind predicts kidney injury"

# 14: Precision

::: notes

So let's talk about some more precise ways to measure the performance of a model like DeepMind's AKI predictor.
This will help you give doctors the information they need to recommend treatment.

Precision is a measure of accuracy of a diagnostic test or predictive algorithm for the positive incidences, when the condition was actually present.
Precision tells us the percentage of positive predictions that are correct.
This is also sometimes called the true positive rate (TP) or the positive predictive value (PPV).

You can see from the formula here, that precision is calculated as the ratio of the correct positive classifications to the total number of positive classifications.

:::

# 15: Recall

::: notes

Recall is a measure of the accuracy of an algorithm for the patients actually suffering from the predicted condition.
Recall is the percentage of patients with a disease that were detected with a particular test or predicted by a particular algorithm.
So for the DeepMind Kidney Failure predictions, this would be the number of patients who were correctly predicted to have kidney injury divided by the total number of patients whose kidneys were actually injured.

:::

# 16: Correlation

::: notes

Correlation between variables is the pattern a machine learning algorithm or data scientist is looking for.
If the disease probability goes up right after some other variable goes up, and if disease probability goes down when the variable goes down, that's called correlation.
Correlation is a measure of how consistently those two variables, the disease and the predictive variable, move together.
If they move together perfectly every time, then they have a correlation of 1.0.
If they move together 50% of the time and move in opposite direction 50% of the time, then they have a correlation of 0.
If they always move in exactly opposite directions, they have a correlation of -1.0.

From these plots it looks like cancer deaths among women seemed to go down as mammograms went up.
This is the kind of data that drove CDC (The Center for Disease Control) to recommend wide spread mammograms.
But if you dig a little deeper, things aren't quite as they seem.

:::

[desantis-2011]: https://onlinelibrary.wiley.com/doi/full/10.3322/caac.20134 "Breast cancer statistics, 2011"

# 17: Correlation is not enough

::: notes

Perhaps another correlation example would help.
Can you see a pattern here?
What would you estimate the correlation coefficient to be for the black and red lines here?
Dig a little deeper.
Does this correlation make sense?
Could eating cheese for breakfast and lunch cause people to get tangled in their bedsheets at night?
Not likely.

Correlation is just not enough.
There are hundreds of spurious correlation plots like this on Tyler Vigen's website.
And all he had to do to generate these plots was to scrape the web for pairs variables that were correlated.
And the combinations of variables you can consider in health care or any other field is virtually endless.
So you need some more tools to separate spurious correlation from real causal relationships.

:::

[vigen-2013]: http://tylervigen.com "Tyler Vigen's catalog of spurious correlations."

# 18: Traditional approach (the Bradford Hill Criteria)

::: notes

In the past, statisticians had to come up with some rules of thumb, a checklist of viewpoints from which to examine the data.
If many of these criteria were met, then the evidence was said to be overwhelming.

Bradford Hill formalized the 6 criteria here in a lengthy paper on scientific evidence and correlation.

The first criteria is consistency.
If multiple studies or datasets or groups all seem to exhibit the same correlation, then that adds weight to the argument.

The second criteria is strength.
If the correlation magnitude is strong, close to 1 then that's evidence that the correlation might actually be causal.

Dose-response is the third criteria.
If the effect increases as the dose or magnitude of the input variable increases, that's yet more corroborating evidence.

Number four is specificity.
If the predictive variable correlates with only one or two potential effects, that's another indication that you've found a causal relationship.

Number five is the temporal relationship.
The cause must happen before the effect for the temporal evidence to add weight to a hypothesis.

Finally, the coherence of the hypothesis adds weight to a theory.
If there is a plausible biological mechanism for the relationship, it may be causal rather than a spurious correlation.

Despite these rigorous criteria, spurious correlations and confounders can still produce misleading results.
This is one of the reasons why we seem to get conflicting advice from year to year on things like diet and exercise and their affect on our health.

:::

# 19: Causal or Confounder

::: notes

Fortunately there's a better way than leaning on the fuzzy Hill Criteria.
Judea Pearl has been a "causal revolution" evangelist since the 1990's.
Most data scientists, economists, and statisticians now agree.
A causal diagram or and influence graph is critical to making the right decisions about causal relationships.
And Judea Pearl has worked hard to formalize a new kind of causal algebra that we can use to manipulated and simplify these diagrams.

Here's an example causal diagram for breast cancer death rates like we discussed earlier.

Imagine scientists and doctors on an advisory panel are using the data from the previous plots to make recommendations about mammogram and physical examination frequency.
In fact they do exactly that, every few years.
Their initial analysis identified a negative correlation between mammogram frequency and breast cancer death rates among women.
Of course they normalized for all the certain biological causes, such as gender, but other causes are not so obvious.
Genetics and ethnicity may not be directly associated with cancer treatment efficacy, but instead might be indicators for other indirect causes such as diet, smoking, and pregnancy rates.
And these environmental factors (including mammogram frequency itself) could just as easily be caused by things like socio-economic status, education, and geographic location (urban vs rural) and any number of other lifestyle choices.
These "other possible causes" are called confounding variables because they interfere with our ability to clearly measure the causal relationship we are interested in.
Can you think of others?

Causal diagrams or influence diagrams are critical to determining whether an association is indicative of causality.
There could be many possible correlates and causes of breast cancer death.
Even though mammograms don't directly cause or prevent breast cancer deaths, they are used to diagnose cancer.
This can determine or influence treatment decisions.
So we'll need to normalize for all those other possible causes of cancer and cancer treatment to determine the cause-effect relationships.
In some cases we can **normalize for** these confounding variables.
In other cases that normalization can create an unintended confounding effect, called the "explain away effect".
In the Digital Health Data Science course I'll show you how to manipulate influence diagrams so that you can perform this normalization correctly.

:::

# 20: Bayes Rule

::: notes

Another common mistake when thinking about correlation is the failure to consider the *prior* or the probability of the event before you start to measure it.
For example, the probability that an aspirin is going to stop your headache in 30 minutes should take into account the probability that the headache would go away on its own in 30 minutes.
For treatment efficacy probabilities, doctors rarely get confused by this analysis.
But for diagnostic test results, like X-rays and blood tests, some studies have suggested that the failure to properly consider the prior results in over-treatment more than half of the time.

Bayes rule is a formula to help you take the prior into account and give you a much better chance at making the right clinical decisions.
To accurately compute the probability of a disease, not only must you know the probability of the diagnostic test being correct (the likelihood ratio), but you must then multiply that by the prior probability of having the disease in the first place.

The vertical bar in this equation is the symbol for the phrase "given that we know" or "assuming that".
So this equations start with the thing you want to know about your blood test or x-ray, the probability that you have a disease if the test is positive.
The terms of the right hand side represent the things we need to know about the test in order to figure that out.

First we need to know how likely the test is to detect the disease, the probability of a positive test given that we know we have the disease.
Then we need to divide that by the probability of the test returning a positive result in general among the entire population.
Finally, we need to multiply this by the prior probability of the disease affecting any individual like you in the population.

:::

# 21: Bayes Rule

::: notes

Because this is such an important concept, and it's been in the news recently, you should use some real numbers to apply Bayes Rule to mammograms.
Each year 1 in 700 women over the age of 40 in the UK contract breast cancer.
This is the prior.
The probability that a mammogram will test positive when a woman does indeed have breast cancer is approximately 72%.
This is called the *sensitivity* of the mammogram test.
This is why doctors often prescribe surgery when they get a positive mammogram result.
Many doctors incorrectly assume that the patient has a 72% chance of having cancer when they receive a positive result.

But you also need to take into account the false alarm rate.
The probability that your mammogram will come back positive, regardless of whether or not you have cancer, is 12%.
Finally you need to compute the positive test result rate for a mammogram.
This is the weighted average of the rates for the False Positive and True Positive Rates.
For the mammogram test this is 12.1%, because only 1 in 700 women contract breast cancer each year.

:::

# 22: Example: Mammograms and breast cancer

::: notes

Now, apply Bayes' Rule using these values: The disease rate, the true positive rate, and the total positive test rate.
When you follow Bayes' rule and multiply out these probabilities you'll find that a woman's probability of having cancer after a single positive mammogram is less than 1%.

This is why in 2016 the CDC increased the recommended age to begin mammogram screen from 40 to 50.
The CDC also recommended a less frequent biennial screening rather than annual screenings.
Mammograms are painful and can be emotionally traumatic if they produce a positive test result.
For many women the risks outweigh the benefit until the age of 50 when Bayes' rule begins to show a net benefit for women having mammograms.

:::

[cdc-2016]: https://www.cdc.gov/cancer/breast/pdf/BreastCancerScreeningGuidelines.pdf "Breast Cancer Screening Guidelines for Women. 2016"

# 23: Deep Learning

::: notes

Bayes rule and other statistical equations can be tricky to implement correctly.
Medical practitioners and patients often get the math wrong.
Fortunately machines are pretty good at computing probabilities, even for thousands or millions of interacting influences and Bayesian prior probabilities.
AI and deep learning promise to help us fallible humans by doing the math for us.
The earliest deep learning networks were simply Bayesian networks, very similar to the influence diagram you saw earlier.

Another advantage of deep learning is that the machine can work directly with the data to measure all the probabilities it needs.
In fact the most shallow neural network (not really deep learning, but still a neural network) is equivalent to a multivariate linear regression on probabilities, like the probability of a patient having cancer.
To create a deep learning model, we simply need to stack these linear regressions in layers.
But these neural networks need to be constructed carefully to avoid the "spurious correlation" and "confounding variable" problem you learned about before.

Nonetheless, deep learning neural networks can find the patterns in really high-dimensional datasets, like external pictures, X-Ray images, or even EKGs (echo-cardio-grams).
A deep learning network can process a set of x-ray images or mammograms and learn to recognize the patterns that indicate a tissue abnormality that might be the result of cancer.
In 2016, Stanford researchers showed that deep learning networks were able to detect some lung diseases better than human radiologists.
And in 2018 researchers in the UK used deep learning models to detect skin melanomas with nothing more than a mobile phone camera image of the patient's skin.
Now AI dermatologists can make house calls without leaving the hospital.

:::

[stanford-2018]: https://engineering.stanford.edu/magazine/article/ai-rivals-radiologist-level-x-ray-screening-certain-lung-diseases "AI rivals radiologist-level X-ray screening for certain lung diseases"

[rajpurkar-2018]: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002686 "Deep learning for chest radiograph diagnosis: A retrospective comparison of the CheXNeXt algorithm to practicing radiologists. 2018, Pranav Rajpurkar, Jeremy Irvin, Robyn L. Ball, Kaylie Zhu, Brandon Yang, et al"

[DeepMind-2017]: https://www.theguardian.com/technology/2017/jan/25/ai-artificial-intelligence-recognise-skin-cancers "AI system as good as experts at recognising skin cancers, say researchers"

# 24: Neural network

::: notes

Why don't you try out a deep learning neural network for yourself.
Take a break from math and play around with neural networks and deep learning.
This neural network playground doesn't have any high dimensional data, but it will help you to see how neural networks are similar to linear regression.
You'll also see that you need to add more and more layers and neurons as the dataset becomes more complicated.

:::

[nueralnet-playground]: http://playground.tensorflow.org "Neural Network Playground (Google TensorFlow)"


# 25: Explainability

::: notes

In order to effectively employ deep learning and artificial intelligence in health care it's helpful to be able to explain the algorithm that produced the prediction.
There are typically many millions of learned parameters in a neural network for high dimensional data like radiology images.
The application that first proved the value of neural networks for image processing (computer vision) was the cats and dogs image classification problem.

In 2012 Geoffrey Hinton showed how to use Convolutional Neural Networks (CNNs) to identify handwritten digits (MNIST) and classify images of cats vs dogs with 10x better accuracy than previous approaches.
However, the convolution neural networks contain millions of trainable parameters.
The network is optimized for correct predictions, not explainability or simplicity (like human-designed models are).

However there are several visualizations that can help you see which parts of an image are important for the classification decisions.
This can be valuable for ongoing training and assistance for radiologists.

First the raw signal output by the neurons for each convolutional filter can show you the areas of the image that contain the particular features, like edges or fuzziness, that helped the network classify this image as a cat image.
You can see that the neurons light up around the ears, eyes, nose, mouth, and head of the cat.
These are the same features that a human would pay attention to.

You can also display a heat map of the important regions of the image by playing the "Peekaboo" game with the image.
If you hide (*occlude*) part of the image and that causes the network to output the wrong answer, then you know that part of the image was important to the network's decision.

And, similar to the activation maps from before, you can display a heatmap of all the filter activations.
You can combine them together by weighting the ones that are most important to the particular class for that image (cat, in this case).

And the gradient (slope) of the activation is an even better indication of the region's importance than the raw activation for the individual filters.

:::

# 26: Assignments

::: notes

So that's it.
Now is your chance to put your new Data Science tools to work.
You'll now take a quiz to exercise your knowledge, and then you'll be given some problems to work on at home.

:::

# 27: Quiz

::: notes

Question number 1. give two applications of DAta Science to Health Care.
Question number 2, How is **Deep Learning** applicable to Health care?
Question number 3, Will Artificial Intelligence replace doctors?
Question number 4, Why or why not?
Question number 5, If a blood test for a particular disease has a False Positive rate of 10% and a False Negative rate of 30%, what’s the test’s precision  (positive predictive value) and  recall (sensitivity)?

:::

# 28: Homework

::: notes

Visit playground.tensorflow.org
Select the spiral dataset and add 20% Noise
Add and remove different combinations of features: x1, x2, x1^2, x2^2, x1*x2, sin(x1), sin(x2)
Play around with different numbers of “HIDDEN LAYERS” and neurons per layer.
How many features, hidden layers and total neurons do you need achieve < 15% test set loss?

:::
