import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

OCCAMS_ADVISORY_URL = os.getenv("OCCAMS_ADVISORY_URL", "https://www.occamsadvisory.com/")  # Load from .env or default


def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = soup.get_text(separator='\n', strip=True)
        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None


if __name__ == "__main__":
    website_data = scrape_website(OCCAMS_ADVISORY_URL)
    if website_data:
        print("Website content scraped successfully.")
        # You can save this to a file for inspection if needed
        # with open("website_content.txt", "w", encoding="utf-8") as f:
        #     f.write(website_data)
    else:
        print("Failed to scrape website content.")
