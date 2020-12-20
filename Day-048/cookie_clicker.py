from datetime import datetime, timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a bot using Selenium and Python to click on the cookie as fast as possible.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = datetime.now() + timedelta(seconds=5)
end_game = datetime.now() + timedelta(minutes=5)

while True:
    cookie.click()

    # Every 5 seconds:
    if datetime.now() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = datetime.now() + timedelta(seconds=5)

    # After 5 minutes stop the bot and check the cookies per second count.
    if datetime.now() > end_game:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
