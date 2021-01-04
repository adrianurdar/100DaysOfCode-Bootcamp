# Analyse the Popularity of Different Programming Languages over Time
## Day 72 - Advanced - \#100DaysOfCode

**To do:**
* Analyse the Popularity of Different Programming Languages over Time

**Requirements:**
* Data Exploration
    * Read the .csv file and store it in a Pandas dataframe
    * Examine the first 5 rows and the last 5 rows of the dataframe
    * Check how many rows and how many columns there are. What are the dimensions of the dataframe?
    * Count the number of entries in each column of the dataframe
    * Calculate the total number of post per language. Which Programming language has had the highest total number of 
      posts of all time?
    * Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in 
      September 2008.
    * How many months of data exist per language? Which language had the fewest months with an entry? 
    
* Data Cleaning
    * Change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"

* Data Manipulation
    * What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column 
      names and print out the first 5 rows of the dataframe.
    * Count the number of entries per programming language. Why might the number of entries be different?

* Data Visualisation with Matplotlib 
  
    * Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 
      to plot a single programming language (e.g., java) on a chart.

    * Show two line (e.g. for Java and Python) on the same chart.

* Smoothing out Time Series Data

    * Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an 
      average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time 
      and move it forward by one overservation. Pandas has two handy methods already built in to work this out: 
      [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and 
      [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html).

**Screenshots:**

![]()

![]()

![]()

![]()

![]()

![]()

![]()

![]()

![]()

![]()
