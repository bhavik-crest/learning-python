import requests
from bs4 import BeautifulSoup


#################################################### Quotes ####################################################
# Step 1: Make a request to the page
url = "https://quotes.toscrape.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error if request failed

    # Step 2: Parse the HTML with BeautifulSoup
    quoteList = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract the data you want (example: all quotes)
    quotes = quoteList.find_all('span', class_='text')

    for quote in quotes:
        print(quote.text)

except requests.exceptions.HTTPError as http_err:
    print(f"For Quotes : HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("For Quotes : Error connecting. Please check your network.")
except requests.exceptions.Timeout:
    print("For Quotes : Timeout error: The request took too long to complete.")
except requests.exceptions.RequestException as err:
    print(f"For Quotes : An unexpected error occurred: {err}")



#################################################### Books ####################################################
# Step 1: Make a request to the page
url = "https://books.toscrape.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error if request failed

    # Step 2: Parse the HTML with BeautifulSoup
    bookList = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract the data you want (example: all quotes)
    books = bookList.find_all('article', class_='product_pod')

    # Step 4: Set empty array to hold book data
    books_data = []

    # Step 5: Loop through each book and extract title, price, and image URL
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        image = book.find('div', class_='image_container').a.img['src']
        image_url = f"{url}/{image}"

        books_data.append({
            'title': title,
            'price': price,
            'image': image_url
        })

    print(books_data)

except requests.exceptions.HTTPError as http_err:
    print(f"For Books : HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("For Books : Error connecting. Please check your network.")
except requests.exceptions.Timeout:
    print("For Books : Timeout error: The request took too long to complete.")
except requests.exceptions.RequestException as err:
    print(f"For Books : An unexpected error occurred: {err}")