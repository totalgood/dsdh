# Clinical Data Science

<aside class="notes">
    Welcome to lesson 4 in the data science for digital health course at UCSD Extension.
    I'm Hobson Lane.
    Today you will be learning how to build clinical data science models.
    By the end of this lesson you will be able to use python and data science to predict a patient's likelihood of a diabetes patient
    </aside>
# 1: Agenda

- Data Privacy Environments
    US: HIPPA
    Europe: GDPR
    PII and Privacy
    Developing Countries
- Clinical Machine Learning
    Pandas
    Scikit learn
# Data in Europe

<aside class="notes">
    The first word and the first consideration in any data science project is the data.
    So you will first look at the kinds of clinical healthcare data available to you in three environments.
    The US and Europe are becoming more and more similar in terms of the kinds of data that are available and who can access it.
    However, because most if not all European countries, private healthcare is the exception not the rule.
    This means that that healthcare providers in a clinical setting are more likely to be willing to share their data with "competitors" because it is not IP.
    Nonetheless international pharmaceutical companies that operate in Europe are for-profit.
    And pharmaceutical companies have access to the most detailed and extensive clinical data.
    In addition, privacy law in the US and Europe are quite different.
    In the US there is HIPPA, The Health Insurance Portability and Accountability Act.
    In Europe and soon in the US there is GDPR, The General Data Protection Regulation.
    HIPPA regulations in the US and GDPR regulations in Europe determine how organizations protect and disseminate data.
    This leaves a large plot of fertile ground for growing and harvesting data, the rural and agricultural regions of the world.
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

# EU and EEA Maps

<aside class="notes">
    The European Union and European Economic Area are governed by the GDPR and other healthcare data regulations that govern how personal data can be shared.
    From a data perspective this means that you can often gain access to datasets from Europe that cover a wide range of healthcare systems.
    And these systems serve patients with a greater diversity of ethnic backgrounds, cultural norms, and religious practices.
    Many cultures have a significant impact on food preparation and exposure to diseases and toxins.
    With the Wuhan corona virus, we've seen how the cultural norms around eating exotic wild animals can dramatically affect human health.
    Similarly, as you learned previously from John Snow's research in London many epidimics and healthcare crises have been traced to cultural norms and public services like water and sewage.
    As a data scientist working with data from Europe, this diversity of regulation and cultural norms enables you to more easily account for more variables that affect clinical outcomes.
    This can often lead to more effective clinical healthcare models.
    The ability to normalize for socioeconomic conditions and healthcare customs and regulations.
    </aside>

# WHO

<aside class="notes">
    The WHO (World Health Organization) provides an interactive gateway to a large repository of clinical healthcare data.
    Because of GDPR and greater uniformity of regulation around healthcare data, much of the WHO data comes from Europe.
    The WHO gateway to EU data is interactive and allows inexperienced data scientists to explore aggregated data with scatter charts, bubble charts, line charts and maps.
    It's possible to visualize up to 4 dimensions at once with time or year as the animation "dimension."
    In this plot you can see a "chloropleth" or map of beer consumption rates in Europe.
    Czenia aparently has this highest consumption rate, 7 liters of equivalent pure alcohol consumption per person.
    In Ireland the rate is only about 5 liters of pure alcohol.
    This chart is interactive, so the user can mouse-over any individual bubble or location on the map to see the detailed numerical data.
    The chart is also dynamic, it can be animated to show the changes from year to year using the play button at the bottom.
    The chart uses a javascript library called d3.js to allow this rich interactivity.
    </aside>

# d3.js

<aside class="notes">
    I'd like to give you a brief diversion into the eye candy of the d3.js library.
    Even though d3 is a javasript library, you don't have to know javascript to create these informative interactive visualizations.
    You can use a python package called plotly to generate all the code for you.
    It works just like seaborn, the main python package we use for visualization in this course.
    All you have to do is give plotly your data and then select and configure your plot with python commands and you can then have data-driven interactive visualizations to help you and your patients understand data in a richer way.
    Your takeaway from this should be to use the keywords "d3" and "plotly" in your duck.com searches for visualization ideas.
    Not only will you get inspired by new ways to look at your data, you may find code you can just copy and paste to create those visualizations for yourself.
    </aside>

# UK Hospital Data

<aside class="notes">
    In Europe it's often easier than in the US to retrieve detailed up-to-date data on patient care aggregated for individual hospitals and clinics.
    Here on this you can see a listing of all the hospitals in the UK and the aggregated discharge data or hospital episode statistics (HES) for each.
    This data can be used for epidemiology and healthcare system performance optimization, but not clinical data science.
    Clinical data science requires data on individual patients.
    Even if clinical medical records are not available, admission and discharge data must be provided on an individual basis for you to be able to normalize for confounding variables in you models.
    As a data scientist you would like normalize for individual patient variables such as treatment history, blood test results, biometric data or even just detailed demographics like age, gender, ethnicity, residence and workplace geographic information like postal code.
    As in the US, academic researchers must request access to patient records from the custodian of the data, usually another researcher who has acquired data from hospitals and government agencies.
    Individuals without an associated university or governmental organization and e-mail address generally are not allowed access to individual patient records, even when anonymized.
    </aside>

# PII

- birthday
- age (80+) + hospital
# US Clinical Data Science is Different

- pharma **prior**
    - insulin
    - medication

<aside class="notes">
    During the opioid crisis in the US, pharmaceutical companies were found to have utilized deceptive marketing and sales techniques to encourage doctors to prescribe opioids.
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





# PII

Also a big part of hospital performance metric (in addition to outcomes, and case difficulty)

# prescriptive vs descriptive

# exercise: predict diabetes risk
