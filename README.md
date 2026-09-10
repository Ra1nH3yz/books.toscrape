# Books Scraper

A Python web scraper built with requests and BeautifulSoup that extracts book data from books.toscrape.com.

## What it does
Scrapes the book listing page, extracts the title, price, and stock availability for each book, and saves the results to `books.csv`.

## Libraries used
- requests — for fetching page content
- BeautifulSoup4 — for parsing HTML
- pandas — for writing the results to CSV

## Running it
pip install requests beautifulsoup4 pandas
python scraper.py