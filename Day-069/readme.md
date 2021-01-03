# Blog Capstone Project (Part 4 - Adding Users)
## Day 69 - Advanced - \#100DaysOfCode

**To do:**
* Allow users to register and login to the blog

**Requirements:**
* Allow users to go to the /register route to sign up to your blog website

* Users who have been successfully registered (added to the user table in the database) should be able to go to the 
  `/login` route to use their credentials to log in
  
* In the `/register` route, if a user is trying to register with an email that already exists in the database then 
  they should be redirected to the `/login` route and a flash message used to tell them to log in with that email 
  instead
  
* In the `/login` route, if a user's email does not exist in the database or if their password does not match then 
  they should be redirected back to `/login` and a flash message should let them know what they issue was and ask 
  them to try again
  
* When the user clicks on the LOG OUT button, it logs them out and takes them back to the home page

* Only the admin should be able to create, edit or delete posts

* Allow users to leave a comment and save the comment

* Display all the comments associated with the blog post

**Demo:**

* [](https://adrian-flask-blog.herokuapp.com/)
