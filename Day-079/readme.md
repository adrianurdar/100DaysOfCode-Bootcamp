# Dr Semmelweis Handwashing Discovery
## Day 79 - Advanced - \#100DaysOfCode

**To do:**
* Analyse the same data collected by Dr Semmelweis from 1841 to 1849.


**Requirements:**
* How dangerous was childbirth in the 1840s in Vienna?
    * Using the annual data, calculate the percentage of women giving birth who died throughout the 1840s at the 
      hospital.
      
* Create a [Matplotlib chart](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html) with twin y-axes.
  It should look something like this:

<img src=https://i.imgur.com/F9DOJxx.png width=700>

* Use plotly to create line charts of the births and deaths of the two different clinics at the Vienna General 
  Hospital. 
    * Which clinic is bigger or more busy judging by the number of births?
    * Has the hospital had more patients over time? 
    * What was the highest number of deaths recorded in clinic 1 and clinic 2?

* Calculate the proportion of maternal deaths per clinic. That way we can compare like with like. 
    * Work out the percentage of deaths for each row in the `df_yearly` DataFrame by adding a column called 
      "pct_deaths". 
    * Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the 
      total number of births).
    * Create another plotly line chart to see how the percentage varies year over year with the two different clinics.
    * Which clinic has a higher proportion of deaths?
    * What is the highest monthly death rate in clinic 1 compared to clinic 2?


* Date when handwashing was made mandatory
    * Add a column called "pct_deaths" to `df_monthly` that has the percentage of deaths per birth for each row. 
    * Create two subsets from the `df_monthly` data: before and after Dr Semmelweis ordered washing hand.
    * Calculate the average death rate prior to June 1947.
    * Calculate the average death rate after June 1947.

* Create a DataFrame that has the 6 month rolling average death rate prior to mandatory handwashing.

* Modify the Matplotlib chart from before to plot the monthly death rates (instead of the total number of births and 
  deaths). The chart should look something like this:

<img src=https://i.imgur.com/X6TQe0R.png width=500>

* Calculate the Difference in the Average Monthly Death Rate
    * What was the average percentage of monthly deaths before handwashing? 
    * What was the average percentage of monthly deaths after handwashing was made obligatory?
    * By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?
    * How do these numbers compare to the average for all the 1840s that we calculated earlier? 
    * How many times lower are the chances of dying after handwashing compared to before?
    
* Use [NumPy's `.where()` function](https://numpy.org/doc/stable/reference/generated/numpy.where.html) to add a column 
  to `df_monthly` that shows if a particular date was before or after the start of handwashing. 
    * Then use plotly to create box plot of the data before and after handwashing. 
    * How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy?

* Create a [plotly histogram](https://plotly.com/python/histograms/) to show the monthly percentage of deaths.
    * Use docs to check out the available parameters. Use the 
      [`color` parameter](https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html) to display 
      two overlapping histograms.
    * The time period of handwashing is shorter than not handwashing. Change `histnorm` to `percent` to make the time 
      periods comparable. 
    * Make the histograms slighlty transparent
    * Experiment with the number of bins on the histogram. Which number work well in communicating the range of 
      outcomes?
    * Just for fun, display your box plot on the top of the histogram using the `marginal` parameter. 

* Use [Seaborn's `.kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) to create two kernel 
  density estimates of the `pct_deaths`, one for before handwashing and one for after.
    * Use the `shade` parameter to give your two distributions different colours. 
    * What weakness in the chart do you see when you just use the default parameters?
    * Use the `clip` parameter to address the problem. 

* Use a t-test to determine if the differences in the means are statistically significant or purely due to chance.
    * Use the 
      [`.ttest_ind()` function](https://docs.scipy.org/]doc/scipy/reference/generated/scipy.stats.ttest_ind.html) to 
      calculate the t-statistic and the p-value
    * Is the difference in the average proportion of monthly deaths statistically significant at the 99% level? 
