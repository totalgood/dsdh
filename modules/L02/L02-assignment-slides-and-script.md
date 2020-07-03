# 1: Assignment: Spreadsheet Linear Modeling

# 2: Dataset Spreadsheet: bit.ly/ucsd-spreadsheet

![Image of totalgood/dsdh raw/download buttons](media/assignment-github-spreadsheet-download.png)

<aside class="notes">
    Visit the  bit.ly url in red to retrieve the Libre Office Open Calc spreadsheet which contains the data for this assignment.
    You can also find it on github within the totalgood organization at the `dsdh` repository and the `data/` directory.
    DSDH stands for datascience for digital health.
    If you do not have Libre Office you can download it for free and install it to run this spreadsheet directly.
    Alternatively you can upload it to Google Sheets, which is also free.
    If you have a Microsoft Office or Office 360 license on your machine you may be able to import it into Excel.
</aside>

# Dataset Columns

A: Patient ID (integer, but not usable, unique for each)
B: Gender (“Male’/”Female”), text feature
C: Height (in), continuous numerical feature
D: Weight (lbs), continuous numerical target (regression)

<aside class="notes">
    A: The first column is not usable for modeling because it is unique and has no relationship with the target variable (weight).
    B: Gender is provided as a text field but you will create a binary 0/1 integer field when you use it for the multivariate linear regression.
    C: Height is the main feature for this model because it contains the strongest relationship to our target variable, weight.
    D: Weight is your target variable. Because it is a continuous numerical variable, this problem is called a regression problem.
</aside>

# 4 Assignment Goals

Descriptive Statistics: Min, Max, Mean, Standard Deviation
Scatter Plot
Linear Regression (by manual trial and error)
Multivariate Linear Regression

<aside class="notes">
   In this assignment you will first compute some descriptive statistics to get to know your data.
   You will then plot a scatter plot.

   Templates for each of these objectives are provided in tabs with appropriate labels.
</aside>

# 5: Example Descriptive Statistics and Scatter Plot

<aside class="notes">
    A template for your statistics and plots is provided in the tab titled "gender-height-weight-viz".

    Examples descriptive statistics for your dataset are shown here, but you'll need to calculate them yourself using built in formulas in your spreadsheet program.


    For the scatter plot, make sure you label your axes.
    Because weight is your target or dependent variable you should plot it on the vertical Y axis.
    Height is one of your independent or feature variables so you should plot it on the horizontal X axis.
    You may also examine your plot to estimate the slope of the relationship between height and weight.
    This will help you "fit" the linear regression model more quickly.

    A histogram is also provided for your reference.
    You may want to increase the number of bins from 3 to 10 in order to get a feel for the difference in the distribution of weight values for Male and Female patients.
</aside>

# 6: Example Linear Regression

<aside class="notes">
    A template for your linear regression model is provided in the tab titled "height-weight-regression".

    The values in green are for you to adjust using trial and error and your intuition.

    The linear formula for the line has already been implemented for you in column D.
    The error calculations and total MSE (mean square error) has also already been calculated for you.
    You only need to guess at slope and intercept values that can improve the model fit by reducing the MSE value.

    One guessing procedure that works well is to adjust the slope value (cell J3).
    This will make the total error in cell E3 go up or down.
    You can then compensate for this total error by subtracting this value from your intercept parameter in cell I3.
    It's possible to bring the average exactly to zero.
    This is the bias of your model or how your pattern of predictions is centered around the true values.
    However your MSE will change as well.
    If it gets worse (goes up), then you'll want to go in the other direction with the slope (the value in cell J3) for your next guess.
    With each pair of guesses for the slope and intercept manually record your results as a row in the table directly below starting at I6.
    This will help you see patterns in your answers and help you refine your solution.
    You may be able to get below 145 RMSE.
</aside>

# 6: Template for Regression

<aside class="notes">
    You will delete the green boxes with some of the instructions mentioned here.
    They are just to reminders.

    </aside>

# 7: Example Multivariate Regression

<aside class="notes">
    The multivariate regression tab adds two more columns to your table to allow you to incoporate gender into your linear formula to predict weight.
    You will now have slopes for both height and gender.
    But you will need to convert the gender text feature to a numerical binary feature to use it within a data science model.
</aside>

# 8: Example for Multivariate Regression

<aside class="notes">
    The multivariate regression tab adds two more columns to your table to allow you to incoporate gender into your linear formula to predict weight.
    You will now have slopes for both height and gender.
    But you will need to convert the gender text feature to a numerical binary feature to use it within a data science model.
</aside>

# 9: Template for Multivariate Regression

<aside class="notes">
    The green boxes show you where you need to change the values or formulas to get the multivariate regression working.
    For the multivariate linear regression you will first want to create a binary variable for the Gender.
    You will have a value of 1 for Female and 0 for Male.
    You will copy this formula (IF statement) into all of the rows within this column so that you can use this as a new feature in your linear regression model.

    After this you will add a third term to the existing linear regression model terms for the height slope and the intercept.
    This will be the slope for your IsFemale variable.

    Once you've copied this new prediction formula into the entire prediciton cell, you can then begin guessing at parameters for your model, like the slope for the IsFemale feature.
    Because there are not 3 parameters to balance, you challenge will be much more difficult. But it should be able to improve upon the RMSE you achieved in the previous tab for the single-variate linear regression.
</aside>
