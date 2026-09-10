import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")
print(f"{len(books)} kitap bulundu")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    data.append({"title": title, "price": price, "availability": availability})

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print(df.head())