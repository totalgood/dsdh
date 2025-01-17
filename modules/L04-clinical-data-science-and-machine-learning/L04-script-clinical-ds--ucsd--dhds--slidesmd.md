# 1: Clinical Data Science

<aside class="notes">
    Welcome to lesson 4 in the data science for digital health course at UCSD Extension.
    I am Hobson Lane.
    Today you will be learning how to build clinical data science models.
    By the end of this lesson you will be able to use python and data science to predict a patient's likelihood of developing diabetes.
    </aside>

# 2: Agenda

- Data Privacy Environments
    US: HIPAA
    Europe: GDPR
    PII and Privacy
    Developing Countries
- Clinical Machine Learning
    Pandas
    Scikit learn

<aside class="notes">
    The first word and the first consideration in any data science project is the data.
    So you will first look at the kinds of clinical healthcare data available to you in three environments.
    The US and Europe are becoming more and more similar in terms of the kinds of data that are available and who can access it.
    Developing economies and rural areas often offer reduced data privacy to their citizens and reduced intellectual property protection to pharmaceutical companies.
    So you will learn about some of the unique clinical data science approaches and services that are possible in these regions of the world.

    Once you have explored some clinical data resources and regulations you will then learn the science part of clinical data science.
    Clinical data is data about individual clinical patients.
    Usually this data is stored in a table within a database or a computer file.
    Your first clinical data set will be a tabular record of blood tests and vital signs for diabetes patients.
    Your model will predict the severity of each patient's diabetes over subsequent years.
    You will download a file from the Internet and load it into a python table called a DataFrame.
    You will explore that data by plotting some of it with one of the most useful plots in data science, a scatter plot.
    Then you will train a model to predict diabetes severity for these patients.
    </aside>

# 3: Clinical Data

Quantity
Quality

    <aside class="notes">
    Healthcare is funded in different ways in the US, Europe, and in developing economies.
    This leads to varying degrees of data quality, quantity, and availability.
    In the US, to gain access to protected data you must comply with HIPAA regulations.
    HIPAA is the Healthcare Insurance Portability and Accountability Act.

    In Europe and soon in the US there is GDPR, The General Data Protection Regulation.
    In most if not all European countries, private healthcare is the exception not the rule.
    HIPAA regulations in the US and GDPR regulations in Europe determine how organizations protect and disseminate data.
    In addition, websites and mobile apps often have EULA (End User Licence Agreements).
    These are the checkboxes and buttons you click to "Accept" and gain access to networked apps like for your social media accounts, or wearable device.
    These devices and apps are not only tracking your cute photos of puppy dogs, but also your vital signs, workout sessions, sleep, psychological profile, and other indicators of your health and wellbeing.
    Your apps know more than your doctor does.
    If you're like most people, you don't read these agreements.
    Nonetheless, they protect US and international corporations from lawsuit when user data is used within those corporations to make money with advertising or predictive models about your health and behavior.
    There are famous cases of national mail-order retailers unintentionally informing parents of their daughters' pregnancies through advertising campaigns and mailers.
    The Internet or The Cloud provides a wealth of data to the corporations that maintain the servers that store the data.
    Data scientists in those organizations know more about you than you or your family does.

    Things are different in regions of the world where healthcare data is not horded by corporations.
    In Europe, under GDPR, every citizen owns their own data and healthcare a universal service or right, like water, highways, or the Internet.
    This means that that healthcare providers in Europe are more likely to be willing to share their data with each other and with researchers.
    In Europe your healthcare data is not the intellectual property of corporations.

    As a data scientist you will notice significant differences in the data quality, quantity, and availability depending on the regulations that govern the healthcare system.
    And you will also notice significant differences in the data available to you if you work for a large pharmaceutical company, a university, or a government institution, compared to when you are accessing the data for your own personal use or education as you are now.

    In this course you will be using clinical health data that is publicly available.
    This data was gleaned from widely studied academic datasets so you can compare your results to those of experts.
    Though the data quantity may be limited compared to what you will find inside a large corporation, the data science approaches and techniques are the same.
    You will start small, with a dataset for only 400 patients.
    </aside>

# 4: Centralized US Data Resource (CDC)

<aside class="notes">
    In the US, the CDC or Center for Disease Control maintains large databases of healthcare data for US citizens.
    These databases largely focus on the data most useful for epidemiology.
    And this data is aggregated and anonymized to hide the identity of the individuals whose health information is recorded in these databases.
    Nonetheless pharmaceutical companies and healthcare data scientists are often able to use this dataset to train their clinical data science models.

    These datasets include statistics about mortality rates and causes of death aggregated across cities, states and regions of the US.
    Nutrition data from the FDA and Midicare/Medicaid and welfare programs are often collected within the CDC servers.
    You can access ambulatory care or outpatient data at this ftp server for the CDC as well.
    Health insurance and hospital statistics are also available here.
    And due to lawsuits and regulations around tobacco and alcohol use in the US, you will find significant information about these addictive products within the CDC databases.
    </aside>

# 5: EU and EEA Maps

<aside class="notes">
    The European Union (or EU) and the European Economic Area (or EEA) are governed by the GDPR and other healthcare data regulations that govern how personal data can be shared.
    From a data perspective this means that you can often gain access to datasets from Europe that cover a wide range of healthcare systems.
    And these systems serve patients with a greater diversity of ethnic backgrounds, cultural norms, and religious practices.
    Many cultural practices have a significant impact on food preparation and exposure to disease and toxins like alcohol and tobacco.
    With the Wuhan corona virus, we've seen how the cultural norms around eating exotic wild animals can dramatically affect human health.
    Similarly, as you learned previously from John Snow's research in London many epidemics and healthcare crises have been traced to cultural norms and public services like water and sewage.
    As a data scientist working with data from Europe, this diversity of regulation and cultural norms enables you to more easily account for more variables that affect clinical outcomes.
    This can often lead to more effective clinical healthcare data science models.
    </aside>

# 6: Data in Europe

EU Map
WHO Interactive Data Browser

<aside class="notes">
    The WHO (World Health Organization) in Geneva Switzerland provides an interactive gateway to a large repository of clinical healthcare data.
    Because of GDPR and greater uniformity of regulation around healthcare data, much of the WHO data comes from Europe.
    The WHO gateway to EU data is interactive and allows inexperienced data scientists to explore aggregated data with scatter charts, bubble charts, line charts and maps.
    It's possible to visualize up to 4 dimensions at once with time or year as the 4th dimension of your animation.
    In this plot, which required 4 mouse clicks, you can see an animated "chloropleth", or colored map, of beer consumption rates in Europe.
    Czenia apparently has this highest consumption rate, 7 liters of equivalent pure alcohol consumption per person per year.
    In Ireland, the second highest alcohol consumer, the rate is 5 liters of pure alcohol per person per year.
    Mortality and death rate statistics for these countries reflect this unhealthy alcohol consumption rate.

    The WHO chart dashboard is interactive.
    So the user can mouse-over any individual bubble or location on the map to see detailed numerical data.
    The chart is also dynamic, it can be animated to show the changes from year to year using the play button at the bottom.
    The chart uses a javascript library called d3.js to allow this rich interactivity.
    You will learn more about d3.js as you use it to generate your own rich visualizations using plotly.
    </aside>

# 7: UK Hospital Data

<aside class="notes">
    In Europe it's often easier than in the US to retrieve detailed up-to-date data on patient care aggregated for individual hospitals and clinics.
    Here on this you can see a listing of all the hospitals in the UK and the aggregated discharge data or hospital episode statistics (HES) for each.
    This data can be used for epidemiology and healthcare system performance optimization, but not clinical data science.
    Clinical data science requires data on individual patients.
    If clinical medical records are not available, you need admission and discharge data on an individual patient-by-patient basis to normalize for confounding variables in you models.
    As a data scientist you would like account for individual patient variables such as treatment history, blood test results, biometric data or even just detailed demographics like age, gender, ethnicity, residence and workplace geographic information like postal code.
    As in the US, academic researchers must request access to patient records from the custodian of the data, usually another researcher who has acquired data from hospitals and government agencies.
    Individuals without an associated university or governmental organization and e-mail address generally are not allowed access to individual patient records, even when anonymized.
    </aside>

# 8: d3.js and Plot.ly

<aside class="notes">
    After perusing all thes mind-numbing tables of data you might be ready for a serving of eye candy from the d3.js visualization library.
    Even though d3 is a javasript library, you don't have to know javascript to create these informative interactive visualizations.
    You can use a python package called `plotly` to generate these graphics for you.
    It works just like `seaborn`, the main python package you will use for visualization in this course.
    All you have to do is give plotly your data and then select and configure your plot with python commands.
    Plotly will create data-driven interactive visualizations to help you and your patients understand data in a richer way.
    Your takeaway from this should be to use the keywords "d3" and "plotly" in your duck.com searches for visualization ideas.
    Not only will you get inspired by new ways to look at your data, you may find code you can just copy and paste to create those visualizations for yourself.
    </aside>


# 9: PII

Examples
Full name
Birthdate + hospital/doctor/neighborhood
Hospital + age (if over 80)

<aside class="notes">
    PII (or Personally Identifiable Information) is defined as "Information like birtdates, names, and social security numbers which can be used alone or in combination with other pieces of information to identify an individual."
    This definition is maintained by NIST in the US (the National Institute of Standards and Technology).
    This is the same
    In western countries PII is protected.
    This prevents others from exploiting your data to discriminate against you or harm you.
    Why would anyone do this?
    PII is extremely valuable, not only to criminals and fraudsters and identity thieves.
    It's also valuable to corporations.
    Theres a reason why grocery stores and drug stores give you a discount when you share PII with them.
    Whenever you make a purchase and hand over cash along with your shopping card or telephone number, you are paying twice.
    Your data is very valuable.
    And it is doubly valuable if it is attached to PII which allows data scientists to deduplicate data and ensure that store database records represent the real world statistics accurately.
    It also allows data scientists to join or merge or combine records in multiple tables together to create a rich profile of customer health and behavior.
    You will see this in your clinical data science work.
    You will often think of new variables you would like to have about your patient.
    But when you are using a dataset from academia or another public source you will not have PII, so you will not be able to combine tables to create those more accurate models.
    Only the corporations that control and protect PII can do that.
    That is why big tech and big pharma has a monopoly on the most accurate data science models.

    As you become proficient at data science you will soon have the skill to predict a lot of healthcare data.
    This includes not only things like disease diagnoses and the efficacy of drugs.
    You will also be able to infer and predict PII.
    You may be able to de-anonymize data by collating shared characteristics of individuals across multiple tables.
    With enough data, you can train a data science or machine learning model to predict PII like birthdates, names and social security numbers.
    This is why the pairing of an elderly persons age with any geographic information like a city, or hospital name is considered PII that you must protect and not release to the public.
    Because there are so few people over the age of 80 that attend a particular clinic or hospital, it is easy to identify individuals in a database.
    It would relatively easy to identify particular elderly individual based on any small amount of medical diagnoses or vital sign information associated with that person.

    And even when PII pairings like this are protected, it is still possible for data scientists to identify individuals if they have enough data.
    This is what companies like PIPL and Cambridge Analytica do to connect all your social media accounts with public records like property titles, marriage licenses, court records, and even birth certificates.
    You can search PIPL and discover the phone numbers, birthdays, and all the social media accounts of anyone for whom you have some small piece of PII about.
    An e-mail address, postal address, or social media account username is all you need to discover a lot of things about your friends.
    Imagine how much more is available internally to PIPL and Cambridge Analytica employees who can freely and legally share data with each other.
    </aside>

# 10: Anonymization

Delete PII columns/fields
Wait 50 years after individuals die
Add noise to PII
Shuffle PII
Implement Differential Privacy

<aside class="notes">
    Anonymization is what you do when you want to share data with your fellow researchers and data scientists without revealing any PII of the individuals represented in your dataset.
    You have several options and none of them are fool proof.
    The most straightforward approach is to simply delete as much PII as you can without making the data records unusable by the people your are sharing the data with.
    As a minimum you must delete all names and birthdates and ID numbers and contact information like addresses and telephone numbers.
    And as you learned in the previous slide, you may also have to delete some health information like the age and any rare disease diagnoses or rare blood test and vital sign results.
    In some cases pieces of information like age or blood test results may be critical to the data science you and your collaborators are trying to perform.
    In this case, rather than deleting that PII, you may want to add noise to the data.
    For example you could offset all birthdays a random number of days, or you could create arbitrary random names for individuals.
    You can also shuffle the records in your database so that names and ID numbers are associated with incorrect records.

    The concept of differential privacy is an approach to measuring the effectiveness of any anonymization technique, like adding noise or shuffling records.
    The idea is to test your anonymized dataset by removing an individual from it and making sure that the statistics your system reports do not change significantly.
    In a differential privacy system, the difference in the data reported is insignificant when an individual is added or removed.
    But this requires a system that only reports aggregate statistics about your database.
    Aggregate statistics might be things like the average resting heart rate of African American males under the age of 20 in San Diego.
    This can make the data more difficult to work with in a typical machine learning pipeline.

    And none of these anonymization approaches are perfect.
    In most cases, both shuffling and adding noise are not enough and it's much more appropriate to delete the PII.
    Until you have experience deanonymizing data you should not trust yourself to anonymize a dataset.
    Even professional data scientists make mistakes anonymizing data.
    In 2008 University of Texas at Austin researchers successfully deanonymized the Netflix Prize dataset soon after the data was released to the public.
    They were able to identify individuals and create personality and preference profiles by comparing records in the Netflix dataset to the public IMDb database.
    </aside>

# 11: Developing World Data

Hospital
Clinic
In the field
Dr’s office
Home
Community Health Worker
Mobile app

<aside class="notes">
    Privacy regulations and healthcare data access in the developing world is different than the rest of the world.
    Hospitals and clinics in developing countries are sometimes run by NGOs (Nongovernmental Organizations).
    These organizations are often headquartered and operated from outside the country that they serve.
    And ambulatory or outpatient care is often performed in villages, schools, and homes in these remote areas.
    And volunteers serving these communities are focused on the wellbeing of their patients.
    They use the data they gather for the benefit of those communities, like recommending particular hygiene and cooking techniques to minimize food-born illnesses.
    Privacy is not a barrier to data science in regions of the world where data is not used to exploit people.
    These rural and agricultural regions of the world offer fertile ground for a data scientist to gather data and build models that help improve healthcare outcomes.
    This data is doubly valuable because information about these under-served demographic and cultural groups is often not available in the US or Europe.
    </aside>

# 12: Clinical Data Science in Developing World

<aside class="notes">
    Along with the greater opportunities for gathering data in the developing world comes greater challenges in collecting and communicating that data.
    Often a mobile phone is the only communication lifeline between rural parents and their network of healthcare resources.
    An app designed for a mobile phone in this environment must deal with intermittent wireless and WiFi connections.
    And the virtual assistant being consulted during childbirth is not helpful if, like Alexa, it replies with "cannot connect to the internet, try again later."

    Dimagi is a Boston tech company that builds nurse bots or healthcare apps designed for this challenging environment.
    Dimagi's apps are designed to work regardless of a data connection by storing all data locally on the phone.
    Data is synced during the intermittent connections to the Internet available to app user.
    Dimagi, like other NGOs that serve this market, is motived to use data to improve the wellbeing of the patients in the communities they serve.
    They prize the data, not because it is their intellectual property, but because it can hold the keys to saving lives.
    One Dimagi app that uses data in this way is called CommCare.
    CommCare helps mothers monitor and care for their newborn babies as well as their teenage children.
    These chatbots are carefully designed by trained field managers with experience in these communities.
    These app designers are able to anticipate all the various symptoms and crises that a mother in that part of the world will encounter.
    If a child has diarrhea that persists after the app's recommended treatment, the app will continue to recommend treatment while simultaneously arranging an appointment for a community worker to assist the parent.
    </aside>


# 13: US Nurse/Pharma Bots

- pharma **prior**
    - insulin
    - medication

<aside class="notes">
    All of this privacy regulation around PII and healthcare data makes data science in the US different than in other countries.
    In the US, nurse apps and bots would be more accurately called Pharma bots.
    In this example a chatbot by a pharmaceutical company was introduced to a user that wanted to learn more about whether they might have diabetes and what exercises they might incorporate into their daily lives.
    The first recommended therapies and activities that the bot recommended were to question whether they might need to increase their medicine dosage or insulin injection regularity.
    This is clearly driven by an agenda other than patient health.

    During the opioid crisis in the US, pharmaceutical companies were found to have utilized deceptive marketing and sales techniques like this to encourage doctors to prescribe opioids.
    But with chatbots, the channels of influence on consumer behavior are more direct.
    Pharmaceutical company chatbots are often much more sophisticated and effective and influencing patient behavior than those built by nonprofits or governmental agencies.
    This is because the pharmaceutical companies have access to greater resources and data than is often available to smaller nonprofits without a line of pharmaceuticals and medical devices to sell.
    However, these chatbots are becoming surrogate providers in the US, influencing patients to pressure their doctors into providing diagnoses and prescriptions that are beneficial to the company that built the chatbot.
    This enables for-profit corporations to include their corporate financial growth targets into the "objective function" of their recommendation engines and chatbots.
    And because the pharmaceutical company has access to detailed, deanonymized data, they can build bots that are more effective at influencing us.
    For example, imagine your interactions with a bot reveal that your craving for sweet and fatty foods is highest at 3 pm in the afternoon.
    The maker of the bot can use this knowledge to target you with a recommended therapy at that time when you are most vulnerable.
    The data scientist training the bot, might program the bot to recommend you take your insulin shot or diabetes medication in these situations based on the training set that is optimizing for patient relief and pharma  revenue.
    Alternatively the data scientist can program the bot to recommend alternative therapies such as meditation or exercise, if appropriate based on your clinical medical record.
    When there is uncertainty in a diagnosis and therapy recommendation like this, a pharmaceutical data scientist is less likely to be as objective as a doctor.
</aside>


# 14: Clinical Dataset (Diabetes Severity)

<aside class="notes">
    Scientist meet your data.
    Data meet your scientist.
    Here you can see some tabular data gleaned from an academic study of diabetes at North Carolina State.
    The columns of data you will use as your features include, age, gender, BMI (or body mass index), blood pressure and six blood serum tests.
    The final column on the far right is the target variable you would like to predict.
    As with most data science and machine learning problems you will solve, you are given the answer to the predictions you want your model to make.
    You are going to provide these answers to your model to help it find patterns in your features that it can use to predict that target variable.
    This is called a supervised learning problem because you, the data scientist, are supervising the machine learner by giving it the answers to your tests so it can learn from its mistakes.

    The target variable in this case is the diabetes severity score on the far right in bold.
    It is a quantitative measure of diabetes severity, one year after the patient blood tests and vital sign data was gathered.
    </aside>

# 15: Clinical Dataset (Age, Gender, BMI, BP)

<aside class="notes">
    In these 4 scatterplots you can see the relationship between age, gender, BMI (or body mass index), blood pressure and the target variable, diabetes severity.
    Do you see any patterns?
    If you were to manually draw a line through the middle of each of these plots, would it have a positive slope, a negative slope, or perhaps just a horizontal line with a slope of zero?
    To my eye the slope on age and gender would be about zero.
    There doesn't seem to be a significant relationship between these first two variables and your target variable.
    However, for the second two plots, BMI and blood pressure, I think you can see a positive slope.
    So this may indicate that your model will find that higher blood pressure and higher body mass index are predictors of diabetes severity.

    Do you see any curvature or nonlinear relationships in the data?
    What do you think about the gender or sex plot?
    Can you think of a better way to visualize the relationship between a categorical variable like gender and a continuous variable like diabetes severity?
    Histograms with color representing a categorical variable are my favorite plot in this situation.
    It can also be helpful to embelish a 2D scatter plot with categorical variable as the color.
    You can plot age and severity on a scatter plot like the one here and then color the dots according to gender or sex.
    This might reveal patterns that we can't see in the two separate scatter plots.

    In the end your model will have the best eye of all.
    It will show you the exact linear relationship that is the best fit to your data.
    </aside>

# 16: Clinical Dataset (Blood Serum Test Results)

<aside class="notes">
    In these six scatterplots of your remaining features you can see the relationship between six blood tests and the target variable, diabetes severity.
    The first two blood serum tests provide the LDL and HDL cholesterol level.
    The other scatterplots show blood serum tests for vitamin B12 deficiency indicators as well as thyroid hormone levels and glucose levels.
    Using ones eye you can see a vague diagonal upward or downward trend in the severity of diabetes for each of these blood tests.
    Your challenge is to train a model to quantify these trends and use them to make accurate predictions.
    </aside>

# 17: Single-variate linear regression

<aside class="notes">
    In this plot you can see the linear regression for BMI vs diabetes severity.
    As you can see our eye did indeed accurately detect a real trend in the data.
    Using this one variable, our model can predict diabetes severity with a standard error or root mean square error of 62.
    Because the severity scale ranges from 50 to 350, this standard deviation or standard error represents about one fifth of the total range.
    Not bad for such a simple model and a few lines of python code.

    Another interesting piece of information that this model provides is the slope of the line.
    The slope of 10.26 tells you that for every increase of one in the BMI index there is an increase of more than 10 in the score for your diabetes severity.
    </aside>

# 18: Test Set Error larger than Training Set Error

<aside class="notes">
    In this chart you can see a comparison of the error on two separate subsets of the data.
    Before we fit a line to the data we removed 20% of the points to reserve as our unseen test set.
    This is like the questions that a teacher reserves for the final exam.
    The teacher doesn't give you these questions to train you, but instead gives you other similar questions taken from the same body of knowledge.
    That is what we do here with the machine student, the machine learner.

    On the left you can see how well the machine learning model did on a quiz made up of all the questions your, the teacher, showed it throughout the course of its training.
    You provided both the questions (the BMI) and the answers (the diabetes severity) during the training.
    This allowed the model to identify the linear relationship between these variables.

    On the righthand you can see how well this machine learner did on the final exam.
    When we compare the accuracy of the model on these two datasets you can see that it did about 5% better on the training set than the testset.
    This is about what you expect.
    The line was drawn through a point cloud that did not contain any of the points that we reserved for the test set.
    So it won't be as good as it could be at fitting to those points.

</aside>

# 19: Multivariate Regression

<aside class="notes">
    Once you understand the python syntax to use to create a regression with only one feature or independent variable, you might then be able to extend that to multiple variables.
    The same approach you used before will work here.
    You just give it questions that include more information for it to use to predict diabetes severity.

    This plot is much more difficult to visualize in 2 dimensions.
    Our fit is no longer a line but a multidimensional plane or hyperplane.
    so our red line spreads out into a cloud of points distributed across this plane for our predictions.
    Hopefully the true severity values in blue are closer, on average to these red predictions of severity that our model output.

    when you run the notebook for this multivariate model pay close attention to the RMSE to see if you see an improvement over your simple BMI model for diabetes.
    </aside>

# 20: Coefficients of Multivariate Model

<aside class="notes">
    Here you can see the coefficients for each of the first four featuers in our model: age, sex, BMI and blood pressure.
    It looks like our guesstimate of the age relationship wasn't too far off. each year of age actually reduces the likelihood of diabetes severity, but only slightly.
    For sex it seems that looks can be deceiving.
    The scatterplot seemed to show a zero slope for sex, but the model found that being female reduces your diabetes severity prediction by about 21 points.
    Because we have other parameters to contribute to our predictions, the BMI slope is no longer as high as it was earlier.
    It is about 35% smaller.
    But we have a new contributing factor to consider, blood pressure.
    It seems that each mm of mercury of blood pressure increases your diabetes severity about one point.

    </aside>

# 21: Blood Test Coefficients

<aside class="notes">
    Here are the remaining six coefficients for the six blood serum tests.
    From these slopes can you guess which one is the LDL or good cholesterol value?
    The dataset you will load in the exercise this week contains the names of each of these parameters so you can explore these relationships in greater detail.
    </aside>


# 22: How many features is too many?

<aside class="notes">
    One of the first intuitions you will gain as a data scientist is when enough is enough.
    In these slides you saw a linear regression in only 10 feature variables.
    And your dataset had nearly 400 examples of patients with these measurements.
    The Jupyter notebook you will be using this week shows how to generate many more derived features from these basic features.
    Each time you add another feature you will want to check the test set and training set accuracies.
    You can expect the training set accuracy to be better than your test set accuracy.
    But if you test set accuracy gets worse than it was before with a simpler model, then you may have gone too far.
    This is called over-fitting.
    If your model fits your training set so well that it does poorly on your test set, that is over-fitting.
    You will hear about this phenomenon in nearly every lesson from now on.
    You will see many more ways it can happen.
    And you will learn a variety of approaches to mitigating this error.
    </aside>
