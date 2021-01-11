# Seaborn and Linear Regression
## Day 77 - Advanced - \#100DaysOfCode

**To do:**
* Find out if there's a relationship using the movie budgets and financial performance data that I've scraped from 
[the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**. 

<img src=https://i.imgur.com/kq7hrEh.png>

**Requirements:**
* Answer these questions about the dataset:
    1. How many rows and columns does the dataset contain?
    2. Are there any NaN values present?
    3. Are there any duplicate rows?
    4. What are the data types of the columns?

* Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format 
  by removing `$` signs and `,`.

* Convert the `Release_Date` column to a Pandas Datetime type.
 
* Answer the following questions:
    1. What is the average production budget of the films in the data set?
    2. What is the average worldwide gross revenue of films?
    3. What were the minimums for worldwide and domestic revenue?
    4. Are the bottom 25% of films actually profitable or do they lose money?
    5. What are the highest production budget and highest worldwide gross revenue of any film?
    6. How much revenue did the lowest and highest budget films make?

* How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that 
  grossed nothing?

* How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?

* Use the 
  [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to 
  accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but 
  made zero revenue in the United States. 
  
* Identify which films were not released yet as of the time of data collection (May 1st, 2018).
* How many films are included in the dataset that have not yet had a chance to be screened in the box office?
* Create another DataFrame called `data_clean` that does not include these films. 

* What is the percentage of films where the production costs exceeded the worldwide gross revenue?

* Try to create the following Bubble Chart:
<img src=https://i.imgur.com/8fUn9T6.png>

* Create a column in `data_clean` that has the decade of the release.
<img src=https://i.imgur.com/0VEfagw.png width=650> 
  
* Create two new DataFrames: `old_films` and `new_films`
    * `old_films` should include all the films before 1969 (up to and including 1969)
    * `new_films` should include all the films from 1970 onwards
    * How many films were released prior to 1970?
    * What was the most expensive film made prior to 1970?

* Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`. 

* Run a linear regression for the `old_films`. Calculate the intercept, slope and r-squared. How much of the 
  variance in movie revenue does the linear model explain in this case?
