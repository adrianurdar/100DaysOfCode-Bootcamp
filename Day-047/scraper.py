import requests
from bs4 import BeautifulSoup


def scrape(product_url):
    res = requests.get(url=product_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    product_title = soup.select(
        "#main-container > section:nth-child(1) > div > div.page-header.has-subtitle-info > h1"
    )[0].get_text().strip()

    website_raw_price = soup.select("#main-container > section:nth-child(1) > div > div:nth-child(2) > "
                                    "div.col-sm-5.col-md-7.col-lg-7 > div > div > div.col-sm-12.col-md-6.col-lg-5 "
                                    "> form > div.product-highlight.product-page-pricing > div:nth-child(1) > div > "
                                    "div.w-50.mrg-rgt-xs > p.product-new-price")
    product_price = float(int(f"{website_raw_price[0].get_text().strip().split()[0].split('.')[0]}"
                              f"{website_raw_price[0].get_text().strip().split()[0].split('.')[1]}") / 100)

    return product_title, product_price
