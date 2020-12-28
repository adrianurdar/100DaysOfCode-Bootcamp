# Blog Capstone Project (Part 2)
## Day 59 - Advanced - \#100DaysOfCode

**To do:**
* Build a blog website with these features:
    * Multi-page website with an interactive navigation bar
    * Dynamically generated blog post pages with full screen titles
    * Fully mobile responsive with an adaptive navigation bar
    
**Requirements:**
* Step 1 - Download the starting project
    * Head over to Start Bootstrap's website and download the Clean Blog Template: 
      https://startbootstrap.com/previews/clean-blog/

    * Unzip the downloaded file and rename the folder to "upgraded blog"
    
    * Open the project folder in PyCharm and:
        * Create the static and templates folders.
        * Move the files in the project to the correct folders (HTML files to templates and all folders to static).
        * Delete the mail folder. We're going to be coding up the functionality from scratch.
        * Create a `header.html` and `footer.html` file and the all important `main.py`.
    
* Step 2 - Get the home page to work
    * Use what you have learnt about Flask, get the home page to render when you go to http://localhost:5000 in your 
      browser.
      
* Step 3 - Fix the header and footer
    * Notice that at the moment the styling is completely missing. This is because the static files 
      (CSS/JS/images etc.) are served up by our server and they are no longer at the locations specified in the header.
    * Fix the header in `index.html` so that the styling and bootstrap all appear.
    * Fix the footer resources so that the Javascript works. You can verify this by checking that when you scroll the 
      navigation bar becomes sticky at the top and changes background color
      
* Step 4 - Using Jinja Include for Render Templates
    * Remove the `<head>` & navigation code from index.html and place it in the header.html file.
    * Remove the `<footer>` from index.html and place it in the footer.html file.
    * Using the above documentation, use include to make the website still function exactly the same as before.
    
* Step 5 - Make the About and Contact Pages Work
    * Delete the navigation bar item that points to the "Sample Post"
    * Update main.py and the about.html and contact.html files so that when you click on the About link in the  
      navigation bar it goes to the About page and likewise with the Contact page.
    * See if you can make the static images work on the About and Contact pages.
    
* Step 6 - Fetch and render the blog posts from an API
    * In main.py get hold of the json data at the above API endpoint.
    * Use the data from the API to render the home page, replacing the title, subtitle, author and dates of each 
      blog post with the data from the API.
      
* Step 7 - Rendering Individual Posts
    * Render each individual post in the post.html page.
    * When a user clicks on a particular post title on the home page (index.html), we should take them to the post.
      html page where the title/subtitle/image/date/author/body of the post is shown.

**Screenshots:**

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-059/screenshots/screencapture-127-0-0-1-5000-2020-12-28-10_05_36.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-059/screenshots/screencapture-127-0-0-1-5000-about-2020-12-28-10_06_01.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-059/screenshots/screencapture-127-0-0-1-5000-contact-2020-12-28-10_06_17.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-059/screenshots/screencapture-127-0-0-1-5000-post-1-2020-12-28-10_06_31.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-059/screenshots/screencapture-127-0-0-1-5000-post-2-2020-12-28-10_06_49.png)
