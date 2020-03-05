# Deep Learning and AI

# Agenda

- Deep Learning
    - Why
    - What
    - How
- Example
    - TF playground
    - heart sounds
- IA?

<aside class="notes">
    The definition of AI is a bit vague and controversial.
    So rather than confusing you with that controversy, you'll learn how to use AI first.
    You'll build on your experience with machine learning in the previous lesson to help you see how deep learning is a big improvement in the state of the art.
    This will help you develop your own definitions of AI and deep learning.
    Just as you have your own definition of Intelligence, you'll have your own perspective on artificial intelligence or machine intelligence.
    That will help you see how you can use it to tackle some of the harder problems in healthcare data science.

    You'll go back to the playground for a bit so you can play with deep learning again.
    Now that you've experienced machine learning and you understand why deep learning is such a big deal, you'll appreciate some of the sublties of the playground a bit better.
    And then we'll dive into a real example dataset and problem statement that you can experiment with.
    Just like the previous lesson, I'll walk you through an overview of a data science pipeline.
    Only this time you'll use deep learning and compare it to conventional machine learning approaches.
    You'll teach a machine to listen through a stethescope to patients' hearts.
    This may touch a nerve if you're a doctor who prides herself on her stethescope skills.
</aside>

# Review: Diabetes Prediction

<aside class="notes">
    Last week you trained a diabetes prediciton model.
    You used the SciKit-Learn package in a jupyter notebook to fit a LinearRegression model to 10 columns of clinical patient data.
    You used features like patient age, sex, and BMI to predict diabetes severity.
    As you added more variables to the fit, the model got more and more accurate.

    Above the data table in this chart you can see the mathematical equation for a linear regression.
    Y is the target variable, the severity of disease.
    It ranges between 0 and 300 in your dataset.
    The best RMSE (Root Mean Square Error) on the test set that you were able to achieve was probably about 55 on this severity score scale.
    55 divided by 300 is about 18% standard error.
    This isn't bad, but I'm sure your patients would like a bit more certainty in your diagnosis.

    Look at the formula for linear regression.
    A linear regression merely adds and subtract your features in a linear combination.


    The first term in the formula is C_0, the intercept or the offset.
    The intercept is just your average of all the target variable values in your dataset, the entire column of diabetes severity values.
    The average severity in your diabetes dataset is 150, halfway between 0 and 300.
    This is why your Linear Regression intercept was 150.

    The rest of the fomula shows how you multiply each feature by a coefficient is create a weighted average of your features.
    This weighted average is the prediction for that particular patient.
    Your weights or slopes can be negative, but otherwise it's just like taking a weighted average of a row in your spreadsheet of data.
    </aside>

# Linear Regression

<aside class="notes">
    Here you can see the python code for the linear regression formula.
    The scikit-learn implementation stores those coeficients in an object attribute named `coef_`.
    So if you named your linear regression `lr` you can see the actual slopes of your lines along each dimension the `lr.coef_` array values.
    There is one coef value for each feature.
    Your features are arranged in the same order as the data you passed into the fit method on the model.

    Take a look at first and seond coefficients, shown in red here within the python code snippet.
    The first slope after the intercept, `lr.coef_[0]` , tells you the relationship between patient age and your severity prediction.
    And your `.intercept_` value is just added to this linear combination of all your feature values.
    </aside>

# Data Flow

<aside class="notes">
    You can get a new perspective on all this math if you think about it like signals flowing through wires or neurons in your body.
    The features are what your model is measuring or sensing.
    You can diagram those as blue arrows flowing out of the lab or the clinic database and into your model.
    </aside>

# 6: Model Multiplication

<aside class="notes">
    Your blue feature values are multipled by the red coefficients as they flow through your model.
    You have one of these multiplications and regression lines for each feature.
    This creates a new value that is the estimated severity change based on that feature.
    These new values are going to be added together to produce the total severity score prediction.
    So you can think of each calculation as bumping the score up or down a bit.
</aside>

# 7: Nudges

<aside class="notes">
    You can plot these prediction nudges on a scatter plot.
    They would form the points on this red line if you did this for a wide range of features.
    You can see graphically how the red slope values define a line that passes through the cloud of previous values of x.
    These point clouds are your features that you trained your model on.
    Because this is a linear model, the nudge only gets linearly bigger in proportion to the change in the value of the feature.
    The coefficients tell you the slopes of each of the red lines in these scatter plots.
    The training set severity values are plotted here in the scatter plots so you can see how the model got these slopes.
</aside>

# 8: Voting

    <aside class="notes">
    point on the red linear regression lines.



    Red multplied by blue makes the purple output variable.
    Of course you add the intercept to this regression value so that it bumps up the prediction to the appropriate range.
    </aside>

#

# Man vs Machine

<aside class="notes">
    A 2007 study found that internists who regreshed their stethescope skills by using a smartphone app were able to double their accuracy.
    The doctors who listened to 400 clips of 5 different heart murmurs were able to then correctly classify real heart murmurs with 80% accuracy, vs 40% for the control group.
</aside>

# NLP Application: Summarization

- Adjudication
- Clinical Medical Records
- Insurance Claims
- Retrospective Utilization Review

<aside class="notes">
    Clinical medical records full of unstructured data in a variety of formats.
    Summarizing these records brings together deep learning algorithms for NLP and computer vision.
    An obvious application is to use NLP to and summarize text notes by doctors and nurses.
    Interestingly machines are also being taught to read the reports generated by other machines such as those tables of blood test and genetic test results included in your medical record.
    Over time EHR systems will standardize on more and more data formats for the various tabular data generated by the machines assisting us with medical tests and procedures.
    Only recently has deep learning technology advanced to the point that machines can start to reduce the burdon on doctors.
    Doctors are the first ones to benefit from systems that allow them to summarize clinical medical records accurately.
    This helps doctors focus on the most relevant information in the long history of symptoms and treatments cataloged in a clinical medical record.
    In the US most of the deep learning and AI applications in healthcare center around insurance companies.
    Adjudication is the process by which health insurers aprove or deny claims and coverage requests.
    When you file a medical health insurance claim or obtain treatment at a hospital, that begins a long paper trail of documentation and bills.
    Your clinical medical record is updated and the insurer then reviews the bill from the provider.
    They can *disposition* the claim, request additional information.
    Health Insurance companies are required to pay for outside entities to review insurance claims to validate their disposition.
    These outside entities hire doctors to review clinical medical records and the dispositionare leading the way in employing deep learning and AI to improve docto
    </aside>

# NLP Application: Search and QA

- LiveStrong.com
- MayoClinic.com
- WebMD.com

<aside class="notes">
    Like you learned in the previous lesson, chatbots are a common applicaiton of deep learning and AI in healthcare.
    More and more patients and doctors are using search and chat to find answers to their medical questions.

    </aside>

# NLP Application: Medical Assistance

- CommCare (dimagi)
- Breath, Calm

# NLP Applicaitons: Mental Health Coaching

- Woebot
- Mindcurrent

- Replika

## TODO

[-] Why: Review feature engineering (sum, product, polynomial, pca)
[-] Layers: linear combinations of linear combinations creates nonlinear math?
[-] tensorflow playground
[-] sound file feature engineering (FFT, cepstral coefficients, convolutional filters, CNN)
[-] image file feature engineering (PCA, FFT, CNN)
[-] biology of neurons
[-] biology of brains

# What

<aside class="notes">

    </aside>

# Why

Feature engineering

<aside class="notes">
    What did you learn from your experience with the diabetes dataset?
    Did you generate all possible products, quotients, polynomials, exponentials, logs, transcendentals (sin, cos, tan, htan, etc)?
    What about all the possible phases and periods of transcendentals?
    If you did try to improve upon the 15% standard error
    </aside>

# How

Back propagation



# 3: Applications

- Medical imagery

# Medical imagery for diagnosis

- broken bones
- tumors
- pneumothorax
- retina damage

::: notes

Medical imagery can be used to diagnose injury like broken bones, torn ligaments, trauma, skin abnormalities, and damage to your retina or cornea (lasers, arc welding, sun damage).
Medical imagery is also used to diagnose disease like pulmonary disease, cardio-vascular disease, and even psychological abnormalities.
Data science tools are contributing in all of these areas.

:::

# Medical imagery for postoperative assessment

- Damage to tumors
- Ablative "tracks" in hear muscle
- Collatoral damage to healthy tissue



### References

SR: Phonocardiograms
["Artificial intelligence in healthcare: past, present andfuture"](https://svn.bmj.com/content/svnbmj/2/4/230.full.pdf) by Fei Jiang, Yong Jiang, et al., bit.ly/ucsd-ai-survey
