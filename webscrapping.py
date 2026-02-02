import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

# Create CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        # Product name
        name = product.h3.a["title"]

        # Price
        price = product.find("p", class_="price_color").text

        # Rating
        rating = product.find("p", class_="star-rating")["class"][1]

        # Write data to CSV
        writer.writerow([name, price, rating])

print("✅ Data scraped successfully and saved to products.csv")
