import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    print("🕸️ Starting Scraper...")
    
    # TODO 1: Send a GET request to the URL
    url = "http://quotes.toscrape.com/"
    # response = ...

    # TODO 2: Parse the HTML content
    # soup = ...

    # TODO 3: Find all quote elements
    # quotes = ...

    # TODO 4: Loop through quotes and extract text/author
    # for quote in quotes:
    #     text = ...
    #     author = ...
    #     print(f"{text} - {author}")

    print("✅ Done!")

if __name__ == "__main__":
    scrape_quotes()
