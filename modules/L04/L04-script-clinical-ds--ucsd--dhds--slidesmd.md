# Clinical Data Science

# 1: Agenda

- Data Privacy Environments
    US (HIPPA)
    Europe (GDPR)
    Developing Countries
- Clinical Machine Learning
    Pandas
    Scikit learn
# Data in Europe


<aside class="notes">
    For data in Europe, the W H O (World Health Organization) provides an interactive gateway to explore aggregate data with scatter charts, bubble charts, line charts and maps.
    It's possible to visualize up to 4 dimensions at once with time or year as the animation "dimension."
    In this plot you can see a "chloropleth" or map of beer consumption rates in Europe.
    Czenia aparently has this highest consumption rate, 7 liters of equivalent pure alcohol consumption per person.
    In Ireland the rate is only about 5 liters of pure alcohol.
    This chart is interactive, so the user can mouse-over any individual bubble or location on the map to see the detailed numerical data.
    The chart is also dynamic, it can be animated to show the changes from year to year using the play button at the bottom.
    The chart uses a javascript library called d3 to allow this rich interactivity.
    There is a library called plotly in python that can automatically create these
    In addition
    </aside>

# Hospital Data

<aside class="notes">
    In Europe it's often easier to retrieve detailed up-to-date data on patient care aggregated for individual hospitals and clinics.
    This data can be used for epidemiology and healthcare system performance optimization, but not clinical data science.
    But individual patient admission and discharge data is not often available.
    This limits a data scientists ability to "normalize" or account for confounding variables and influences specific to individuals, such as treatment history, blood test results, and biometric data.
    As in the US, academic researchers must request access to patient records from the custodian of the data, usually another researcher who has acquired data from hospitals and government agencies.
    Individuals without an associated university or governmental organization and e-mail address generally are not allowed access to individual patient records, even when anonymized.
    </aside>

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

# 2: PII

- birthday
- age (80+) + hospital

# 3: clinical trials

# clinical trial advantages

- compensates for confounding variables
- requires fewer trials, fewer patients at risk

# bias/flaw: gender

Due to birth defects caused by diet pills (fen fen?) Women were excluded from future drug trials

# bias/flaw: age

Terminally ill patients on risky drug trials are old and may not have same side effects. Existing conditions may mask side effects (especially cognitive, endurance, and other difficult to assess illnesses)

# bias/flaw: youth

Youth used in psych and exercise and trials (before brain fully formed)

# PII

Also a big part of hospital performance metric (in addition to outcomes, and case difficulty)

# prescriptive vs descriptive

# exercise: predict diabetes risk
