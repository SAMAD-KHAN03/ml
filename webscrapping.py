# Import all the necessary libraries
import requests                     # To send HTTP requests and get web pages
from bs4 import BeautifulSoup        # To extract (parse) data from HTML pages
import pandas as pd                  # To store and save data in table format (DataFrame)
from urllib import robotparser       # To check if the website allows scraping

# ----------------------------------------------------------
# STEP 1: Check if website allows scraping using robots.txt
# ----------------------------------------------------------

# Create a robot parser object
rp = robotparser.RobotFileParser()

# Provide the URL of the website's robots.txt file
rp.set_url("http://books.toscrape.com/robots.txt")

# Read and parse the robots.txt file
rp.read()

# Check if we are allowed to scrape the catalogue pages
if not rp.can_fetch("*", "/catalogue/"):
    print("❌ Scraping not allowed")
else:
    print("✅ Scraping allowed")

    # ----------------------------------------------------------
    # STEP 2: Prepare to store the scraped data
    # ----------------------------------------------------------
    books_data = []  # This list will hold all the book details we collect

    # ----------------------------------------------------------
    # STEP 3: Loop through multiple pages of the site
    # ----------------------------------------------------------
    # The site has pages like:
    # http://books.toscrape.com/catalogue/page-1.html
    # http://books.toscrape.com/catalogue/page-2.html
    # and so on...
    for page in range(1, 6):  # Scrape first 5 pages
        # Send a GET request to the page
        response = requests.get(f"http://books.toscrape.com/catalogue/page-{page}.html")

        # Convert the HTML content into a BeautifulSoup object
        # 'html.parser' helps us navigate and extract data from the HTML page
        soup = BeautifulSoup(response.text, "html.parser")

        # ----------------------------------------------------------
        # STEP 4: Extract data for each book on the page
        # ----------------------------------------------------------
        # Each book on the website is inside an <article> tag with class 'product_pod'
        for book in soup.find_all("article", class_="product_pod"):

            # From each book block, extract:
            # - Title (inside <h3> tag -> <a> tag -> 'title' attribute)
            # - Price (inside <p> tag with class 'price_color')
            # - Rating (inside <p> tag whose class indicates rating like 'star-rating Three')
            books_data.append({
                "title": book.h3.a["title"],
                "price": float(book.find("p", class_="price_color").text[2:]),  # Remove currency symbol (£)
                "rating": book.p["class"][1]  # The second class value is the rating word
            })
    df = pd.DataFrame(books_data)
    df.to_csv("datasets/books_dataset.csv", index=False)
    print(df.head())