# Flight Deal Finder
## Day 39 - Intermediate+ - \#100DaysOfCode

**To do:**
* Create a Flight Deal Finder

**Acceptance criteria:**
* Day 39
  * Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport 
  Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city 
  code, not the airport code see here.

  * Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in 
  the Google Sheet.

  * If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the 
  Twilio API.

  * The SMS should include the departure airport IATA code, destination airport IATA code, departure city, 
  destination city, flight price and flight dates.
    * e.g.
    ```
    Low price alert! Only €41 to fly from London-STN to Berlin-SXF, 
    from 2020-08-25 to 2020-09-10.
    ```

* Day 40
  * Create the Customer Acquisition Code
  * For some destinations, certain time periods, there will be no flights available. We need to add exception handling 
    to our code so that it doesn't break and crash in these situations.
  * If a flight is not found, check to see if there are flights with 1 stop
  * Notify our customers when there is a good deal

**APIs Required:**
* Google Sheet Data Management - https://console.developers.google.com/apis/library/sheets.googleapis.com/

* Flight Search API (Free Signup) - https://partners.kiwi.com/

* Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

* Twilio SMS API - https://www.twilio.com/docs/sms

**Screenshots:**

![]()
