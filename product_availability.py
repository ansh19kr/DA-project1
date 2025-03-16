import requests
from bs4 import BeautifulSoup
import time

# Set headers to mimic a browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def check_product_availability(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to retrieve page")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract product title
    title = soup.find("span", attrs={"id": "productTitle"})
    title = title.get_text(strip=True) if title else "Title Not Found"
    
    # Extract product price
    price = soup.find("span", class_="a-price-whole")
    price = price.get_text(strip=True) if price else "Price Not Found"
    
    # Extract availability
    availability = soup.find("div", id="availability")
    availability = availability.get_text(strip=True) if availability else "Availability Not Found"
    
    return {
        "title": title,
        "price": price,
        "availability": availability
    }

if __name__ == "__main__":
    product_url = input("Enter the Amazon product URL: ")
    while True:
        product_info = check_product_availability(product_url)
        if product_info:
            print(f"Product: {product_info['title']}")
            print(f"Price: {product_info['price']}")
            print(f"Availability: {product_info['availability']}")
        
        print("Checking again in 10 minutes...")
        time.sleep(600)  # Wait 10 minutes before checking again
