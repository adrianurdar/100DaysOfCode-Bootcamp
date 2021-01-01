# Flask Authentication
## Day 68 - Advanced - \#100DaysOfCode

**To do:**
* Create a website to register, login and logout users with email and password.

**Requirements:**
* Allow users to register with their name, email and password
  
* Once a user is registered, redirect them straight to the `secrets.html` page.

* The `secrets.html` page should say `"Hello <insert name>"`, where the name they typed in the registration form is 
  displayed.

* When the user accesses the `secrets.html` page, they should be able to download a secret file.

* Both the `/secrets` and `/download` route need to be secured so that only authenticated users can access them.

* If the user's email doesn't exist in the database, you send them a Flash message to let them know and redirect 
  them back to the login route
  
* If the password does not match, you send a Flash message to the user when you redirect them back to 
  the login page
  
* When a user is logged in, the home page should not show the login/register buttons
  
**Screenshots:**

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.17.31%20PM.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.18.04%20PM.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.18.18%20PM.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.18.47%20PM.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.19.07%20PM.png)

![](https://github.com/adrianurdar/100DaysOfCode-Bootcamp/blob/main/Day-068/screenshots/Screen%20Shot%202021-01-01%20at%2010.19.23%20PM.png)
