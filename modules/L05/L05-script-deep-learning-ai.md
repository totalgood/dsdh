# 1: Deep Learning and AI

<aside class="notes">
    I'm Hobson Lane.
    Welcome to lesson five of the Data science for digital Health course at UCSD Extension.
    Today you are going to learn about Deep Learning and Artificial Intelligence, or AI, and how they can be used to solve problems in healthcare.
    </aside>

# 2: Agenda

Machine Learning Review
Deep Learning
Layered linear regression
Forward and backward propagation
Making it nonlinear
What it’s good for
Playground
Artificial Intelligence
Intelligence Augmentation

<aside class="notes">
    The definition of Artificial Intelligence is a bit vague and controversial so you will build up your understanding of AI in stages.
    You will start with one of the core technologies used in AI, called *Deep Learning*.
    You will build on your experience with machine learning, starting in the shallow end of the swimming pool.
    Later you'll dive into deep learning and discover how it is a big improvement over conventional machine learning.
    You'll see how to add layers of learning to your pipeline to create a deep learning neural network.
    You'll learn how to compute predictions using forward propagation through your network.
    And you'll gain an intuition about how backpropagation is used to train the model and learn the right parameters for your model.

    You'll go back to the playground for a bit so you can play with deep learning again.
    Now that you've experienced machine learning and you understand why deep learning is such a big deal, you'll appreciate some of the subtleties of the playground a bit better, like feature engineering.

    This experience will help you see how you can use deep learning to tackle some of the harder problems in healthcare data science.
    And you will develop your own definitions of AI and deep learning.
    Just as you have your own definition of Intelligence, you'll have your own perspective on artificial intelligence or machine intelligence.
    </aside>

# 3: Linear Regression Review: Diabetes

<aside class="notes">
    Last week you trained a diabetes prediction model.
    You used the SciKit-Learn package in a jupyter notebook to fit a LinearRegression to 10 columns of clinical patient data.
    You used features like the age, sex, and BMI of to predict diabetes severity for each patient.
    As you added more variables to the fit, the model got more and more accurate.

    Above the data table in this chart you can see the mathematical equation for a linear regression.
    Y is the target variable, the severity of disease.
    It ranges between 0 and 300 in your dataset.
    The best RMSE (Root Mean Square Error) on the test set that you were able to achieve was probably about 55 on this severity score scale.
    55 divided by 300 is about 18% standard error.
    This isn't bad, but I'm sure your patients would like a bit more certainty in your diagnosis.

    Look at the formula for linear regression.
    A linear regression merely adds and subtracts your features after multiplying them by coefficients.
    In a linear regression these are the slopes of the plane along each dimension.
    These coefficients are the parameters that are learned when you fit your linear regression model to the training set.

    The first term in the formula is C_0, the intercept or the offset parameter.
    For a linear regression the intercept parameter is just your average of all the target variable values in your dataset, the entire column of diabetes severity values.
    The average severity in your diabetes dataset is 150, halfway between 0 and 300.
    This is why your Linear Regression intercept parameter came out to around 150.

    The rest of the equation shows how you multiply each feature by the learned parameters of your model to compute a prediction.
    </aside>

# 4: LinearRegression.coef_

<aside class="notes">
    Imagine you've already fit your scikit learn LinearRegression model to your table of patient data.
    Now a new patient comes into your office.
    You want to predict their likelihood of developing severe diabetes over the next year.
    Fortunately you have all their blood test results, demographics, and vital signs.
    So we can pass those numbers into your model and get a prediction.
    This is called the prediction or inference part of your process.
    This is how you can use a model to make a logical inference about the world.
    Within your algorithm the inference is something like if the patient's age is 59 and they are female with a body mass index of 32.1 and so on, the linear regression would estimate that they will have a severity rating of 150 plus or minus 50.

    Here you can see the python code for the linear regression formula.

    The SciKit-Learn implementation of a LinearRegression stores the coefficients in an attribute named `coef_`.
    The underscore or underline character is the low horizontal line that you get when you use the Shift key on your keyboard with the hyphen or minus key.
    The parameters of other scikit-learn models are also stored in this `coef_` attribute.
    If you named your linear regression `lr` you can see the actual slopes for your regression in the values of the `lr.coef_`
    There is one coefficient value for each feature in your model.
    Your features are arranged in the same order as the data you passed into the fit method on the model.

    Take a look at the first and second coefficients, shown in red here within the python code snippet.
    The first slope after the intercept, `coef_[0]`, tells you the relationship between patient age and your severity prediction.
    The second coefficient, `coef_[1]`, tells you the relationship between patient gender and your severity prediction.
    You multiply all these coefficients by your feature values and sum them up with the `.intercept_` value to get the predicted diabetes severity for that patient.
    </aside>

# 5: Data Flow

<aside class="notes">
    You can think of a data science pipeline as a flow of data.
    Imagine a single patient's data flowing in from the top of the screen.
    Your patient's data is a vector or array containing their age, gender, body mass index, blood pressure and so on".
    You can represent the values flowing through your algorithm as arrows or lines in a network.
    </aside>

# 6: Multiplication

<aside class="notes">
    Each one of those lines is connecting a piece of data with a term in our equation, a multiplication.
    So arrows represent multiplication in this network diagram.
    As our data reaches the end of the blue arrow it is multiplied by the red coefficient for that feature.
    So the 59 year old patient in this example has that 59 multiplied by a value of negative .2 from our model coefficient for age, shown here in red.
    That gives us about negative 12.
    And the patient's gender is female for this example, which a value of 1 in our dataset, so your prediction algorithms multiplies negative 20 by 1 to get negative 20.
    Negative twelve plus negative 20 give negative 32.
    And we keep doing this for body mass index and blood pressure and any other parameters in our model.
    </aside>

# 7: Coefficients as Slopes

<aside class="notes">
    If you plotted a blue point for each value of each patient you would get the scatter plots like you created in your linear regression exercise.
    And if you plotted your predictions based on each of the features of the patient, you would get the red lines in these plots.
    These are defined by the slopes in your coefficients within your model.
</aside>

# 8: Combining the Nudges

<aside class="notes">
    Each of your patient's features are nudging the severity score up or down, depending on the slope of the coefficient.
    You combine all these nudges together by just adding them up.
    You can show that in a network diagram with a plus sign in a circle.
    We changed these arrows from blue to purple because they contain the product of the red slopes and the blue data points.
    Red and blue gives purple.

    And you need to add in the intercept as well.
    Sometime people like to think of this as the slope that is multiplied by 1.
    But you are just adding our intercept of 150 to the total sum of all the other nudges to get your prediction.
    So for this first patient in your table you are adding 150 plus negative twelve plus negative twenty and so on.
    This patient will probably have a pretty low diabetes severity prediction.
</aside>

# 9: Network Diagram

<aside class="notes">
    Now that you've seen where all these numbers come from in the linear regression formula, let's organize all the multiplications and additions into a single layer.
    This creates a single layer network diagram.
    Our patient's features flow in from the top and are multiplied by the model coefficients within the arrows connecting those data points to the central sum operation.
    The circle with the plus sign in the middle of this chart adds all these signals up.
    And out flows our prediction at the bottom of the chart.

    So what is the point of showing all this simple math in a network diagram?
    Because for now, our linear regression model is shallow.
    It has only one layer of multiplications and additions happening.

# 10: Neuron Simulation

<aside class="notes">
    In the 1960 scientists and doctors looked at a network diagram for linear regression like this and realized it looked a lot like the neurons they saw under a microscope.
    Neuroscientists and statisticians were beginning to think about ways they could build more complicated models to make deeper decisions and predictions, like the human brain does.
    It had been more than 100 years (1843) since Ada Lovelace had invented the idea of computer program for mechanical computers.
    And Turing had just opened the world's eyes to the possibility of electronic computers.
    So researchers diagrammed the math of linear regression based on what they imagined might be happening in the neurons of a brain, an artificial brain that could be simulated in a computer.
    </aside>

# 11: Perceptron = Neuron Simulation

    <aside class="notes">
    Psychologists, like Frank Rosenblatt came up with the idea of a perceptron or an artificial neuron.
    Scientists were imagining that when a doctor sees an woman walk into their office, one neuron might nudge the doctor's prediction of diabetes down by a bit.
    When the neural network received the BMI value back, that would have another effect on the prediction of diabetes.
    So the lines in this diagram represent the flow of information in an artificial neural network.

    This first network of ours is equivalent to a normal linear regression.
    It's a shallow network, with only one layer and one neuron in that layer.
    </aside>

# 12: More Neurons = Smarter?

<aside>
If you're like Frank Rosenblatt, you're probably asking yourself if adding more neurons might make your neural network a little smarter?
Most organisms route different kinds of information to different neurons.
So suppose you want to divide your features into 3 groups to create separate pathways for each kind of feature.
You could connect the three body type features, age, sex, and BMI to one neuron.
You could connect the cardio vascular features, cholesterol levels and blood pressure, to another neuron.
All the other blood serum lab results could go into a third neuron.

There's a problem with this approach.
Those of you that understand linear algebra and math will see that three linear regressions is no better than a single linear regression.
It produces the exact same math in the end, because you are just adding together your feature values after multiplying them by learned coefficients or slopes.
This is the associative property of addition.
It doesn't
</aside>

# 13: More Layers= Smarter?
You would combine these predictions together in a 4th neuron to give a total prediction of diabetes.
This seems to be the way some simple neural networks work.
</aside>

# 14: More Neurons?

<aside class="notes">
    So, as captain kirk would say "Gimme more power Scotty!"
    But if you try to add more layers and more neurons, you'll find it doesn't help."I can't gih yuh any mah Captain!"
    like Scotty in the old _Star Trek_ series you'll have to say "I cannae change the laws of physics!"
    Play with linear neurons in the neural network playground and see if you can find any problems they are good for?
    Now dial your network back to just one neuron and one layer.
    Did that work just as well on your problem?
    </aside>

# 13: 4x2 Network

<aside class="notes">
    If someone tells you that your neural net is dense, they aren't saying that it's dumb, just that it is "fully connected".
    What that means, is that at each layer, each and every neuron in that layer is connected by a weight parameter to each and every neuron in the layer above.
    This is what creates that rectangular parameter or weight matrix that you are multiplying by the vector flowing in from the layer above.
    So that parameter or weight matrix needs to have as many outputs (rows) as you have neurons on the layer below.
    And your parameter or weight matrix between each layer of neurons should have as many inputs (columns) as you have neurons on the layer above.
    And each of these multiplications is just a linear transformation (a rotation and stretching) of the vector above to create a new vector for the layer below.
    This math is exactly the same as the math of a linear regression.
    There's no magic or deep learning here, unless you add a nonlinear *activation function* to your neurons in at least one of the layers.
    </aside>

# Your Network is Dense

<aside class="notes">
    So what activation function should you chose?
    In the early days, the inventor of the neural network, Rosenblat just used a threshold to create a binary output.
    This is because perceptrons were intended to be used to learn binary logic, the logic of computer programs and mathematical proofs.
    Rosenblatt and early researchers assumed that it would be best if each neuron just output a bit.
    But this turned out to be a bit too

    </aside>

# ReLU Activation Function

<aside class="notes">
    It took a while for the Deep Learning researchers to discover reLU activation function.
    The RE in relu stands for rectifified. This is from electrical engineering when you
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


# 31: Backpropagation

<aside class="notes">
    For a linear regression and a single layer neural network there is mathematical formula that will tell you exactly how to adjust your coefficients or parameters to find the best fit.
    In the spreadsheet data science exercise, you didn't even need to use the formula.
    You were able to guess around at different slopes and intercepts until you eventually found a really good fit.
    You can see what each slope does to nudge your answer either closer or further away from the answer.
    But imagine you add a second layer.
    Now when you adjust a slope in the first layer, depending on the sign and magnitude of the coefficients in the second layer, your nudge could push the prediction either closer or further from the truth.
    You have more *degrees of freedom* to work with.
    Even a machine can't deal with this interdependence between the various parameters or coefficients of your model.
    There are multiple different ways it could adjust all the parameters and end up with the same affect on the output.
    You can put all your changes in the layer closest to the output and still get the same fit accuracy as if you put all your changes in the first layer.
    The gradient usually tells a machine learning algorithm how much to adjust each coefficient.
    But for a multi-layer network, this naive approach can lead to what's called "vanishing gradients", where your algorithm only adjusts the output layer coefficients, and never really does much with the first input layer's coefficients.

    Researchers like Henry Kelley first ran into this problem of vanishing gradients in 1960, when working the first neural networks, called perceptrons.
    But it wasn't until 2012 that Geoffrey Hinton and his colleagues at Google published an approach to back-propagation that made it practical on deep, complex neural network architectures.
    These are the deep learning architectures and approaches that are used for modern computer vision problems like x-ray image classification.
    </aside>


# ?: Man vs Machine

<aside class="notes">
    A 2007 study found that internists who refreshed their stethoscope skills by using a smartphone app were able to double their accuracy.
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

### Questions

```yaml
-
    Q: "Were you able to get better than 50% accuracy for the single-layer, 3-neuron, linear neural network: [bit.ly/ucsd-ucsd-try-3-neurons](http://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=3&seed=0.39223&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)?"
-
    Q: "Does increasing the number of linear neurons or layers improve accuracy: [bit.ly/ucsd-ucsd-try-5-5-5-neurons](http://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=3&seed=0.39223&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)?"
    A: No, adding more neurons or layers doesn't help a neural network improve accuracy if the underlying process is nonlinear.
-
    Q: Is it possible to make a neural network nonlinear by adding more linear layers or more linear neurons?
    A: No, a multilayer neural network of many linear neurons is equivalent to a linear network with only one layer and one neuron. Adding more neurons or layers doesn't help a neural network model a nonlinear process or function.
```



### Links

ucsd

### References

On International Womens Day I thought you would enjoy two videos by women driving the movements towards using Randomized Controlled Trials to increase the social impact of foreign aid and social programs.:

SR: Esther Duflo's ["Social Experiments to Fight Poverty"](https://www.ted.com/talks/esther_duflo_social_experiments_to_fight_poverty?language=en#t-660028)
SR: Jacqueline Gratz's [A Third way to Think about Aid](https://www.ted.com/talks/jacqueline_novogratz_a_third_way_to_think_about_aid)

SR: Phonocardiograms

["Artificial intelligence in healthcare: past, present and future"](https://svn.bmj.com/content/svnbmj/2/4/230.full.pdf) by Fei Jiang, Yong Jiang, et al., bit.ly/ucsd-ai-survey
