# Nobel Prize Analysis
## Day 78 - Advanced - \#100DaysOfCode

**To do:**
* Analyse the Nobel Prize winners data

**Requirements:**
* Preliminary data exploration. 
    * What is the shape of `df_data`? How many rows and columns?
    * What are the column names?
    * In which year was the Nobel Prize first awarded?
    * Which year is the latest year included in the dataset?
    * Are there any duplicate values in the dataset?
    * Are there NaN values in the dataset?
    * Which columns tend to have NaN values?
    * How many NaN values are there per column? 
    * Why do these columns have NaN values?
 
* Convert the `birth_date` column to Pandas `Datetime` objects
* Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.

* Create a [donut chart using plotly](https://plotly.com/python/pie-charts/) which shows how many prizes went to men 
  compared to how many prizes went to women. What percentage of all the prizes went to women?

* Who were the first 3 Women to Win the Nobel Prize?
    * What are the names of the first 3 female Nobel laureates? 
    * What did the win the prize for? 
    * What do you see in their `birth_country`? Were they part of an organisation?

* Find the Repeat Winners
    * Did some people get a Nobel Prize more than once? If so, who were they?

* Number of Prizes per Category
    * In how many categories are prizes awarded? 
    * Create a plotly bar chart with the number of prizes awarded by category. 
    * Use the color scale called `Aggrnyl` to colour the chart, but don't show a color axis.
    * Which category has the most number of prizes awarded? 
    * Which category has the fewest number of prizes awarded? 

    
* When was the first prize in the field of Economics awarded?
    * Who did the prize go to?

* Male and Female Winners by Category
    * Create a [plotly bar chart](https://plotly.com/python/bar-charts/) that shows the split between men and women by 
category. 
    * Hover over the bar chart. How many prizes went to women in Literature compared to Physics?

* Number of Prizes Awarded Over Time
    * Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually. 
    * Count the number of prizes awarded every year. 
    * Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).
    * Using Matplotlib superimpose the rolling average on a scatter plot.
    * Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy). 

<img src=https://i.imgur.com/4jqYuWC.png width=650>

* Use the [named colours](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) to draw the data points in 
  `dogerblue` while the rolling average is coloured in `crimson`. 

<img src=https://i.imgur.com/u3RlcJn.png width=350>

* Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out? 
* What could be the reason for the trend in the chart?

* Are More Prizes Shared Than Before?
    * Investigate if more prizes are shared than before.
    * Calculate the average prize share of the winners on a year by year basis.
    * Calculate the 5 year rolling average of the percentage share.
    * Modify the code to add a secondary axis to your Matplotlib chart.
    * Plot the rolling average of the prize share on this chart. 
    * See if you can invert the secondary y-axis to make the relationship even more clear. 

* The Countries with the Most Nobel Prizes
    * Create a Pandas DataFrame called `top20_countries` that has the two columns. The `prize` column should contain 
      the total number of prizes won.
      
<img src=https://i.imgur.com/6HM8rfB.png width=350>

* Is it best to use `birth_country`, `birth_country_current` or `organization_country`? 
* What are some potential problems when using `birth_country` or any of the others? Which column is the least 
  problematic? 
* Then use plotly to create a horizontal bar chart showing the number of prizes won by each country.

<img src=https://i.imgur.com/agcJdRS.png width=750>

* What is the ranking for the top 20 countries in terms of the number of prizes?

* Use a Choropleth Map to Show the Number of Prizes Won by Country
    * Create this choropleth map using [the plotly documentation](https://plotly.com/python/choropleth-maps/):

<img src=https://i.imgur.com/s4lqYZH.png>

* Experiment with [plotly's available colours](https://plotly.com/python/builtin-colorscales/).

* In Which Categories are the Different Countries Winning Prizes?
    * See if you can divide up the plotly bar chart you created above to show the which categories made up the total 
  number of prizes. Here's what you're aiming for:

<img src=https://i.imgur.com/iGaIKCL.png>

* In which category are Germany and Japan the weakest compared to the United States?
* In which category does Germany have more prizes than the UK?
* In which categories does France have more prizes than Germany?
* Which category makes up most of Australia's nobel prizes?
* Which category makes up half of the prizes in the Netherlands?
* Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?

* Number of Prizes Won by Each Country Over Time
    * When did the United States eclipse every other country in terms of the number of prizes won? 
    * Which country or countries were leading previously?
    * Calculate the cumulative number of prizes won by each country in every year. Again, use the 
      `birth_country_current` of the winner to calculate this. 
    * Create a [plotly line chart](https://plotly.com/python/line-charts/) where each country is a coloured line. 

* What are the Top Research Organisations?
    * Create a bar chart showing the organisations affiliated with the Nobel laureates.

<img src=https://i.imgur.com/zZihj2p.png width=600>

* Which organisations make up the top 20?
* How many Nobel prize winners are affiliated with the University of Chicago and Harvard University?

* Which Cities Make the Most Discoveries?
    * Where do major discoveries take place?
    * Create another plotly bar chart graphing the top 20 organisation cities of the research institutions associated 
      with a Nobel laureate. 
    * Where is the number one hotspot for discoveries in the world?
    * Which city in Europe has had the most discoveries?

* Where are Nobel Laureates Born? Chart the Laureate Birth Cities
    * Create a plotly bar chart graphing the top 20 birth cities of Nobel laureates. 
    * Use a named colour scale called `Plasma` for the chart.
    * What percentage of the United States prizes came from Nobel laureates born in New York? 
    * How many Nobel laureates were born in London, Paris and Vienna? 
    * Out of the top 5 cities, how many are in the United States?

* Plotly Sunburst Chart: Combine Country, City, and Organisation
    * Create a DataFrame that groups the number of prizes by organisation. 
    * Then use the [plotly documentation to create a sunburst chart](https://plotly.com/python/sunburst-charts/)
    * Click around in your chart, what do you notice about Germany and France? 

* Patterns in the Laureate Age at the Time of the Award
    * How Old Are the Laureates When the Win the Prize?
    * Who were the oldest and youngest winners?
    * What are the names of the youngest and oldest Nobel laureate? 
    * What did they win the prize for?
    * What is the average age of a winner?
    * 75% of laureates are younger than what age when they receive the prize?
    * Use Seaborn to [create histogram](https://seaborn.pydata.org/generated/seaborn.histplot.html) to visualise the 
      distribution of laureate age at the time of winning. Experiment with the number of `bins` to see how the 
      visualisation changes.

* Descriptive Statistics for the Laureate Age at Time of Award
    * Calculate the descriptive statistics for the age at the time of the award. 
    * Then visualise the distribution in the form of a histogram using 
      [Seaborn's .histplot() function](https://seaborn.pydata.org/generated/seaborn.histplot.html).
    * Experiment with the `bin` size. Try 10, 20, 30, and 50.
    * Are Nobel laureates being nominated later in life than before? Have the ages of laureates at the time of the 
      award increased or decreased over time?
    * Use Seaborn to 
      [create a .regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html?highlight=regplot#seaborn.regplot) 
      with a trendline.
    * Set the `lowess` parameter to `True` to show a moving average of the linear fit.
    * According to the best fit line, how old were Nobel laureates in the years 1900-1940 when they were awarded the 
      prize?
    * According to the best fit line, what age would it predict for a Nobel laureate in 2020?

* Winning Age Across the Nobel Prize Categories
    * How does the age of laureates vary by category?
    * Use Seaborn's 
      [`.boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot) to 
      show how the mean, quartiles, max, and minimum values vary across categories. Which category has the longest 
      "whiskers"? 
    * In which prize category are the average winners the oldest?
    * In which prize category are the average winners the youngest?
    * Use Seaborn's 
      [`.lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html?highlight=lmplot#seaborn.lmplot) and the 
      `row` parameter to create 6 separate charts for each prize category. Again set `lowess` to `True`.
    * What are the winning age trends in each category? 
    * Which category has the age trending up and which category has the age trending down? 
    * Is this `.lmplot()` telling a different story from the `.boxplot()`?
    * Create another chart with Seaborn. This time use `.lmplot()` to put all 6 categories on the same chart using the 
      `hue` parameter. 
