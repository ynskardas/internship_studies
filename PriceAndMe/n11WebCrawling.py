import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


class Product:

    def __init__(self, title1, link1, price1, category1, mainC1):
        self.title = title1
        self.link = link1
        self.price = price1
        self.category = category1
        self.mainC = mainC1



def pars(tupple1, box):

    cate = tupple1[0]
    url1 = tupple1[1]
    pairs = []
    i = 0
    data2 = requests.get(url1)

    soup1 = BeautifulSoup(data2.text, 'html.parser')

    productArea = soup1.find('div', {'class': 'productArea'})
    bread = productArea.find('div', {'class': 'breadcrumb'})
    
    i = 0
    mostCate = ''
    for li in bread.find_all('li'):
        a = li.find('a')
        title = a.get('href')

        if i == 1:
            mostCate = title


    section = soup1.find('section', {'class': 'listingGroup'})

    div = section.find('div', {'id': 'view'})

    for li in div.find_all('li', {'class': 'column'}):

        div1 = li.find('div', {'class': 'proDetail'})

        a = div1.find('a', {'class': 'newPrice'})

        link = a.get('href')
        title = a.get('title')
        price = a.text.replace(" ", "").replace("\n", "").replace("T", " T")
        product1 = [title, link, price]

        product = Product(title, link, price, cate, mostCate)

        print(product.title)

        box.append(product)

        i = i + 1

        if i >= 1:
            break
    return box

# def pars1(url1):
#     pairs = []
#     i = 0
#     data2 = requests.get(url1)

#     soup1 = BeautifulSoup(data2.text, 'html.parser')
#     div = soup1.find('div', {'id': 'contentWrapper'})

#     for product2 in div.find_all('div', {'class': 'item0'}):
#         pro3 = product2.find('div', {'class': 'productContainer'})
#         a1 = pro3.find('a')
#         link = a1.get("href")
#         title = a1.find('h3').text.strip()
#         pairs.append((title, link))


#         i = i + 1

#         if i >= 10:
#             break

#     return pairs



#-----------------------------------------------------------------------------------------------------


html1 = 'https://www.n11.com/site-haritasi'

data1 = requests.get(html1)

soup = BeautifulSoup(data1.text, 'html.parser')

content = soup.find('div', {'class': 'content'})

divv = content.find('div', {'class': 'container'})

main = divv.find('main', {'class': 'sitemap'})

data = []

ignoreList = []

for div in divv.find_all('div', {'class': 'category-wrapper'}):

    a1 = div.find('a', {'class': 'main-category'})

    if "Bilet" in a1.text and "Tatil" in a1.text:

        break

    else:    
        
        k = True
        
        for div1 in div.find_all('div', {'class': 'sub-category'}):
            
            a = div1.find('a')
            link = a.get('href')
            title = a.text

            for div2 in div1.find_all('div', {'class': 'sub-category'}):

                aIgnore = div2.find('a')
                titleIgn = a.text
                ignoreList.append(titleIgn)

            
            if title in titleIgn:
                tkl = 1

            else:
                data.append((title, link))
                
            

sort = "?srt=SALES_VOLUME&minp=250"

box = []


for i in range(len(data)):
    
    box = pars(data[i], box)

    
    

mainCategory = []
productCategory = []
productPrice = []
productName = []
productLink = []

for i in range(len(box)):

    mainCategory.append(box[i].mainC)
    productCategory.append(box[i].category)
    productName.append(box[i].title)
    productPrice.append(box[i].price)
    productLink.append(box[i].link)
        



Productss = {'Main Category': mainCategory, 
            'Product Category': productCategory, 
            'Product Price': productPrice,
            'Product Name': productName,
            'Product Link': productLink}

df = DataFrame(Products, columns = ['Main Category', 'Product Category', 'Product Name', 'Product Price', 'Product Link'])

export_excel = df.to_excel (r'/home/yunus/University/Internship Projects/PriceAndMe/n11_data_try.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path










