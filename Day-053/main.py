from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ZILLOW_URL = "https://www.imobiliare.ro/vanzare-case-vile/brasov?id=5162684"
FORM_URL = "https://forms.gle/1VQUuRcoh1qvndVs5"

# Use BeautifulSoup/Requests to scrape all the listings from Zillow.
res = requests.get(url=ZILLOW_URL)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

# Create a list of links for all the listings you scraped.
all_links = [item["href"] for item in soup.select("h2 > a")]

# Create a list of prices for all the listings you scraped.
all_prices = [int(item.get_text().replace(".", "")) for item in soup.find_all("span", {"class": "pret-mare"})]

# Create a list of addresses for all the listings you scraped.
all_addr = [item.get_text().strip() for item in soup.find_all("div", {"class": "localizare"})]

# Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/
#  link added to the form. You will need to fill in a new form for each new listing.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url=FORM_URL)
sleep(2)

# Fill in the address
for i in range(len(all_addr)):
    # Fill in the address
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(all_addr[i])

    # Fill in the price
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(all_prices[i])

    # Fill in the link
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ).send_keys(all_links[i])

    # Submit the form
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
    sleep(2)

    # Send another answer
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    sleep(1)
    print(i)

driver.quit()
