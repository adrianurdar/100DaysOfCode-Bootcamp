# Analyse the Android App Store
## Day 75 - Advanced - \#100DaysOfCode

**To do:**
* Analyse the Android App Store

**Requirements:**
* How many rows and columns does `df_apps` have? What are the column names? Look at a random sample of 5 different  
  rows with `.sample()`

* Remove the columns called `Last_Updated` and `Android_Version` from the DataFrame. We will not use these columns. 

* How many rows have a NaN value (not-a-number) in the Ratings column? Create DataFrame called `df_apps_clean` that 
  does not include these rows. 

* Are there any duplicates in data? Check for duplicates using the `.duplicated()` function. How many entries can you 
  find for the "Instagram" app? Use `.drop_duplicates()` to remove any duplicates from `df_apps_clean`.

* Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings 
  alone to determine the quality of an app?

* What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you 
  think there could be limit in place or can developers make apps as large as they please? 

* Which apps have the highest number of reviews? Are there any paid apps among the top 50?

* How many apps had over 1 billion (that's right - BILLION) installations? How many apps just had a single install? 

* Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.
 
* Use the [plotly express examples from the documentation](https://plotly.com/python/line-and-scatter/) alongside 
  the [.scatter() API reference](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html) to 
  create a scatter plot. 

* How many different types of genres are there? Can an app belong to more than one genre? Check what happens when 
  you use .value_counts() on a column with nested values? See if you can work around this problem by using the 
  `.split()` function and the DataFrame's 
  [.stack() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html). 

* Can you create this chart with the Series containing the genre data? 

* Use the plotly express bar 
  [chart examples](https://plotly.com/python/bar-charts/#bar-chart-with-sorted-or-ordered-categories) and the 
  [.bar() API reference](https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar) 
  to create a bar chart

* Create a box plot that shows the number of Installs for free versus paid apps. How does the median number of 
  installations compare? Is the difference large or small?
