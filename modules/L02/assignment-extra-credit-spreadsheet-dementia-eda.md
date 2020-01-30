# Dementia Spreadsheet EDA

- download dementia treatment data: https://github.com/totalgood/dsdh/blob/master/notebooks/data/iq-test-scores-gender-age.xls?raw=true
- load dementia treatment data into LibreOffice or Google Sheets
- combine first and second rows that contain headers to create unique variable names for each column in a single header row
- Compute the mean and standard deviation of all numerical columns to 2 decimal places
- Notice the #DIV/0 error and correct it by changing all numerical cells to the "Number" format
- reduce the digits of precision on all numerical cells so that only integer values are displayed for the original source data rows (leave your descriptive statistics, std and mean rows, with 2-decimal precision)
- create a numerical binary indicator variable for gender
- create a total VFT score (combine 3 scores) for the beginning of treatment group
- create a total VFT score (combine 3 scores) for the after six-months treatment group
- create a "VFT_diff" column showing the change over six months in your total VFT score
- verify that all the 0s and 1 numerical values in your sex indicator variable are correct
- plot two histograms of your VFT_diff column, one for boys and one for girls
- plot two histograms of your VFT_diff column, one for children with age >= 14 and another for age <= 13
- compute the mean VFT_diff for each of the 4 groups of patients that you plotted histograms of: Boys 14 and older, Boys 13 and younger, Girls 14 and older, Girls 13 and younger
- notice that you don't have any data for boys 13 and younger, can you think of a way to guess at (extrapolate) a 12 year old Boy's VFT_diff score based on the data you have for Girls?
- create a decision tree model with 2 decisions (4 leaves) that predicts a childs VFT_diff based on their age and gender using your two histograms
