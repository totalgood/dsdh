# 1: Deep Learning and AI

<aside class="notes">
    I'm Hobson Lane.
    Welcome to Lesson 5 of the _Data Science for Digital Health_ course at UCSD Extension.
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
    The term "Artificial Intelligence" is a bit unscientific and controversial so you will build up your understanding of AI in stages.
    You will start with one of the core technologies used in AI, called *Deep Learning*.
    You will build on your experience with machine learning, starting in the shallow end of the swimming pool.
    Later you will dive into deep learning and discover how it is a big improvement over conventional machine learning.
    You will see how to add layers of learning to your pipeline to create a deep learning neural network.
    You'll learn how to compute predictions using forward propagation through your network.
    And you'll gain an intuition about how backpropagation is used to train the model and learn the right parameters for your model.

    You will go back to the neural network playground for a bit so you can play with neural networks again.
    Now that you've experienced machine learning and you understand why deep learning is such a big deal, you'll appreciate some of the subtleties of the playground a bit better, like feature engineering.

    This experience will help you see how you can use deep learning to tackle some of the harder problems in healthcare data science.
    And you will develop your own definitions of AI and deep learning.
    Just as you have your own definition of *intelligence*, you will have your own perspective on artificial intelligence or machine intelligence.
    </aside>

# 3: Linear Regression Review: Diabetes

<aside class="notes">
    Last week you trained a diabetes prediction model.
    You used the SciKit-Learn package in a jupyter notebook to fit a LinearRegression to 10 columns of clinical patient data.
    You used features like the age, sex, and BMI of to predict diabetes severity for each patient in your tabel.
    As you added more variables to the fit, the model got more and more accurate.

    Above the data table in this chart you can see the mathematical equation for a linear regression.
    Y is the target variable, the severity of diabetes after 1 year.
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
    If you named your linear regression `lr` you can see the actual slopes for your regression in the values of the `lr.coef_` attribute.
    There is one coefficient value for each feature in your model.
    Your features are arranged in the same order as the data you passed into the fit method of your model.

    Take a look at the first and second coefficients, shown in red here within the python code snippet.
    The first slope after the intercept, `coef_[0]`, tells you the relationship between patient age and your severity prediction.
    The second coefficient, `coef_[1]`, tells you the relationship between patient gender and your severity prediction.
    You multiply all these coefficients by your feature values and sum them up with the `.intercept_` value to get the predicted diabetes severity for that patient.

    The scikit learn package and the LinearRegression model take care of all this math when you call the `.predict()` method.
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
    So the 59 year old patient in this example has that 59 value multiplied by a value of negative .2 from our model coefficient for age, shown here in red.
    That gives us about negative 12.
    And the patient's gender is female for this example, which is a value of 1 in our dataset, so the predict method for the scikit learn model multiplies negative 20 by 1 to get negative 20.
    Negative twelve plus negative 20 give negative 32.
    And we keep doing this for body mass index and blood pressure and any other parameters in our model.
    </aside>

# 7: Coefficients as Slopes

<aside class="notes">
    If you plotted a blue point for each value of each patient you would get the scatter plots like you created in your linear regression exercise.
    And if you plotted your predictions based on each of the features of the patient, you would get the red lines in these plots.
    These are defined by the slopes in your coefficients within your model.

    ### TBR: to be recorded
    You can plot your prediction nudges on a scatter plot.
    They would form the points on this red line if you did this for a wide range of feature values.
    You can see graphically how the red slope values define a line that passes through the cloud of previous values of x.
    These point clouds are your features that you trained your model on.
    Because this is a linear model, the nudge only gets linearly bigger in proportion to the change in the value of the feature.
    The coefficients tell you the slopes of each of the red lines in these scatter plots.
    The training set severity values are plotted here in the scatter plots so you can see how the model got these slopes.
</aside>

# 8: Combining the Nudges

<aside class="notes">
    Each of your patient's features are nudging the severity score up or down, depending on the slope of the coefficient.
    You combine all these nudges together by just adding them up.
    You can show that in a network diagram with a plus sign in a circle.
    We changed these arrows from blue to purple because they contain the product of the red slopes and the blue data points.
    Red and blue gives purple.

    And you need to add in the intercept as well.
    Some people like to think of this intercept as a slope that is multiplied by a constant feature value of 1.0.
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

# 10: Neuron

<aside class="notes">
    In 1960, scientists and doctors looked at a network diagram for linear regression like this, and they realized it looked a lot like the neurons they saw under a microscope.
    At this time neuroscientists and statisticians were beginning to think about the ways they could build more complicated models to make deeper decisions and predictions.
    They were trying to imitate human decisions and predictions with a computer.
    It had been more than 100 years since Ada Lovelace in 1843 had invented the concept of a computer program.
    So by the 1960's researchers had had a lot of time to think about algorithms to program into a computer.
    And in the 1940's, Turing had opened the world's eyes to the possibility of electronic computers and the kinds of problems they could solve.
    So researchers diagrammed the math of linear regression based on what they imagined might be possible in a computer.
    And they wanted to see if it were possible to program the decision process that was happing in the neurons of a brain.
    This was the advent of the first artificial neuron, a neuron that could be simulated in a computer.
    </aside>

# 11: Perceptron = Neuron Simulation

    <aside class="notes">
    Psychologists, like Frank Rosenblatt came up with the idea of a perceptron or an artificial neuron.
    Scientists were imagining that when a doctor sees an woman walk into their office, one neuron might nudge the doctor's prediction of diabetes down by a bit.
    When the neural network received the BMI index value from a nurse, that would have another effect on the prediction of diabetes.
    So the lines in this diagram represent the flow of information in a simple artificial neural network.

    This first network of ours is equivalent to a normal linear regression.
    It's a shallow network, with only one layer and one neuron in that layer.
    </aside>

# 12: More Neurons = Smarter?

<aside>
If you're like Frank Rosenblatt, you are probably asking yourself if adding more neurons might make your neural network a little smarter.
Most organisms route different kinds of information to different neurons.
So suppose you want to divide your features into 3 groups to create separate pathways for each kind of feature.
You could connect the three body type features, age, sex, and BMI to one neuron.
You could connect the cardio vascular features, cholesterol levels and blood pressure, to another neuron.
All the other blood serum lab results could go into a third neuron.

There's a problem with this approach.
Those of you that understand linear algebra and math will see that three linear regressions is no better than a single linear regression.
It produces the exact same math in the end, because you are just adding together your feature values after multiplying them by learned coefficients or slopes.
This is the associative property of addition.
</aside>

# 13: Try it!

<aside class="notes">
    This is an important insight in deep learning.
    It will help you design neural networks for healthcare problems if you let the idea sink in.
    Once you're just about to give up on neural networks to go back to your trusty linear regression, we'll show you how to give your network the brain power it needs to solve modern problems.
    But for now it will help your understanding to play with a simple 3-neuron neural network again.
    Visit this link to the neural network playground.
    I've set the activation function to be linear, so this network imitates the math we've talked about so far.
    The only thing that might be a little confusing is that I've set this to a classification problem.
    In this playground exercise you are trying to discriminate between severe diabetes and mild diabetes, the blue and red dots on the scatter plot.
    You are not predicting a continuous score between 0 and 300 like we did earlier.
    And you are only using two features x_1 and x_2 to predict your target variable.
    But the insights are the same as for a linear regression and multiple variables.
    You will find, with this 3-neuron neural network, that it is impossible to do any better with your prediction than flipping a coin.
    This is because we've created a nonlinear problem with the doughnut shaped dataset shown in the scatter plot.
    A linear neural network and a linear regression are no match for a nonlinear problem.
</aside>

# 14: More Layers = Smarter?

<aside>
    But what about adding additional layers?
    You could combine the predictions from the 3 neurons together in a 4th neuron to give a total prediction of diabetes.
    This seems to be the way some real neural networks work in the world of biology.
    Perhaps this will give your model the nonlinearity it needs to deal with the doughnut and the diabetes problems.
    After all, most brains that make decisions like this contain more than one neuron.
</aside>

# 15: More Power?

<aside class="notes">
    So, as captain kirk would say "Gimme more power, Scotty!"
    But if you try to add more layers and more neurons, you will find it does not help.
    Like Scotty in the old _Star Trek_ series you'll have to say "I cannae change the laws of physics!"
    Play with 3 layers of linear neurons in the neural network playground.
    This network is set up with 5 neurons in each of 5 layers.
    Try it with the doughnut problem first.
    Now select some of the other datasets in the upper left.
    Can you can find any problems that this deep neural network is good at solving?
    Now dial your network back to just one neuron and one layer.
    Did that work on the simpler problem you found?
    </aside>

# 16: Activation Function: Thresholding

<aside class="notes">
    Now that you have struggled with combining linear regressions to solve nonlinear problems, it is finally time to get nonlinear.
    You have reached the big reveal for this lesson and for deep learning.
    Deep learning relies on an important additional function in our artificial neurons to make them work.
    You need an activation function.
    And not just any activation function will do.
    It needs to be nonlinear.
    You can't just multiply the entire sum of your prediction by some linear value like you did with linear regression.
    You need to run a function on your predictions or output values, a function that looks nonlinear.

    In the 1960's Rosenblatt and the other inventors of perceptrons were interested in binary classification problems.
    These are the fundamental building blocks of all decisions.
    These are the *if* - *then* statements in a computer program.
    We just want our neural network to program itself based on example dataset.
    So the first activation function that was tried was just a threshold check at a value of zero.
    So you can shift your diabetes severity score by subtracting 150 so that the output is between negative 150 and positive 150.
    When your network computes a score that's above zero your activation function can change it to a positive 1.
    When your network computes a score that's below zero your activation function can change it to a zero.
    This is also sometimes called the Heaviside function.
    But you don't need to remember that name or the function's shape, because it turns out not to be as useful as more recent activation functions.
    </aside>

# 17: Activation Function: Sigmoid

<aside>
    Mathematicians like to work with smooth functions that are differentiable.
    And that's what the word sigmoid means.
    It means S-shaped.
    And the shape of the letter S is quite smooth.
    If a function is differentiable that means you can compute the slope or gradient of that function at any point on it, for any input value.
    It has no hard corners.
    It's possible to perform the fitting of your model to data much faster and more accurately if you can compute the slope or gradient of your activation function.
    And the sigmoid function turns out to be a particularly easy function to compute the derivative or gradient for.
    In fact the derivative of the sigmoid function is the sigmoid function itself!
    So early researchers thought they were being clever when they chose this as their activation function for neural networks.
    It took decades for them to figure out why this was a bad idea for most complex problems.
    For simple problems and for regression problems, the sigmoid function is still sometimes used.
    But in almost all cases you will be better off using an even simpler activation function, that only really became popular in the 21st century.
</aside>

# 18: Activation Function: ReLU

    <aside>
        In 2012 Hinton and other researchers were trying to solve a really hard problem.
        They were classifying millions of images into more than 100 different categories for Imagenet.
        They were trying to teach a machine to recognize things like cats and dogs and cars and motorcycles.
        The lowly ReLU activation function turned out to be one of the pieces that helped them solve this problem.

        ReLU stands for rectified linear unit, R E L U.
        Rectified means that all negative values are turned positive or set to zero on the output.
        For ReLU, the output is zero for any negative input.
        And the linear unit part of ReLU just means that the output is exactly the same as the input for any positive values.

        It surprised most researchers to find that this activation function worked so well.
        It turns out that it has just the right amount of nonlinearity to solve the image classification problem quickly.
        Feel free to go back to your neural network playground examples and see if relu is the last piece of the puzzle you need to solve the doughnut problem and the diabetes problem.

        In most cases this is the activation function you will want to use in your neural networks.
    </aside>

# 19: Grouping Features

<aside class="notes">
    Earlier we talked about grouping similar features together as inputs to a particular neuron.
    This is the way most biological neurons are wired up.
    In the machine learning world this is called feature engineering.
    You are computing a function on some set of features to create a new feature to represent your data point, in this case your diabetes patient.
    You could combine age, sex, and BMI to compute a body health score.
    You might combine LDL and HDL cholesterol levels with blood pressure to create a heart health score.
    And you might combine TCH and glucose blood test results with other blood test results to create a pancreas health score.
    But who is to say that our grouping is the best way to combine features.
    Just because it seems like these features go together, that doesn't mean that this is the best math to compute accurate predictions.
    What if diabetes severity depends on some nonlinear relationship between blood pressure and glucose level?
    We haven't put those two features together in our guess at the feature engineering for this problem.

    So in order to give our neural network all the flexibility or plasticity it needs to solve an unknown problem we need make it fully connected or dense.
    </aside>

# 20: Dense Network

<aside class="notes">
    If someone tells you that your neural net is dense, they aren't saying that it is dumb.
    They are just saying that it is well connected.
    In fact, a dense network is "fully connected."
    What that means, is that at each layer, each and every neuron in that layer is connected by a weight parameter to each and every neuron in the layer above.
    This is what creates that rectangular parameter or weight matrix that you are multiplying by the vector flowing in from the layer above.
    So that parameter or weight matrix needs to have as many outputs (rows) as you have neurons on the layer below.
    And your parameter or weight matrix between each layer of neurons should have as many inputs (columns) as you have neurons on the layer above.
    And each of these multiplications is just a linear transformation (a rotation and stretching) of the vector above to create a new vector for the layer below.
    This math is exactly the same as the math of a linear regression.
    There's no magic or deep learning here, unless you add a nonlinear *activation function* to your neurons in at least one of the layers.
    </aside>

# 21: Your Network is Dense

<aside class="notes">
    Your network is dense.
    And that is a good thing.
    It is fully connected.
    Biological brains are rarely arranged in neat layers like ours.
    But our fully connected layered networks will give our artificial neural networks the option of connecting each neuron to each other neuron in the neighboring layer.
    When training on data, your algorithm can turn off any connections that aren't helping the accuracy of your model by setting the coefficients to zero.
    And you can keep adding more layers and more neurons until the brain solves your problem.
    </aside>

# 22: Threshold Activation

<aside class="notes">
    So what activation function should you chose?
    In the early days, the inventor of the neural network, Rosenblat just used a threshold to create a binary output.
    This is because perceptrons were intended to be used to learn binary logic, the logic of computer programs and mathematical proofs.
    Rosenblatt and early researchers assumed that it would be best if each neuron just output a bit.
    But this turned out to be a bit too simple.

    Modern researchers have found that a Rectified Linear Unit or ReLU activation function is usually a better choice.
    Whether or not this is the kind of activation function that is happening at the synappses between neurons doesn't really matter.
    The dendrites and axons of our artificial neurons don't need to imitate real biological neurons.
    The artificial neural networks in our deep learning models just need to give us good predictions.
    </aside>

# 23: Dot Products in Python

<aside class="notes">
    Now that you know how to construct a good neural network, lets look at the math of making a prediction.
    Follow your data as it flows in from the top and down through the dot products of your model.
    Between each layer in an artificial neural network is a rectangular matrix of coefficients that is multiplied in a dot product with the vector of data flowing in from the layer above.
    Your blue feature values are multiplied by the red coefficients as they flow through your model.
    You have one of these multiplications and regression lines for each feature.
    This creates a new value that is the estimated severity change based on that feature.
    These new values are going to be added together to produce the total severity score prediction.
    So you can think of each calculation as bumping the score up or down a bit.

    This is the value of neural networks and deep learning.
    The outputs at each layer are the features you would otherwise have to engineer by hand.
    But a deep learning model can learn the formulas automatically from your data.
</aside>

# 24: Input 1 (age)

<aside class="notes">
    Your first input feature is age.
    Age is multiplied by the coefficient for the first layer, the first neuron and the first feature.
    This is the coefficient 0 comma 0 comma 0.
    </aside>

# 25: Input 2 (sex)

<aside class="notes">
    The next input feature for your model is sex.
    Sex is multiplied by the coefficient for the first layer, the first neuron and the second feature.
    This is stored in the coef_ matrix at position 0 comma zero comma 1.
    </aside>

# 26: Input 3-10 (bmi)

<aside class="notes">
    For features 3 through 10 the procedure is the same.
    This is just the math of a dot product, or a matrix product.
    </aside>

# 27: Layer 1: Intercept

<aside class="notes">
    In order to complete the math for this first layer we need add in the intercept value.
    This will produce z_0, the intermediate output value needed in the next layer down.
    </aside>

# 28: Layer 1: Neuron 1

<aside class="notes">
    The output of neuron 1 in the first layer is just the sum of all these values that we computed from the dot product of the coefficient matrix.
    Now you can complete the calculation for the first neuron in the first layer by computing the activation function on this sum to produce z zero comma zero.
    </aside>

# 29: Layer 1: Neuron 2

<aside class="notes">

    The output of neuron 2 in the first layer is just the dot product of the coefficients for this neuron with all those same input feature  from the input vector.

    </aside>

# 30: Layer 1: Neuron 3

<aside class="notes">

    The output of neuron 3 in the first layer is just the dot product of the coefficients for this third row in the coeficient matrix with input feature vector.

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

# 32: Backpropagation: Error Gradients

<aside class="notes">
    Backpropagation works by estimating the error gradients associated with each coefficient in each layer.
    First, the error in the prediction for an example in the training set is computed at the bottom of this chart.
    The true value from the training set is subtracted from the predicted value.
    The coefficients in the layer above can be adjusted small amounts to see how this affects the error below.
    And this gradient can be propagated back up the network to the next coefficient to measure it's affect on the error below.

</aside>

