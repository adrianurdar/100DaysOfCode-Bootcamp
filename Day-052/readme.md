# Instagram Follower Bot
## Day 52 - Intermediate+ - \#100DaysOfCode

**To do:**
* Create an automated Instagram Follower Bot

**Requirements:**
* Step 1 - Get Your Instagram Credentials
    * Set up your Instagram account: https://www.instagram.com/
    * Figure out which account you would like to target. (Pick a large account that has a lot of followers).
    
* Step 2 - Create a Class
    * Create a class called InstaFollower
    * In the init() method, create the Selenium driver .
    * Create three methods - login() and find_followers() and follow().
    * Outside of the class, initialise the object and call the three methods in order.
    
* Step 3 - Login to Instagram
    * Use Selenium and Python to login to Instagram automatically using your email and password. 
      Write your code in the login() method.
      
* Step 4 - Find the followers of the target account
    * The list of followers in the popup is limited to around 15 when it first loads, in order to see more followers, 
      scroll down in the popup
      
* Step 5 - Follow all the followers
    * Inside the follow() method find all the follow buttons in the modal (popup) and click on each of them in turn. 
      
    * Add a 1 second delay between each click, so you can seem more human.
