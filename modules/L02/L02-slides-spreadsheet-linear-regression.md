# Spreadsheet Linear Regression

- Training Data: Gender, Height, Weight
- Target: Weight

# Application

- Carnival game
- Clinic data-cleaning
- Diagnosis (BMI)

# Load data

1. Download data:
    - totalgood.org/midata/ucsd/height-weight-gender.csv
2. Upload data to Google sheet:
    - File menu heading -> Import -> Upload tab heading -> Select a file ...

# Descriptive Statistics

1. Select the "Height" column
2. Calculate the mean height (AVERAGE)

sheets_reg_02

2. To graph the data, we first need to select it in the spreadsheet. Left mouse click in cell A1. While holding the mouse button down, drag the cursor to cell B6.

sheets_reg_03

The data and labels at the top of the column should be highlighted.

3. From the Insert menu at the top of the window, select Chart.

sheets_reg_04

4. A window will appear that allows you to create a variety of different types of graphs including scatter plots.

sheets_reg_05

This window indicates where the data is located (A1:B6:) and indicates that the first rows contains headers or labels. There are several recommended chart, but none of them are scatter plots. To find a scatter plot, select Charts in the upper left corner of the window.

5. Select Scatter from the column of chart types on the left side of the window.

sheets_reg_06

6. In the next column, choose the scatter plot at the top.

sheets_reg_07

Now the preview on the right side of the window show a scatter plot.

7. To change the chart titles and axes labels, select Customize.

sheets_reg_08

Under Chart Title, you should put a name that describes your chart. You can also change the color and size of the chart title font.

8. Use the scroll bar in the middle of the window to move farther through the chart options. Look for Axis Horizontal.

sheets_reg_09

Give the horizontal axis an appropriate label under Title. You can also change the minimum and maximum extent of the graph by entering values into Min and Max.

9. Once you have given the horizontal axis a title, use the box next to Axis to choose Left Vertical.

sheets_reg_10

Give the vertical axis an appropriate label under Title. Like the horizontal axis, you can change the vertical extent of the axis using Min and Max.

10. You may also add a trendline to the scatter plot. To do this, scroll farther down in the Customize window. Under the area labeled Series, look for Trendline. Selecting the box to the right give you several choices of regression for the data.

sheets_reg_13

For example, select Linear to find the line of best fit. If you choose Use Equation for the Label and Show R2, the legend on the graph will show the equation as well as the coefficient of determination.

sheets_reg_11

Select Insert to place the scatter plot in the sheet.

sheets_reg_01

11. The equation in the legend may not include enough decimal places. If this is the case for a linear trend, the SLOPE and INTERCEPT commands may be used to calculate the slope and intercept of the trend. For this data, we would write

=SLOPE(B2:B6,A2:A6)

or

=INTERCEPT(B2:B6,A2:A6)

in a cell. Note that each of the functions require the range of the dependent variable to be listed first (B2:B6)and the range of the independent variable second (A2:A6).

12. If you need an output on the trend, the command FORECAST may be used. For instance, to find the y value on the linear trend at x = 130, we would type

=FORECAST(130,B2:B6,A2:A6)
