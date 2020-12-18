from email_sender import send_email
from scraper import scrape

with open("products.txt") as file:
    content = file.readlines()

products = {line.split("/")[3]: {"url": line.split(",")[0], "price_limit": line.split(",")[1]} for line in content}

for key in products:
    product = scrape(products[key]["url"])
    product_title = product[0]
    product_price = product[1]

    message = f"{product_title}\n" \
              f"Price now: {product_price} lei\n" \
              f"{products[key]['url']}"

    if product_price < float(products[key]["price_limit"]):
        send_email(message_to_send=message)
