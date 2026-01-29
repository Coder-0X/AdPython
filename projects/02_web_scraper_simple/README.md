# 🕷️ Project: Simple Web Scraper

## Goal
Build a Python script that scrapes a website to get some data.
You will practice:
1.  **Fetching** HTML using `requests`.
2.  **Parsing** HTML using `BeautifulSoup`.
3.  **Extracting** specific information (like quotes or titles).
4.  **Saving** the data to a CSV file.

## The Mission
Your target is the "Quotes to Scrape" website: [http://quotes.toscrape.com/](http://quotes.toscrape.com/)

**Your script should:**
1.  Connect to the website.
2.  Find all the quotes on the first page.
3.  Print the quote and the author name.
4.  (Bonus) Save them into a file called `my_quotes.csv`.

## Helpful Snippets
```python
import requests
from bs4 import BeautifulSoup

# Get the page
response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

# Find elements (Hint: quotes are in <div class="quote">)
quotes = soup.find_all("div", class_="quote")
```

Good luck!
