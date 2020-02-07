---
title: Statistics
layout: slides
---

# 1: Statistics

<aside class="notes">
    I'm Hobson Lane.
    Welcome lesson three of the Data science for digital Health course at UCSD Extension.
    Today you are going to learn about statistics and probability and how to apply these concepts to data science problems in healthcare.
    </aside>

# 3: Agenda

What is statistics and probability?
Descriptive statistics
Probability distributions
Distribution parameters
Prescriptive statistics
Accuracy
Bayes Rule

<aside class="notes">

    Today you are going to add to your statsitics and probability toolbox.
    Data science is mainly just applying statistics to historical data or natural experiments.
    You will use the principles of statistics and probability to answer questions about that data.
    I'm not going to try to squeeze a semester of statistics and probability into a single lesson.
    Fortunately much of the discipline of statistics, as it has been applied to data science has been simplified and reimagined over the past years by people like Judea Pearl.
    And the jargon of statistics is not helpful when you are talking to patients or managers in a healthcare organization.
    You will only need to grasp the core principles of statistics and be able to recognize the terminology relevant to data science so you can collaborate with other statisticians and data scientists.

    You will first learn about what statistics are and the difference between descriptive and prescriptive statistics.
    You will see how descriptive statistics can help you understand the frequency of random events.
    You will be using descriptive statistics as you are getting to know a dataset.
    This is the bulk of what you will learn in this lesson because it is the first thing you will do with any new dataset to explore and get to know it.

    You will also learn about prescriptive or inferential statistics.
    This will help you build a predictive data science model that you can use to improve business performance or outcomes in healthcare.
    Most importantly you will start to build your Spidey sense for "Lies, damned lies, and statistics".

    Our brains did not evolve to compute statistics accurately, they evolved to survive in a dangerous world.
    Cave men and women made reliable predictions and decisions about what to do in split seconds when confronting a wildebeest.
    As a data scientist you will have days if not years to make accurate decisions not only for yourself but for millions of others relying on your data and your model.
    So in this lesson and throughout this course you will gain an intuition for lies of statistics that cloud our judgment.
    This will give you x-ray vision into the core of what makes the world work, the true drivers of disease and human behavior.
    You will be a sage among the cavemen around you.
    </aside>

# 3: Statistics

Describe a set of numbers in a dataset
Describe probabilities outside the dataset
Probabilities used to infer properties about the world
Probabilities used to predict the future
Probabilities used to prescribe actions in the world

<aside class="notes">
    So what are statistics?

    Statistics are just numbers about other numbers.
    Statistics are numbers that summarize a larger set of numbers called a dataset.

    And sometimes these summaries can help us infer information about the real world.
    You can observe a coin flip or a die roll for several flips or tosses, and then you can use what you learn to infer the probabilities for each side of the coin or dice turning up.
    And you can use this to predict the next coin flip or the next roll of the dice.
    Most importantly you can use this to predict how predictable the coin flip is, how accurate your coin flip predictor is going to be.
    This is called the confidence interval for your prediction.
    Obviously you are more interested in predicting the health and efficacy of the red pill vs blue pill, but the coin flip analogy is where you will start your statistics journey.
</aside>

# 4: Probability

How often an event will happen among a set of trials
Inherently binary (coin flip)

<aside class="notes">
    To calculate the probability of an event, we count up its frequency or number of occurrences.
    We divide events into bins or categories based on which of those bins those events match.
    We think of events as binary.
    Either the event happened or it didn't.
    So we'll first start with an event that you've probably seen a lot of, a coin flip.
    The event we care about in our binary world is whether the coin came up heads or not.
    A coin either lands with the heads side facing up or it does not.
    If we have a really thick coin and it sometimes lands on it's edge we'd need to add another binary class to evaluate whether it landed on its edge or not.
    We can go from observations of a coin to infer properties about that Probability.

    So we might observe 10 coin flips and get 7 heads during those trials and infer the probabilty of heads as 7 over 10 or .7 or 70%.
    This data story is probably tingling your statistics Spidey sense.
    You probably know that the true probability of a coin flip coming up heads is 50%.
    So our inference from these observations seems incorrect.
    But you will learn in this lesson whether this 70% probability inference that we've made is likely to be lies, damned lies, or accurate statistics that tell us something about the world.
    In fact you'll soon be able to put a number to exactly how confident you should be in that 70% probability estimate.

    We could do the same for the respondents on a True/False question or we could define true and false as being correct or incorrect.

    Or we could use the numbers 0 and 1 to represent our binary states so we can do math on them like for a linear regression on a binary gender category.

    And we could use a binary variable to represent the colors or two pills that we have to chose from to help us escape from The Matrix.
    Seriously, drug trials are sometimes constructed with a binary feature for the treatment and control groups.
</aside>

# 5: complementary rule of statistics

- Heads
- True
- 1
- red pill

<aside class="notes">
    Binary probabilities are complementary.
    This means we can calculate the probability of heads even if we don't know or don't pay attention to the occurrence of heads on the coin flip.
    We only have to pay attention to one side of the coin.
    We could pay attention to the tails side and count how many times it comes up.
    Then we can use this first bit of statistical algebra that you will learn here.

    The probability of a binary event is equal to one minus the probability of the opposite event.
    This is called the "complementary rule" of statistics.
    So the probability of heads is 1 minus the probability of tails.
    So in the previous example we would have had an easier time counting up the 3 occurrences of tails in our coin flip experiment.
    But we would still know the probability of heads by subtracting .3 from 1 to get .7 or 70%.
    And the opposite also works.
    If we already know that the probability of heads is 70% we can subtract .7 from 1 to get .3, the probability of tails coming up on this coin.

    Likewise the probability of True is 1 minus the probability of False.
    The probability of 1 is 1 minus the probability of 0.
    And the probability of red is 1 minus the probability of blue.
</aside>

# 6: Binary = Mutually Exclusive

<aside class="notes">
    The complementary rule of statistics relies on the definition of binary events, that they are mutually exclusive, or complementary.
    This means we only need to pay attention to one side of a binary event, as the two possibilities are mutually exclusive.
    We only have to pay attention to one side of the coin.

    The probability of tails is merely 1 minus the probability of heads.
    Likewise the probability of True is 1 minus the probability of False.
    The probability of 1 is 1 minus the probability of 0.
    And the probability of red is 1 minus the probability of blue.

    But what about that edge case we talked about with the coin landing on its edge?
    The way we deal with that in data science and machine learning is to create another binary class for this "edge case".
    For a coin we might even name this new binary variable "edge" or "is_edge".
    This allows us to fully specify the 3 possible states of the coin toss with 2 binary variables.
    In general you must create at least N - 1 binary variables for each categorical variable with N possibilities.
</aside>

# 7: Binary Dice?

<aside class="notes">
    Machines think and learn in binary.
    So for machine learning and data science models you want to represent categorical variables in binary form, 0's and 1's.
    But how do you create binary dice?
    Imagine you are creating a data science model using a variable that has 6 possible states, like the sides of a die.
    Technically this is an ordinal variable and could be accurately represented with the discrete integers 1 through 6.
    However it's often much more convenient in machine learning and deep learning models to represent it as a *One-hot* vector with one dimension for each of the 6 possible values of a die.
    In fact, this is the only representation that can be guaranteed to take maximum advantage of all the information in each of these categories.
    This allows our data science model to infer probabilities for each side of the die independent of the others.
    This ensures that our model can deal with "loaded dice."
    The world is full of loaded dice, where the outcome probabilities are not evenly distributed among all the possibilities.
    Probability distributions are rarely uniform.

    You can think of this 6-dimensional binary representation, or one-hot encoding, as the answer to six independent questions:
    "Is it a 1?" "Is it a 2?" "Is it a 3?" "Is it a 4?" "Is it a 5?" and "Is it a 6?"
</aside>

# 8: Ordinal Dice?

- 1, 2, 3, 4, 5, 6

<aside class="notes">
    Some of you may be saying to yourself, "But wait, all the dice in my toy box are fair."
    "Each of the sides of my dice are equally likely."
    And the value of each possible die roll in your game may be linearly increasing from 1 to 6.
    Now I would encourage you to still use the one-hot encoding or binary representation of these values.
    But technically this is indeed an ordinal variable and could be represented in yoru data science model with the discrete integers 1 through 6.
    Nonetheless you will run into problems where this trips you up.
    Your metaphorical dice will be loaded or have edge cases that you haven't considered.
    Treating all your ordinal variables as categorical variables with binary one-hot-encoding will help you avoid these confusing and hard to diagnose errors in your model.
    Once you've experienced as many of these insidious errors that have cost you days or months of time and effort, I'm sure you'll come around to this approach.
    Let your data do the talking by giving it as much freedom as possible.
    Ordinal representations impose your view of the world on the data.
    And that view is often incorrect.
    The data will often surprise and delight you if you let it.

    So just say NO to ordinal representations like 1, 2, 3, 4, 5 and 6.
    Say yes to binary representations of both categorical and ordinal variables.
</aside>

# 9: Dice Probability

<aside class="notes">
    When you know a little bit about the problem you want to solve, like predicting a die roll, you can short circuit the entire data science process using statistics.
    If you enumerate all the possibilities, and you know the distribution of probabilities between them, you can calculate the exact probability for each possibility.
    In the case of dice we know that a fair die follows a uniform or even distribution between each of the 6 possible values on the faces of the die.
    So for a 6 sided die, the probability is 1/6th for each possible value 1 through 6.

    Things get a little more interesting if you combine the probabilities for two dice and consider your new outcome to be the sum of the values on each die.
    The probability distribution for the outcome or sum is no longer uniform.
    To compute the probability distribution we need to enumerate all the possible outcomes for both dice.

    This table shows that enumeration for the first few small values in the probability distribution graphic of red and orange dice on the right.
    Start at the top row to calculate the probability of "snake eyes" or two ones.
    There's only one way for us to roll a two on a pair of dice.
    So one out of six times we will roll a 1 on the first die.
    And one out of six **of those times** we will roll a 1 on the second die.
    That's the key.
    When you realize that we have to get lucky on one die and then get lucky on the second die both at the same time you realize that out of all 36 rows in this table only one of them contains a sum of 2.
    This means that we have a 1 in 36 chance of rolling two ones or "snake eyes" on a pair of dice.
    And you've probably noticed that 1/6th times 1/6th is one out of 36.
    So whenever you know the probabilities for two independent events you can calculate the probability of both of them happening by multiplying the probabilities together.

    That takes care of multiplication, but what about addition?
    So when should you **add** two probabilities together?
    Take a look at the next two rows in our table of possible die rolls.
    In this case you know the probabilities of two independent events, the probability of rolling a 1 then a 2 and the probability of rolling a 2 then a 1.
    But these two independent event have the same total sum and the same outcome in our game.
    So when two probabilistic events have the same effect we can add them together to calculate the total probability of that event occurring.

    Looking at this histogram, can you see why the number 7 is often considered lucky?
    This concept of "lucky 7" came about before many people playing the dice game called "craps" understood statistics.
    Now that you do, you will be able to see why the house always wins in the long run at the craps table.
    </aside>

# 10: Categorical Probabilities

<aside class="notes">
    What do you do when you have many categories
    Can you extend your understanding of dice game probability to the realm of machine learning for categorical probabilities?
    Well you now know the right way to calculate the probability or frequency of cats and dogs photos.
    And you might even be able to guess how we'd extend our probabilities to include other categories like "Fox" or "Other".
    You divide your problem into many small binary questions that to ask your machine learning model.
    And this approach works even for more challenging applications like asking the machine to classify tissue X-rays or images as "Malignant" or "Benign".
    We use probabilities in this situation as estimates of our confidence in the model's prediction or diagnosis.

    And the complementary rule of probability tells us that if we know the probability or confidence for all the different possible diagnoses, they must add up to 1.
    So the confidence our model reports for an image being benign plus the confidence of it being malignant, plus the probability of if being healthy tissue, plus the possibility of it being something unlike human tissue, that total probability is one.
    The "unknown" category is to allow for real images of things like prosthetics and internal fixation.
    </aside>

# 11: Die Statistics

<aside class="notes">
    Your newfound understanding of probability will now give you an appreciation for the statistics we use to describe those probabilities.
    You will also learn about probability **distributions** that show you the probabilities for events in a particular dataset or experiment.

    For example, when we roll a single die, we can describe the probability distribution of possible outcomes in several ways.
    We can count up each of the outcomes in 1000 rolls of the die and plot the discrete distribution of values like is shown here on the right with the blue rectangular bars.
    You divide that count by the total rolls or total number of possible outcomes to get the probability for each of those discrete events.

    You can also draw a smooth continuous curve through each of these probabilities.
    This isn't an accurate representation of the real probabilities it's just an abstract representation that we can use for much more continuous problems. As you'll see in subsequent slides.
    For now just know that you can calculate things like the average or mean die roll of 3.5 and the min and max and other statistics, just like you would for a continuous number for the outcome.

    In the next slides you'll see how extend this concept of histograms and distributions to 2 dice.
</aside>

# 12: 2 Dice Statistics

<aside class="notes">
    Consider the 2 dice problem we talked about before.
    Do you remember the discrete probabilty distribution graphic?
    We computed that directly from what we know about probability.
    Well here we are just showing the counts of an actual dice rolling experiment.
    You can see that the probability distribution in blue on the right looks a lot like the theoretical probability you calculated in the graphic earlier.
    It looks like tall isoceles triangle or the steep roof of a house.

    Now the range of possible values is getting larger, almost double, from 6 possible outcomes to 11 possible outcomes.
    So our discrete experiment is starting to look a bit more continuous.
    And our continuous probability density estimate is looking more reasonable, less uniform and more like a bell curve.
    A bell curve may be what you normally think of when you think of a probability distribution.

    And actually, if you continue this experiment to many more dice, the probability distribution will eventually approach the gaussian or normal probability distribution shape.

    </aside>

# 13: 3-dice statistics

<aside class="notes">
    Here you can see what happens when we add a 3rd die to our game.
    When we sum 3 dice together we now have 16 possible outcomes.
    Now these descriptive statistics on the left are becoming more useful.

    What do you think the "luck 7" dice roll is now?
    It's not seven.
    You can see that our probability estimates continue to grow as our outcome variable increases above 7.
    The probability of rolling 7 is about 5% and the probability of rolling an 8 is about 7%.
    And if you look at the peak of the discrete probability distribution, you can see that the maximum probability occurs at a value of 10.
    The location of the peak of a probability distribution is called the "mode" of the distribution.
    And the probability of rolling a 10 in this 3 dice game is about 13%.

    If you continued this experiment to more dice you would see that the distribution would eventually approach the shape of the continuous normal distribution or bell curve.
    This phenomenon, is called "The Central Limit Theorm."
    When you add many distributions or histograms together they will create a Gaussian or normal distribution, no matter the shape of the distributions you started with.
    **We** started with a very square distribution, the uniform distribution.
    And yet we ended up with a nice smooth bell curve after adding only 3 of these uniform random variables together.

    The python packages called `numpy` and `pandas` are what you will use to calculate these statistics and plot these curves and histograms.
    These are the descriptive statistics that will be most valuable in understanding a new dataset.
    The mean will give you a feel for where the center of the distribution is.
    The mode will tell you what the most likely value is.
    The standard deviation will give you a feel for the spread of the data.
    The min and the max will tell you the exact boundaries of the values that exist in your dataset.

    These are called descriptive statistics because they describe your data.

    </aside>

# 14: Mystery Dataset

<aside class="notes">
    Now imagine you have been given a new mysterious dataset.
    You want to explore it and try to understand its statistics.
    You notice that it has 3 columns of data, x, y, and a binary categorical variable.
    So this is actually three potential statistical variables.
    But it only makes sense to plot the histograms of the continuous variables x and y.
    So you start with the x variable.
    There are a small number of events shown in orange for one of the binary categorical values.
    And there are a larger number of events or data points shown in blue.
    This is a common way to display distributions when you have two classes or a binary categorical variable.
    You use python to quickly calculate some descriptive statistics to help you understand the data.
    But this doesn't help you much.
    It's still a mystery what this data is all about.
    </aside>

# 15: Scatterplot

<aside class="notes">
    Here you can see a new kind of plot a scatter plot.
    This plot allows you to visualize the statistics of 2 continuous variables simultaneously, one on each axis.

    Perhaps you can see some patterns in the scatter.
    For example, some of the points line up in straight lines.
    You could imagine that these might be people or cars on city streets or some event that tends to occurr on the street grid of a large city.

    Also, there only appears to be one orange point within the larger blue cloud of points in the scatter.
    the other orange points seem to surround the blue points.

    A python command for computing and displaying descriptive statistics is `.describe()`.
    This dataset was stored in a Pandas `DataFrame` and `DataFrame`s all have the method `.describe()` which outputs these descriptive statistics.
    You will learn more python and Pandas in the next lesson when you start using it to solve data science problems.

    The red lines show the minimum and maximum extent computed for the y variable in the orange category labeled
    "P" in the scatterplot legend.

    This visualization and these descriptive statistics are still probably not enough for you to recognize the source of the data, unless you happen to have taken a Data Science course before.
    This dataset is a famous dataset in data science and epidemiology.

    </aside>

# 16: Pairplot Histograms

<aside class="notes">
    You can see the command for creating a histogram here.
    Perhaps the histograms on either side of the scatter plot will help you see some more patterns in the data.

    The mean or average value is also shown here.
    The mean in 2 or 3 dimensions is often called the centroid or the center of mass because it lies at the center of the data.
    If all the points in the diagram represented a quantity of mass or weight, the center of mass of all the points would be located at the mean.
    And the symbol for center of mass is a pie chart with 4 quadrant slices, and is shown at centroid location for the blue points.

    Another clue about this dataset is revealed by this centroid location.
    Did you notice how close it is to one of the orange points?
    The mode and median are even closer to this special orange point.
    You can learn about the formulas for mode and median by reading the documentation within the python packages numpy and Pandas which contain functions to calculate these statistics.

    Perhaps this one point represents something unique and different from the other orange points.
    And perhaps it is in some way the source of all the blue points.
</aside>

# 17: Coordinate frame (representation) matters

<aside class="notes">
    Finally the big reveal.
    Here we've shown how the x and y coordinates are actually rotated relative to another coordinate frame, the one used for a 19th century map of London.

    These data points are from the cholera deaths and water pump locations in London.
    These were collected and analyzed by a statistician and epidemiologist named John Snow.
    Some people think of him as the first data scientist, even though it would be another 100 years before that term was invented in the US.

    The reason why there is an orange water pump near the center of all the cholera deaths is that the water pump handle was an infection vector for cholera a bacterial disease.
    Cholera causes diarrhea and is spread by ingestion of the bacterium in drinking water or by eating with ones hands that have been infected with the bacteria.

    In this case, the bacteria were being transmitted from person to person on the wooden water pump handles as dehydrated cholera sufferers pumped water for consumption and washing.

    The key to making this connection with the street map data is to ensure that both the water pump and death datasets were aligned to the same coordinate frame.
    In addition, the london street map was rotated and scaled to align with the pump data.
    </aside>

# 18: Probability = Prediction

<aside class="notes">
   Often a probability distribution or statistic is all you need to make a prediction.
   In the case of the John Snow Cholera data, the probability distribution of cholera deaths near the central water pump would allow us to predict the death rates at various distances from the centroid.

   So far you've learned about two kinds of distributions.
   The first kind of distribution you learned about was the discrete probability distribution like the one we used to describe die rolls.
   Then you learned a about continuous distributions which can be used to quantify the probabilities of continuous values like the location of cholera deaths in London.

   Finally you learned about how to use these distributions for prediction.
   When two variables are related in this way, where one variable affects the probability distribution of another, that is called a "conditional probability distribution".
   In our cholera example, the distribution of cholera deaths was affected by the distribution of infected water pumps.
   We can say that the oval probability contours in this plot show us the probability of cholera deaths conditioned on the location of the infected water pump.

   You will see simpler real world examples in later lessons.
   But the key concept to grasp is that a statistic model that predicts something about data is defined by a conditional probability distribution.
   And that distribution can be used to make predictions.

   This is what you call predictive statistics, or inferential statistics.
   Inferential statistics help you infer or predict something about the future or other parts of a dataset.
</aside>

# 19: Distribution shapes

<aside class="notes">
You have also learned about two basic shapes of probability distributions: the uniform distribution, and the Gaussian or normal distribution.

The uniform distribution is used for any variable that has hard limits on its maximum and minimum values and the probability of the possible values within that range remains the same no matter how close to the middle or the min or the max a point is.
The probability is uniform across the entire range of possible values.
In the case of die rolls, the probability is the same for all 6 possible die rolls, assuming a fair die.
An example of a continuous uniform distribution is given near the beginning of _The Book of Why_ by Judea Pearl.
In Chapter 2, Pearl describes how the stopping point of a ball on a billiards table is uniformly distributed along the length of the table if it is given a random initial velocity.

A Gaussian or normal distribution is often the best way to describe most continuous random variables in the real world, things like the height and weight of things or organisms.
This is due to a property of random variables that when added together they become more and more normally distributed, no matter what the distribution shape of their individual components.
When you add more and more dice to your dice game, the uniform distributions of the possible outcomes on the individual die get smoothed out.
By the time we reached 3 dice, the shape of the distribution was already approaching the normal distribution.
You could even combine the rolls from a 4-sided die, a  6-sided die and a 20 sided die, as you might in a Dungeons and Dragons campaign.
If you added your dice together and did the experiment many times you would see the Gaussian shape of your histogram emerge.

A Gaussian distribution is defined by two parameters, its mean and standard deviation (or its variance).
The mean is the location of the middle of a Gaussian distribution.
The standard deviation is about a 3rd of the width of the data.
99.7% of the events in a normally distributed random variable will be within 3 times the standard deviation from the mean or center.

A third much less common probability distribution shape is shown here.
It is called the Gamma distribution.
The Gamma distribution is often appropriate when counting things or when your values are bounded on one side, but not the other.
If you have heard of the Poisson distribution, it is a special case of the Gamma distribution.
The Poisson distribution is defined by a single parameter, lambda.
In contrast, the Gamma distribution, like the Gaussian distribution, is defined by two parameters, k and theta.
The k parameter is called the shape parameter.
The theta parameter is called the "scale parameter".
There are additional names and formulas for these parameters, but it is not necessary to understand them.
You will learn how to use the Gamma distribution in future lessons.

</aside>

# 20: Mean

<aside class="notes">
    Now let's do something useful with these statistics.
    You're going to see the formulas for the two most useful statistics.
    You can rely on python to calculate the rest.
    The first, most important statistic, as you can imagine is the *arithmetic mean* or just *mean* for short.
    The mean was first used for astronomy and statistics in 1587 by Tycho Brahe.
    This is around the time that decimal numbers were invented.
    Decimal numbers enabled the concept of an arithmetic mean or average to find application in the real world.

    The mean is the average value of a set of numbers, usually measurements or observations or possible outcomes.
    Normally the mean and other statistics are used to calculate the most likely outcome from a set of measurements or numbers that represent observations in the real world.
    But the mean calculation also works on a set of possible outcomes when you think all those outcomes are equally likely.
    So we can apply the mean calculation to our list of possible dice rolls to make sure our mean statistic tells us the truth, that 7 is the most likely outcome.
    Most dice rolls will output values like 5, 6, 7, 8, and 9.
    Sixes and eights will be more common than 5 and 9.
    And sevens will be more common than than all the other possible rolls.
    This is how it got the name "lucky seven" and it's prominent roll in many dice games.

    Here's the mathematical notation for the mean calculation on any variable x where you have N observations.
    You sum up all the values of the observations and divide by the number of observations.
    This gives you the center of mass of the distribution.
    Most of the observations are likely to be near this value.
    And when you calculate the mean of all the possible dice rolls, you get a value of exactly 7.
    This corresponds to the most likely outcome for our discrete value representing the dice roll.

    As you learn python in the coming lessons you will get comfortable with the expressions shown below the mathematical notation.
    Personally I prefer python expressions to mathematical notation.
    Mathematical notation is often ambiguous, as you've learned in _The Book of Why_.
    There's no symbol in math for many real world math concepts and algorithms like Judea Pearl's `do()` operator.
    And this operator is to the concepts he introduced The Book of Why.

    So here are several ways to use python to compose a set of numbers, one for each pair of possible die rolls and then take their mean.
    These long lines of code is a crash course in several python concepts.
    Don't worry, there's a function in numpy called `mean()` that you can use.
    And you probably won't ever have to create a for loop or list comprehension like we have here.
    You'll usually be interested in the mean of your dataset, not some made up list of numbers.
</aside>


# 21: Standard Deviation

<aside>
    When you learned about the mean in the previous slide you may have noticed that we mentioned that most of the values in your dataset could be expected to be "near" that mean value.
    Now you'll learn what nearness means.
    Perhaps you've guessed that nearness is the oposite of difference or distance.
    So the magnitude of the difference between two numbers tells us how far apart they are.
    The smaller that magnitude the closer or nearer they are to each other.
    Six is closer to lucky seven than five is because 7 minus 6 is smaller than 7 minus 5.
    And the same goes for negative values, we just need to take the magnitude of the difference or the absolute value.
    So 8 is closer to 7 than 9 is because the absolute value of 7 minus 8 is smaller than the absolute value of 7 minus 9.

    The concept of standard deviation was invented much more recently than the concept of mean.
    Karl Pierson used standard deviation and variance in his lectures and papers in 1894 during the industrial revolution.
    Standard deviation and variance are based on the concept of a mean.
    Standard deviation was called the mean error by another Carl, spelled with a C this time, Carl Gauss.
    Carl Gauss used this concept in his development of the normal distribution.
    That's why it is sometimes called the Gaussian distribution or just "The Gaussian".

    If you think about mean error as another name for standard deviation, you can fall back on the formula for Root Mean d Error, or RMSE, or remzee, to help you remember the formula for standard deviation.
    This formula and the formula for mean are the only ones I ask you to know by heart.
    They will come up again and again in everyday life and in healthcare.

    "RMSE" or "Root Mean Square Error" means you calculate the errors first.
    You work your way from right to left to get the order of mathematical operations.
    Error is the last word in RMSE so it's the first thing we need to evaluate in the innermost parentheses of our python code.
    The errors in this case are the differences between all your observations and the mean.
    Then you calculate the square of all those errors.
    After that you calculate the mean of all those squared errors.
    You know how to calculate the mean from the previous slide.
    Finally you take the square root of that mean squared error.
    This gives you a single value for the root mean square error or standard deviation.

    Imagine computing the standard deviation in the 19th century without computers or calculators.
    Try it with me in your head for the simplest possible case of a coin flip.
    We have only two possible outcomes in our experiment.
    We have a 0 for tails and a 1 for heads.
    So lets just compute the standard deviation on the two values zero and one.
    So first calculate the mean of 0 and 1, that gives us one half or 0.5.
    Then let's calculate the errors.
    For the value of 0 our error is zero minus .5 or negative 0.5.
    For the value of 1 our error is 1 minus .5 or positive 0.5.
    Now we need to square both of those value.
    Half of a half is a quarter or .25.
    And this is the same value for the square of both positive and negative .5 so we have two squared errors of .25 and .25.
    Now we take the mean of those two squared errors which gives us a single value of 0.25.
    Finally we take the square root of .25.
    Fortunately we already know the square root of .25 because we squared .5 to get it, so the square root of .25 is .5.
    And this is the standard deviation of a coin flip distribution for zero and 1.


    Now think about the dice problem.
    With the 36 possible dice rolls, it would take a lot of effort to accurately compute the squares and differences required and then sum them up accurately.
    If you do the same for the 11 possible outcomes for the 36 possible dice rolls, you will get a standard deviation of 2.415...
    In the next slide you'll see how to use this to compute confidence intervals, like your confidence in rolling a value of a value between 6 and 7.
    You will even be able to calculate the probability of a dice roll on the edges of the distribution, such as dice that come up with a value below 5 or a value greater than 9.
    </aside>

# 22: Normal (Gaussian) Distribution Confidence Intervals

<aside class="notes">
    Computing confidence intervals is a bit more challenging than computing a descriptive statistic like mean or standard deviation.
    An interval is a region of the number line, like the horizontal axis in these plots.
    An interval is defined by it's left and right boundaries, the min and max values for those boundaries.
    If we can compute the area underneath the probability distribution between those two boundaries that will tell us the probability that any value within that interval might occur.
    under a probability density function or probability distribution tells us how likely a value is to occur within that area.
    For the histograms or discrete probability distributions shown here on the right, this is relatively straight forward.
    Like we did before we just need to add up all the counts in each bar for a region that we are interested in within our interval.

    And for the continuous case, fortunately there is a rule to help us compute the confidence interval for the standard normal distribution or bell curve.
    The rule is called the 68, 95, 99.7 rule.
    The name of the rule contains all the numbers you need.
    For the red confidence interval shown in this plot you can use the first number in the rule, 68%.
    There is a 68% that any random sample will fall within plus or minus 1-sigma of the mean. This is a confidence interval of negative 1-sigma and positive 1-sigma around the mean.
    And there is a 95% chance that a random sample will fall within 2 sigma of the mean.
    This for a mean of 0 and a standard deviation of 1, this means you have a 95% chance of drawing a random sample between negative 2 and positive 2.
    Likewise you have a 99.7% chance of a random sample falling within plus or minus 3-sigma of the mean.
    </aside>

# 23: Accuracy

continuous variable (regression)
RMSE

<aside class="notes">
    In data science the statistic you'll hear about the most is probably accuracy.
    For a continuous target variable, it's not possible to count of the number of test cases that your model predicted exactly correct.
    Your model will almost never be precisely correct for a regression problem where it outputs a continuous decimal value.
    That means you need to compute accuracy based on how close each prediction is to the true value of the target variable for that example rather than whether it is perfectly correct or not.

    Fortunately you do not have to learn any new math to compute this average distance or average error.
    Root mean square error or RMSE or remzee is the standard error formula for a continuous target variable.
    This is the same formula you used to compute the standard deviation on the rolls of pairs of dice.

    This is nice because you can use the normal distribution and the standard normal curve to compute a confidence interval around each of your predictions.
    So let's say you computed the standard error on a test set of data in the weight prediction problem and you got a value of 2.5 pounds.
    And let's say you use your model to predict the weight of someone coming into your clinic and it predicts a weight of 100 pounds.
    You 2.5 pound standard error tells you that you have 68% confidence that they actually weigh 100 pounds plus or minus 2.5 pounds or between 97.5 and 102.5 pounds.
    Similarly, for 2 sigma, or 2 standard deviations, you know that the patient weighs between 95 and 105 pounds with 95% confidence.
    And the 68-95-100 rule tells you that you have 99.7% accuracy that the patient weighs betwen 92.5 and 107.5 pounds.

    This approach to measuring the accuracy of a model has a lot of advantages.
    It's the most common form of accuracy quoted in academic papers and medical equipment ification sheets.
    </aside>

# 24: Categorical Accuracy

discrete variables (regression)
RMSE

<aside class="notes">
    For discrete or categorical target variables the accuracy calculation is even easier.
    For binary predictions like blue pill vs red pill, or 3-category predictions like malignant, benign, or healthy, we can just count up the number correct.
    This is similar to how you would grade a test or quiz in school.
    You divide the total correct by the total number of predictions that you made with the model.
    This gives you a fractional number between 0 and 1 which we usually report in percent.
    So if you gave a radiology model 10 x-ray images of cancerous and healthy tumors, and it correctly classified 8 of them, you would say that your model has an 80% accuracy.
    </aside>

# 25: Bayes Rule

<aside class="notes">
    Finally, my favorite rule in all of statistics, Bayes Rule.
    I like to think of this as the second opinion rule.
    For Baye's Rule, the second opinion is from a diagnostic test or machine learning predictive model, not necessarily a real doctor.
    Bayes Rule tells you exactly what to do when you make predictions and you want to update your estimate of the target variable based on new information.

    For example, Bayes Rule tells you the best way to interpret a new blood test result to combine it with previous blood tests and diagnoses.
    Let's say you have a patient, and based on their demographics you think there is a 25% chance that your patient has type 1 diabetes, based on their age and demographics.
    Then let's say you run blood test that has 80% accuracy on people with diabetes.
    This is a little different from the radiology model in the previous slide because this is the true positive rate only on those people with the disease.
    We call this precision rather than accuracy.
    This 80% probability is called precision, because it is the accuracy only on a subset of the data, the patients that truly have the disease.
    This is the probability of a positive test result T given the patient has the disease D.
    In mathematical notation this is P of T given D.

    Now, imagine your blood test comes back positive.
    A positive result means that the blood test is indicating that your patient has type 1 diabetes.
    But a blood test is not the final word.
    As a Doctor or Data Scientist you can use Baye's rule to combine those two 3 probabilities together to create an estimate of the likelihood that the patient actually has diabetes.
    Bayes rule says that the probability of disease D given a positive test result T is equal to the liklihood ratio times the original probability that they had disease before you had the blood test results.
    This probability of disease that you knew prior to the blood test is called the prior probability.
    In your case this is 25%.
    Prior to the blood test you were 25% confident that the patient had diabetes.
    The likelihood ratio is the probability that the test will indicate a positive result given that the patient has the disease divided by the probability of the test giving a positive result on a random person from the population with similar demographics to your patient.

    For Bayes rule we need to divide this by the probability of the test returning a positive result, or P of T.
    To get the likelihood ratio we need the probability of the test returning a positive result on all patients from our patient's demographic cohort (age, gender, height, and weight).
    This is tricky to calculate, but we can estimate it from the weighted average of the precision of the blood test and the false positive rate.
    False positive rate is the rate your blood test will sound the alarm by returning a positive result when the patient does not actually have the disease.
    You can assume that the false positive rate for this particular test is 10% and that 25% of your patient's cohort have the disease.
    So for this example the probability of T, the total positive rate of the test, as .25 times .8 plus .75 times .1 which gives .2 plus .075 or .275.
    Your test has a 27.5% chance of returning a positive result on a random patient with your patient's demographics.
    So your liklihood ratio is .8 divided by .275 which is 2.9.
    Multiplying 2.9 by .25 again to get .727272 and so on, or about 73%.
    Depending on the risks associated with your intervention, you may want to have your patient take another blood test to increase your confidence in the diagnosis.
    So when you apply Bayes Rule, you will often get reduced likelihood of a disease if you account for the false positive rate of the test correctly.
    And this can lead to better outcomes, particularly when interventions carry significant health risks, as they do for type 1 diabetes.

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

# Accuracy

- Continuous numerical predictions (regression):
    - How close to correct are your predictions

<aside class="notes">
    One statistic that you've likely encountered in your daily life is accuracy.
    In the past you've probably used the word accuracy to describe how close your measurements are to the truth.
    In Data Science and Machine Learning we also often talk about the accuracy of a model.
    So in this case your measurements are the predictions that your model makes.
</aside>

# Backup Agenda

# Topic Checklist

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
- real world example of bayes rule

## References:

[wiki/Iron_Ring](https://en.wikipedia.org/wiki/Iron_Ring)UC
[wiki/Osteopathic_medicine](https://en.wikipedia.org/wiki/Osteopathic_medicine_in_the_United_States)
[wiki/Primum_non_nocere](https://en.wikipedia.org/wiki/Primum_non_nocere)
