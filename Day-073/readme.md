# Analyse a Dataset of LEGO Pieces
## Day 73 - Advanced - \#100DaysOfCode

**To do:**
* Analyse a dataset of lego pieces

**Requirements:**
* What is the most enormous LEGO set ever created and how many parts did it have?

* How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the  
  company sell when it first launched?

* Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked  
  Harry Potter or Marvel Superheroes?

* When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based 
  on how many themes and sets did it released year-on-year?

* Did LEGO sets grow in size and complexity over time? Do older LEGO sets tend to have more or fewer parts than 
  newer sets?
  
* How many different colours does the LEGO company produce?

* Find the number of transparent colours where `is_trans == 't'` versus the number of opaque colours 
  where `is_trans == 'f'`.

* Read the sets.csv data and take a look at the first and last couple of rows.

* In which year were the first LEGO sets released and what were these sets called?

* How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the 
  year the company started?

* Find the top 5 LEGO sets with the most number of parts.

* Use `.groupby()` and `.count()` to show the number of LEGO sets released year-on-year. How 
  do the number of sets released in 1955 compare to the number of sets released in 2019?

* Show the number of LEGO releases on a line chart using Matplotlib.

* Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 
2020 and 2021).

* Use the `.groupby()` and `.agg()` function together to figure out the average number of 
  parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?

* Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number 
  of parts over time using a Matplotlib scatter plot.

* Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many <code>id</code>s 
  correspond to this name in the themes.csv? Now use these `id`s and find the corresponding the sets in the sets.csv

**Screenshots:**

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-08_59_39.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-08_59_55.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-09_00_09.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-09_00_27.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-09_06_59.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-04-09_07_17.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-05-08_40_52.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-05-08_55_22.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-05-09_08_00.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-073/screenshots/screencapture-colab-research-google-drive-1jgoTgaOxbtSLnte3P63VlZ4fQ8jVxLY5-2021-01-05-09_19_09.png)
