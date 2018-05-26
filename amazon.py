import requests
from bs4 import BeautifulSoup

search = "a"

sort_dict = {
    'Relevance': 'relevance',
    'Popularity': 'popularity',
    'Price -- Low to High': 'price_asc',
    'Price -- High to Low': 'price_desc',
    'Newest First': 'recency_desc',
    'Discount': 'discount', }

while search != "exit":
    search = input("\nEnter the product you want to search \n Enter exit to exit\n")
    search.lower()
    if search != "exit":
        res = requests.get('https://www.flipkart.com/search?q=' + search + '&sort=popularity')
        soup = BeautifulSoup(res.text, 'html.parser')
        sort = soup.find_all("div", class_="_1xHtJz")

        if not sort:
            print("\n product search is incorrect \n")
            continue

        for i in sort[:]:
            print(str(sort.index(i) + 1) + " " + i.get_text())

        print("Enter option to find the price")
        sort_op = input()
        print("\n")
        sort_type = sort_dict[sort[(int(sort_op) - 1)].get_text()]

        # search + sort request
        sort_request = requests.get("https://www.flipkart.com/search?q=" + search + "&sort=" + sort_type)
        soup_sort = BeautifulSoup(sort_request.text, 'html.parser')

        # get product prices
        product = soup_sort.find_all("div", class_="_3wU53n")
        price = soup_sort.find_all("div", class_="_1vC4OE _2rQ-NK")

        if not product:
            product = soup_sort.find_all("a", class_="_2cLu-l")
            price = soup_sort.find_all("div", class_="_1vC4OE")

        for i in product[:]:
            print(i.get_text() + "\n Rs " + str(price[product.index(i)].get_text())[1:])
