import requests
from bs4 import BeautifulSoup

#################################################### Quotes ####################################################
# Step 1: Make a request to the page
url = "https://quotes.toscrape.com"
response = requests.get(url)
response.raise_for_status()  # Raises an error if request failed

# Step 2: Parse the HTML with BeautifulSoup
quoteList = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract the data you want (example: all quotes)
quotes = quoteList.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)

#################################################### Books ####################################################
# Step 1: Make a request to the page
url = "https://books.toscrape.com"
response = requests.get(url)
response.raise_for_status()  # Raises an error if request failed

# Step 2: Parse the HTML with BeautifulSoup
bookList = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract the data you want (example: all quotes)
books = bookList.find_all('article', class_='product_pod')

# Set empty array to hold book data
books_data = []

# Loop through each book and extract title, price, and image URL
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
