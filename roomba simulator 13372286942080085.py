
import fake_useragent
import requests
from bs4 import BeautifulSoup
url = "https://allo.ua/ua/roboty-pylesosy/"
user = fake_useragent.UserAgent().random
#print(user)

headers = {"user-agent": user}
response = requests.get(url, headers = headers)
#print(response.text)

soup = BeautifulSoup(response.text, "lxml")
all_product = soup.find("div", class_ ="products-layout__container products-layout--grid")
product_list = all_product.find_all("div", class_ ='product-card')
#print(product_list[0])

for i in range(len(product_list)):
    product_tittle = product_list[i].find("a", class_='product-card__title')
    #product_link = product_list[i].find("a", {'href': "https://allo.ua"})

    try:
        product_cost = product_list[i].find("div", class_="v-pb__old")
        product_cost_with_discount = product_list[i].find("div", class_="v-pb__cur discount")

        # print(product_tittle.text)
        #
        # print(product_cost.text)
        #
        # print(product_cost_with_discount.text)
        with open("roombas.txt", "a", encoding="utf-8") as file: #If you don`t have the file called roombas.txt yet, change the a to w
            file.write(f"  {product_tittle.text} {product_cost.text} {product_cost_with_discount.text} '\n' ")
    except AttributeError:
        print("There is no discount for that item currently")












