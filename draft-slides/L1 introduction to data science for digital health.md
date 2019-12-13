---
title: L1 Introduction to Data Science for Digital Health
created: 2019-12-11
---

# big picture to microscopic

- Pop Health
- Hospital
- Doctor
- Patient
- Diease
- Microbiology

::: note
We're going to apply data science and digital health to big picture applications first before diving into the nitty gritty details of more focused specializations.
We'll start with pop health, calculating statistics about the health of populations.
We'll then dive progressively deeper into the healthcare system by examing the performance of individual insurers and hospitals and ultimately individual providers or doctors.
Finally, with clinical health you will learn how to model diseases and make diagnoses with data.
And this will require us to dive even deeper into microbology and the genetics of disease.
:::

# general to specific

- Philosophy (general principals)
- Theory
- Examples
- Skills

::: note
Within each module you will first learn the history and philosophy of data science and healthcare relevant to the topic you are learning.
You'll learn about things like the Iron Triangle of Healthcare.
Data scientists like you are trying to stretch the iron triangle so that Healthcare Cost, Quality and Access are no longer rigidly tied together in a zero sum economic system.
Then you'll dive into the particular theories or models about biology and statistics that will give you the foundation you need to understand the "why" behind the data science algorithms.
And each module will include many concrete examples to anchor your understanding.
And you will practice the skills of the module on these examples to help you develop habits and ways of dealing with data that you can apply to similar problems you encounter outside of class.
:::

# skills-based approach

- Loading data
- Types of data
- descriptive statistics (count, dimensionality, mean, standard deviation, cardinality, entropy, correlation)
- Cleaning data (missing values, outliers)
- Visualizing data
- Transforming data (scale, limit, logarithmic, back difference, pca, tsne)
- Modeling data (linear regression, logistic regression, decision tree, random forest, boosted trees, neural networks)

::: note
So this course will start with the foundational skills you need.
For example you will build on your existing understanding of math and spreadsheets to extend that to doing data science entirely in a spreadsheet.
You'll quikcly see the limitation of the spreadsheet as a data science tool and this will motivate your eagerness to move on to more programatic approaches to data science.
You'll learn how to write small python programs that automatically accomplish everything you learned in the spreadsheet exercises, and more.
You'll progress from descriptice statistics, to data cleaning and transformation, and finally into data modeling.
:::

# Loading data

- text files (CSV, TSV, JSON, TXT)
- compressed files (ZIP, GZ)
- binary files (XLS, PDF, Images)
- web pages (links to HTML)
- databases

::: note

The first bit of python magic you'll learn is how to load data.
It will feel like casting a spell each time you give python a command and it goes out onto your hard drive or the web and retrieves whatever you're looking for.
You'll start with files that you've probably seen before, like text files and CSV files (comma separated values).
You'll learn how to automate the reading and cleaning of those files using python, so you no longer have to spend your days scrolling through massive spreadsheets of numbers.
This will be your first chance to see the power of python to do data science.
No longer will you be limited to the files you can import into Excel
:::

# Data types

- numerical
- categorical
- time series
- natural language
- sequence
- imagery

::: note

Throughout the course you'll incrementally learn about various data types.
You'll learn to perceive numbers and text as data the way a data scientist views data.
This will help you see how a particular dataset can be used for data science.
You'll soon be able to see how each variable or dataset can fit into a data pipeline.
You'll learn to load and manipulate the most straightforward data types first.
Numerical data is what machines were built for. So you'll start there.
Categorical data may not be as obvious to you. So you'll build your understanding of various kinds of categorical data as you progress through the modules.
You'll work your way from categorical data into time series data where your intuitions about dates and times will be useful in extracting both categorical and continuous numerical data.
From that foundation you'll dive into sequences of words and characters that humans read, called natural language.
Machines can extract data and information from lengthy clinical medical records or technical documents and summarize or plot it in ways that will help you glean actionable intelligence or knowledge from those documents.
And those sequences will incrementally become less and less comprehensible by humans as you learn how to use machines to process longer and more complicated sequences of data like DNA and the human genome.
Finally you'll eventually put on your radiology hat as you examine X-ray and MRI imagery and even cell phone camera images of patients.
You'll learn how to train a machine to see things that a human doctor might miss.
:::

# Exciting applications

- Pop health (Population Health)
- Epi (Epidemiology)
- Virtual assistance (Lifestyle support)
- Disease trigger detection
- Personalized medicine

::: note
Some of the most exciting oportunities for Data Science and Digital Health are in your personal life.
The two biggest applications of data science in industry have previously been advertising and finance.
These tools for measuring, influencing and predicting the sentiment of customers and markets can be repurposed for good in healthcare.
Just as quants (quantitative financial analysts) use data science to predict markets you can predict the spread of disease and time your investments in your own health.
Just as advertises have built adwords campaigns and chatbots to influence your behavior, you can build your own assistant to influence your decisions for more positive outcomes for your health and the health of those around you.
and predicting the future of financial markets.
This democratization of Data Science technology is driving an exciting trend in healthcare, personalized medicine.
Whole companies have been formed ot help people with rare diseases, diseases ignored by the insurance companies and healthcare providers.
With personalized medicine, innovative companies can now read your genome and your health history and use information about your particular situation to help you in particular.
And this is all made possible by the automation that data science provides.
A doctors' time is expensive.
In comparision, a computer server's time is virtually free.
That's why WebMD and various nursing chatbots are free and open to everyone around the world.
In fact, this automation has reached such a high level or meta, you will learn in this course how install and configure a nursing virtual assistant on your laptop.
This nursebot can help you monitor your own health and help you predict and mitigate any future health risks.
If you asked your doctor to read your entire clinical medical record in detail and correlate that with the 30 thousand genes that define the architecture of your body that would be very expensive.
In the past, that clinical medical history was not even obtainable.
For the younger of you, you may soon be able to find all of your medical records in one place.
I don't even think your insurance company or a doctor would even entertain that idea, unless you agreed to a pretty large cash payment up front.
You will read that same data into the python programs your will construct in this course to visualize and glean insight for free.
:::

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

::: note
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
