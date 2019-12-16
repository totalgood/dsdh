---
layout: slides
title: L1 Introduction to Data Science for Digital Health
created: 2019-12-11
---

# 0: (Talking Head)

::: notes

Welcome to the UCSD Extension Data Science for Digital Health.
This is the second course in the Digital Health certificate.
My name is Hobson Lane and I’ll be your instructor for this course.

In this module you will learn about what to expect in the upcoming modules.
The first few slides will give you some learning principles that will help you grasp the subsequent material.
Then you'll see what this "Data Science" thing is all about.
You'll soon be able to use terms like "Bioinformatics", "Machine Learning", and "Artificial Intelligence" not only in the board room or an elevator pitch, but also in your research lab.
You'll know what you're talking about.
You won't just know what these terms mean, you'll know how to use them to solve real healthcare problems.

It's often said that doctors touch the lives of thousands of patients with their healing diagnoses and treatments.
By teaming up with computers, doctors and data scientists can scale that power to touch the lives of millions.
Data Science promises to make medicine more effective and affordable for everyone.
And unlike calculus, your statistics acumen will be useful in your daily life, even if you don't apply them to healthcare.

So let’s get started!

:::

# 1: Introduction to Data Science for Digital Health (first slide)

::: notes

Welcome to the first lesson in the UCSD Extension course "Data Science for Digital Health."

I'm Hobson Lane, your instructor for this lesson.

First I will give you the agenda for this "Introduction to Data Science for Digital Health."

Our agenda will include the course syllabus and what to expect in the rest of the course.

:::

# 2: Agenda

::: notes

In this agenda you can see that you will first build a foundation for your learning.
This approach to learning will help you throughout the course.
You will first learn some best practices for absorbing new material.
You will then get an overview of exactly what data science is and why everyone is so excited to apply it to healthcare.
Then you will see where Data Science fits in among some popular buzz words, terms like:

    Bioinformatics
    Machine Learning
    Deep Learning
    AI or Artificial Intelligence
    Health Informatics
    and, of course, Digital Health

You will even pick up some everyday Data Science insights that you can apply in your everyday life and personal health.

After that you will get familiar with the syllabus for the rest of the Data Science for Digital Health course.
That way you know what to expect, and when in the course you will learn more about powerful technologies like AI.
Finally, like I promised at the beginning, the general principles of Data Science will be applied to real world examples.
You'll learn about a new machine learning algorithm in the UK that can detect kidney failure two days in advance.
And you're not going to be able to sit back and just bask in the progress of others.
You're going to have to learn how those UK doctors evaluated the performance of their kidney disease diagnostic tool.
You'll start to build your own data science tool kit by learning about two important metrics for measuring a machine learning algorithm's performance.
After that you'll learn about another useful performance score, correlation.
You will learn how to use this metric properly without getting misled by the common misconception that correlation implies causation.
Understanding the relationship between correlation and causation will be critical to your ability to use the power of Data Science in the real world.
The exercises for this lecture will require you to compute correlation by hand.
And you'll be quizzed on your ability to ask the right questions about data.

:::

# 3: Big to small

- Pop Health
- Hospital
- Provider
- Patient
- Diease
- Microbiology

::: note

In this lesson, and in this course, you will progress from big picture ideas to microscopic examples.
You'll learn how to apply data science to some of the big picture healthcare problems first, like pop health, population health, or public health.
You will apply statistical theory to examples of disease propagation within populations.
You will progress from population statistics to the biological mechanisms within an individual patient.

The statistics about populations will naturally lead you to questions about individual healthcare organizations like insurers and hospitals.
You will learn the ways data science can help improve the efficiency of those systems.
In this lesson you will see how you can use data science to shatter the previously rigid limits of the iron triangle: affordability, access, and outcome quality.
Once you grasp the big picture you'll dive into the nitty-gritty details of more focused problems in clinical healthcare.

And you'll progress from epidemiology to biology.
You will dive into the biology of an individual patient, using data science to discover the causes of disease and potential preventions and cures.
You will ultimately apply data science from the perspective of the provider, like a doctor or nurse.
At each step along the way you will learn the theory behind the data science.

Towards the end of this lesson you'll even see how data science applies to the molecular biology world of DNA, RNA, and protein sequences.
As in this diagram, you will progress from data science on humanity to data science on the health of individual cells in the human body, like the nerve cell in this fluorescent microscopy photograph.

:::

# 4: Self-Pedagogy

- History and philosophy first
- Quintessential examples, e.g. [spurious correlation](http://tylervigen.com/view_correlation?id=7)
- Critical thinking -- ask questions
- Approaches, tools
- Specific Examples

::: note

Let's talk about pedagogy, the philosophy of teaching.
Within each module you will first learn the history and philosophy of data science and healthcare.
This will help you progress through the same thought processes that great minds like Francis Crick, who discovered DNA, and Judea Pearl, who championed causal diagrams.

That history will help you understand present-day real world examples.
And I think you'll see how the concrete examples help you anchor your understanding.
For example, when I think of the correlation-causation fallacy, I can't help but think of Tyler Vigen's hilarious "disovery".
He showed how per-capita consumption of cheese correlated almost perfectly with death by bed sheet entanglement.

You will also find how important it is to practice the skills you learn and exercise critical thinking.
Asking questions of yourself will help you develop habits and ways of dealing with data.
And you can apply this skeptical mindset to similar problems you encounter outside of class.
When an instructor answers questions with questions, it's called the Socratic method.
Between the questions I ask of you in the quizzes of this course, I suggest you ask questions of yourself and the material you are learning. For example

What is this data trying to tell me?
Why does it work this way?
Are there alternatives/exceptions to this principle? (there almost always are)
Are there examples of this in my life?

Write down your questions and any answers that come to you during the lectures or exercises.
And if you discover something interesting, please share it with me and your fellow students on the discussion forum.
The best way to learn something thoroughly is to teach others.

The most important skill you'll learn in this course is critical thinking.
The theories and principles of biology and statistics that you learn in this course will eventually be replaced by more accurate theories and approaches.
There are almost always exceptions to every rule and approximation in biology.
Biological systems are too complex to be summarized by a model in the same way that the laws of physics model the motion of stars and planets.

But your ability to analyze data and think critically about data science and biology will help you throughout your life.
You will learn to notice mismatches between theory and data throughout your life.

note-to-self: add slides to quiz students on their critical thinking skills using general principles they should already know. use examples from a quack homeopathic medicine book or HSP book, etc. share the horoscope story or even try it on your students.
:::

# 5: Syllabus

Session 1: Lecture 1:  Data Science in Healthcare
Session 2: Lecture 2:  Spreadsheet Data Science
Session 3: Lecture 3:  Statistics, Privacy, Ethics
Session 4: Lecture 4:  Clinical Data Science & Machine Learning
Session 5: Lecture 5:  Deep Learning  & AI
Session 6: Lecture 6:  Hospital Performance Modeling
Session 7: Lecture 7:  Population Health (Epidemiology)
Session 8: Lecture 8:  Public Policy, Privacy & Ethics
Session 9: Lecture 9:  Natural Language Processing
Session 10: Lecture 10:  Bioinformatics and Genomics

::: notes

After this introductory lesson you will have nine more lessons in this ten week course.
In the next lesson you will use a spreadsheet application to create data science visualizations.
In the third lesson you will learn how to use Python, a user-friendly programming language, to speed things up and compute statistics on larger datasets.
Lesson four will cover clinical data science where we'll use machine learning packages in Python to perform clinical diagnoses.
Next you will see how to use deep learning and AI to deal with extremely high dimensional data, like radiology images.
In Lesson six you will analyze and model the performance of hospital systems.
In lesson eight you will tackle big picture public policy, privacy and ethics challenges.
In lessons nine and ten you will learn how to process sequences of english words and then sequences of genes and nucleotides in DNA.

:::

# 6: Continuous Improvement

- Efferent data
- Afferent procedures


::: notes

In 2006 the Institute of Medicine realized that machine learning would make possible more rapid and continuous improvement to the healthcare system.
The institute of medicine published "The Learning Healthcare System", a handbook on evidence-based medicine.
This handbook anticipated the rising importance of data science and machine learning in healthcare, as a feedback tool for continuous improvement.
In 2014, Charles Friedman at the University of Michigan began promoting the concept of "afferent" data feeding back into the brain of the healthcare system.
In our nervous system, "afferent signals", refer to the information carried along neurons from our sensory organs to our brains.
In this biological view of healthcare, efferent signals, with an "e", are the effects of this data on the policies and procedures.
This is evidence-based medicine, which takes its cues from the "data-driven" culture of Silicon Valley startups.

Data science has tightened and accelerated this data-driven feedback loop, giving providers and patients ever more accurate and efficient tools for improving patient lives.

:::

# 6 ALTERNATIVE: Continuous Improvement Philosophy

["Learning Health System"](https://www.ncbi.nlm.nih.gov/books/NBK53494/) 2006 Instutute of Medicine report
["Toward Complete & Sustainable Learning Systems"](https://medicine.umich.edu/sites/default/files/2014_12_08-Friedman-IOM%20LHS.pdf) 2015 Charles P. Friedman, U. Mich.

::: notes

Afferent neuron signals carry information from your six senses to your brain.
In the healthcare system this is the data flowing from doctors and patients into electronic healthcare records and all the disparate databases that "learn" medicine and healthcare.
You can imagine all the places that data exists: hospital operations databases, insurer claims and decisions, pharmaceutical company databases, individual university professor databases, the CDC in Atlanta, healthcare systems in Africa and East Asia, academic journal archives and data sets. And with the growth in social networks, nearly every human being on the planet stores much of their health information in places like Facebook, [Xiaoice (Microsoft Tai re-branded for China)](https://en.wikipedia.org/wiki/Xiaoice), Reddit, and even publicly shares that data on Twitter and in blog posts. Very little of that data flows into the brain of the doctor performing surgery of the  operating on you or pres all the data flowing into hospital operations databases as well as insurer and provider knowledge bases.
Efferent neuron signals tell your muscles (effectors) to move. In the healthcare system these are the regulations, policies, and instruction given to providers.
You can think of the provider (doctor or nurse) as the central nervous system of healthcare system.
The provider is where the rubber hits the road or the scalpel hits the skin.
The doctor or nurse decides what information is relevant and helps the patient make the decision about actions to take to manage their health.
If you think about it, the central nervous system really includes the minds of both the patient and the doctor.
They make all the important decisions and take all the important actions together.
With the democratization of data and tools, more and more of those decisions are made and implemented by the patient directly.
It's this shift towards patient independence from the healthcare system that has doctors worried about AI replacing doctors.
It won't replace all doctors, but it has already replaced many doctors.
The iron triangle has already been shattered in places where there are not affordable options that involve certified medical doctors or hospitals or even nurses, in some cases.
This can have dire consequences for public health, such as the anti-vaxer campaigns on Facebook. Somoa recently passed legislation to limit the spread of measles that resulted when a small minority stopped vaccinating their children. And lawsuits have beenfiled against Facebook and other organizations complicit in this spread of misinformation.

:::

# 7: Iron Triangle

::: notes

In his book _Medicine’s Dilemmas_, William Kissick, the father of Medicare, describes three primary concerns of a healthcare system: Cost, Quality, and Access.
Kissick recognized that these three things are tightly coupled.
This triangle of relationships is described as being iron because of the rigid limitations on providing low-cost, high quality, widely accessible healthcare services.
Since Kissick's proclamation in 1994, that idea has remained.
It is generally assumed that if quality increases, then costs must increase as well.
Data scientists and students like you are trying to stretch the iron triangle so that Healthcare Cost, Quality and Access are no longer rigidly tied together in a zero sum economic system.

Data Science offers us the tools to break out of the iron triangle,
tools like electronic health records and the widespread availability of Internet resources for diagnostics. These make it possible to provide high quality healthcare to everyone with an Internet connection, virtually free.
Healthcare is becoming more and more a self-service industry.
This does not mean that doctors are being replaced.
It just means that their knowledge and insight is being "scaled out" to reach millions more than was possible in the past.

:::


# 8: Advantages of the Data Science Approach

::: notes

In traditional medicine, before a new treatment could be implemented, providers and researchers had to perform experiments on animals and ultimately humans.
These experiments must be randomized to ensure that the results will be applicable to the general population.
These experiments are called randomized controlled trials or RCTs.
An RCT or real-world experiment takes a lot of resources and time to recruit subjects, formulate protocols, and collect data.
These typically require years of work and millions of dollars for each new medical device, procedure, or drug, whether or not it is ultimately approved by the FDA.

Data Science can bypass this process by taking advantage of existing data.
These are called natural experiments, or "accidental experiments" by Steve Levitt and Stephen Dubner of Freakonomics fame.
Data is being recorded from hospitals, doctors, and patients every day.
And now that electronic medical records (EMRs) are becoming common, that data is often centralized and accessible to data scientists.
Often it is cheaper and faster to mine existing data than it is to set up an experiment.
So if the data is already available you can eliminate the time and expense of the experiment.

And because experiments are so expensive and time-consuming they often collect much less data than is available from a natural experiment.
So natural experiments are often more thorough and more accurate.

And sometimes accidental experiments are the only ethical way to perform large scale studies of public health.
You can't ask parents to participate in a study where they are going to be randomly selected to expose their children to environmental toxins or experimental drugs.

Data science offers the promise of Faster, cheaper, better, and more ethical medicine.

:::

[reyes-2007]: https://www.nber.org/papers/w13097.pdf "Environmental Policy as Social Policy? The Impact of Childhood Lead Exposure on Crime. Jessica Wolpaw Reyes, May 2007, NBER Working Paper 13097"


# 10:  What is data science?

::: notes

So how can we do science on healthcare data?
What does a data science pipeline look like?

You'll process data in a straightforward way at first.
You will load data into a table and incrementally clean it up one column or one data type at a time.
But you'll soon discover that the best way to measure the quality of your data is to examine the quality of your predictive model.

So you as soon as you have one or two columns of data cleaned up, you'll proceed to making predictions on that data.
This is your predictive model.
For example, the model you will start with in Lesson 2 will be a linear regression to predict weight from height and gender.
Once you have the predictions from your model, that will tell you if you're on the right track.
You will learn from the accuracy of your model what kind of additional data you should try to include in your next iteration of the model.

So your straight pipeline will quickly bend into a circle as you incrementally feed back what you learn from your model to clean and extract more numerical information from your data.

Traditional science is a continuous cycle.

* Propose a hypothesis
* Run an experiment
* Gather your data
* Then look for patterns in the data
* Use those patterns to propose a new hypothesis or experiment

It's a cycle, so you can begin with the data just as easily as you could begin with the hypothesis or the experiment.
In fact, if the data already exists, you don't even need to run an intentional experiment or gather new data.
You just need to mine the data for insight.
You look for patterns and see what hypotheses it suggests.
Then you can test your model on some other portion of the data or wait for new data to arrive to see if it confirms your hypothesis or not.

:::

[levitt-]: https://pubs.aeaweb.org/doi/pdfplus/10.1257/089533004773563485 "Understanding Why Crime Fell in the1990s: Four Factors that Explain theDecline and Six that Do Not. _Journal of Economic Perspectives_, Volume 18, Number 1, Winter 2004, p 163–190"

[reyes-2007]: https://www.nber.org/papers/w13097.pdf "Environmental Policy as Social Policy? The Impact of Childhood Lead Exposure on Crime. Jessica Wolpaw Reyes, May 2007, NBER Working Paper 13097"

[reyes-2014]: https://www.nber.org/papers/w20366.pdf "LEAD EXPOSURE AND BEHAVIOR: EFFECTS ON ANTISOCIAL AND RISKY BEHAVIOR AMONG CHILDREN AND ADOLESCENTS. Reyes, Jessica Wolpaw. NBER Working Paper 20366"

[reyes-2012]: https://elibrary.ru/item.asp?id=5281613 "Reyes,  Jessica  Wolpaw. 2012. The Impact of Childhood Lead Exposure on Crime. Harvard Department of Economics."

# 11: What is Machine learning?

- machines doing data science automatically

# 12: What is AI

- Artificial intelligence
- a lot of linear or logistic regression
- a lot of logistic regression

# 13: What is Informatics

- Bioinformatics
- Genomics
- Amiomics
- Proteomics
- Phenomics

::: notes

Informatics is
:::

# 14: Data Science Skills

Extracting and loading data
Describing data (data types)
Clean and transform data
Visualizing data
Modeling data

::: Notes

note-to-self:
    - descriptive statistics (count, dimensionality, mean, standard deviation, cardinality, entropy, correlation)
    - Cleaning data (missing values, outliers)
    - Visualizing data
    - Transforming data (scale, limit, logarithmic, back difference, pca, tsne)
    - Modeling data (linear regression, logistic regression, decision tree, random forest, boosted trees, neural networks)

So what are the skills you need to be a part of this data science revolution in healthcare.
You will first need to learn how to extract data from an information system.
In most cases this will be a matter of visiting a web address and downloading a file, like a CSV (comma-separated values) file.
You will then need to recognize the various data types useful to data science.
You will learn to recognize categorical variables, like gender or eye color or categories of disease.
You will learn how to recognize continuous numerical variables, like height and weight and blood pressure, which can be used directly in your data science pipeline.
You will also learn how to deal with more complicated data types like date, time, and geographic location information.

Then you will clean and transform your dataset so that it can be used in a Data Science model.
your goal is to create a table of numerical data, without any strings, or missing values.
In computer science strings are the natural language sequences of characters, words and phrases.
This process of downloading, transforming, and then loading the numerical data into a table is called ETL, or Extraction Transform Load.
In Lesson 2 of this course, you will do this ETL entirely in a spreadsheet.

Then you will get to the fun visual part of the process.
You will learn to create plots from this numerical data.
These plots will help you detect anomalies and patterns, and ultimately fit a predictive model to your numerical variables.

You will start your data science journey by building on your existing understanding of math and spreadsheets.
As you work in a spreadsheet on your first exercise, you will quickly see the limitation of the spreadsheet as a data science tool.
This will motivate you to move on to more programmatic approaches.
You will learn how to write small python programs that automatically accomplish everything you learned in the spreadsheet exercises, and more.

:::

# 17: Loading data

- text files (CSV, TSV, JSON, TXT)
- compressed files (ZIP, GZ)
- binary files (XLS, PDF, Images)
- web pages (links to HTML)
- databases

::: note

In Lesson 3, the first bit of Python magic you will learn is how to extract and load data.
It will feel like casting a spell each time you give python a command and it goes out onto the web or your hard drive and retrieves nice tables of numerical data for you.
You'll start with files that you've probably seen before, like text files and CSV files (comma separated values).
You'll learn how to automate the reading and cleaning of those files using python, so you no longer have to spend your days scrolling through massive spreadsheets of numbers.
This will be your first chance to see the power of python to do data science.
No longer will you be limited to the files you can import into Excel.

If you want to get a head start, or take a shortcut on your spreadsheet data science assignment, search for the Pandas python package.
You can play around with it in the Jupyter notebook environment provided in this course.

:::

# 18: Describing Data (data types)

Continuous: numerical values like height, weight, blood pressure, temperature
Categorical: gender, eye color, disease names
Natural language: symptom descriptions, medical procedure descriptions
Sequence: genome, DNA, RNA, protein, chemical pathways
Time series: treatment timelines, hospital records, EKG/EEG recordings)
Geographic: epidemiology, maps of clinic locations
Imagery: X-rays, MRI slices, CAT scan slices, photos of skin abnormalities

::: note

Throughout the course you'll incrementally learn about various data types.
You'll learn to perceive the world like a Data Scientist.
Numbers and text will be the fuel for your predictive models.
This will help you see how a particular dataset can be used for data science.
You'll soon see how each kind of variable fits into a data pipeline.
You'll learn to load and manipulate the most straightforward data types first.

Numerical data like height, weight, and temperature is what machines were built for. So you'll start there.
Categorical data may not be as obvious to you.
So you'll build your understanding of various kinds of categorical data as you progress through the modules, data like gender, eye color, or disease names.
You'll work your way from categorical data into time series data where your intuitions about dates and times will be useful for extracting both categorical and continuous numerical data.
From that foundation you'll dive into sequences of words and characters that humans read, called natural language.
Machines can extract data and information from lengthy clinical medical records or technical documents and summarize or plot it.
And those sequences will incrementally become less and less comprehensible by humans as you learn how to use machines to process longer and more complicated sequences of data like DNA and the human genome.
Finally you'll eventually put on your radiology hat as you examine X-ray and MRI imagery and even cell phone camera images of patients.
You'll learn how to train a machine to see things that a human doctor might miss.
:::

# 19: Describing data

- summarize
- understand

::: notes

This slide is about statistics.
But I didn't want to scare you by putting it in the title.
I'll save that title for the next lesson where we'll dig deep into statistics.
Statistics is just arithmetic for helping you describing and understanding data.
Yes, the terminology of statistics like mean and variance may not be as familiar to you as the terminology of geometry like right triangle or polygon.
But that's just because the US school system is broken.
Steven Levitt has been trying to fix that for 20 years with his Freakonomics campaign.
And I'll try to get you up to speed with the rest of the civilized world in the next lesson.

But for now I'd just like you to appreciate the power of descriptive statistics.
Descriptive statistics are just numbers that summarize and describe data.
So, let's say you had a list of 7 numbers, say, your heart rate each morning for the past 7 days. You could probably describe that to a friend by just listing a few of the interesting ones, like:
"On Saturday and Sunday I had a heart rate below 60 BPM (beats per minute) when I woke up, but by monday morning I was at 70 BPM before I even sat up!"

So that natural language description of numbers works great when you don't have a lot of numbers to describe.
But what do you do if you have one hundred thousand measurements of the individual heart beats over a day or so?
Your smartwatch, fitbit, or EKG machine can provide you that massive amount of data in a heartbeat.
If you started droning on about all that data to your friend, you wouldn't get more than a minute or two into your soliloquy before she'd roll her eyes and walk away.

So you need to learn statistics if you are going to have interesting water cooler conversations about your heart rate variability, a very accurate measure of stress and even longevity.

TODO: finish this and make slide

:::

## References

[Teach Math through programming](https://www.ted.com/talks/conrad_wolfram_teaching_kids_real_math_with_computers) by Conrad Wolfram, TED Talk, July 2010
[Math education doesn't add up](http://freakonomics.com/podcast/math-curriculum/) by Steven D. Levitt, Freakonomics, Oct 2019


--
------------------------------------------------------------------

# Nurse Bots

- [25 medical search engines in 2009](https://onlinenursepractitionerprograms.com/2009/top-25-health-medical-search-engines/)
- [80% of Americans search for health information online in 2013](http://www.nbcnews.com/id/3077086/t/more-people-search-health-online)

# Common Search Queries in 2015

- Is bronchitis|pneumonia contagious?
- How much water|calories should I consume?
- What is Lupus?
- When do I ovulate?
- How far along is my preganancy

Reference: [health.com](https://www.health.com/cold-flu-sinus/top-health-searches-google-2015)

::: note
People ask search engines serious medical questions that could have a significant affect on their lives.
Knowing about lupus may not be important to your personal health.
But knowing how to monitor a pregnancy or tell when you might get pregnant can be life changing information.
Often people are more comfortable asking questions of DuckDuckGo than they are of their physician.
And they'll often get more accurate, up-to-date, and detailed information than their doctor can provide.
Search engines can provide links to real world examples and symptoms that doctors may not be comfortable discussing, for fear of alarming or misleading their patients.
Patients can spend more time reading articles online than they can afford to spend with their doctor.
:::

# Virtual Assistants

- WebMD
- Wikipedia
- Duck
- Siri
- Google
- Alexa

![](media/L1/WikiQA-92pct-ANSQ+WikiQA.png)
::: note
People use virtual assistants and search engines as their nurse or healthcare advisor.
Search engines have begun to incorporate direct question answering.
DuckDuckGo can answer questions like "what is bonchitis" directly.
Search engines use Wikipedia as a knowledge base and will quote the relevant sentence or section that answers your questions.
WebMD and DuckDuckGo is about to get a lot smarter.
In December 2019, NLP researchers showed how to find the best possible Wikipedia sentence to answer any question [92% of the time].
The previous record was 76%.
:::

# Everyday uses

- Learning how to interpret the statistics you hear in the news
- Plus you'll have interesting cocktail party insights about things like psychology and human behavior
- When your friends
- Reading statistics in the newspaper articles with s critical eye
- Reading about the benefits and
- Listening to Freakonomics episodes
- Watching TED talks and

::: notes

You're going to learn the philosophy of data science, how to think like a data scientist.
You're going to learn how to think better and how to think better about thinking.
And this perspective will make you a better thinker not only in healthcare decisions but in everyday life.
You'll learn how to coach others into making better lifestyle choices, and you'll have the tools to coach yourself, influence your own mind.
You can take back your mind from corporate advertisers and social network applications who are using data science to manipulate you.
Just like a vaccine like the flu shot teaches your body how to fight disease, absorbing Data Science concepts into your mind will innoculate you against anti-vaxer memes.
You'll see the world through new eyes that can see patterns in everyday events.
And you'll use those patterns to make smarter decisions.
You'll be able to predict outcomes much more easily and accurately with the tools you learn in this course.
And your clever insights will make you more than just a cocktail party hero.
You can be a healthcare hero if you go into digital health.
With these insights and skills you can save lives.

:::





====================================================
====================================================
====================================================
====================================================
FROM LO








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





