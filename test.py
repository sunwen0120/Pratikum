import requests
from bs4 import BeautifulSoup
import urllib
import random
import re
import sys
import time

url = "https://www.chefkoch.de/rezepte/kategorien/"
headers = {'user-agent':'Mozilla/5.0'}

html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')

# 页面跳转
link = soup.find('div',{'class', 'category-column'}).find('h2').find('a')['href']
r = requests.get("https://www.chefkoch.de"+link, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
for i in range(1,3):
    for li in soup.find_all('a',{'class': 'ds-page-item'}):
        url_n = li.find('a')['href']
        print(url_n)
        html = requests.get(url_n, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        for article in soup.find_all('article',{'class', 'rsel-item ds-grid-float ds-col-12 ds-col-m-8'}):
            new = article.find('a')['href']
            # print(new)



# def categorien_name(url):
#     cat_name=[]
#     r = requests.get(url, headers=headers)
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, "html.parser")
#     cat_name = soup.find('h2', {'class', 'category-level-1'}).get_text()
#
#     # for categorien in soup.find_all('h2', {'class', 'category-level-1'}):
#     #     # cat_name = categorien.get_text()
#     #     cat_name.append({
#     #         "categorien name":categorien.get_text().lstrip().rstrip()
#     #     })
#     return(cat_name)
# print(categorien_name(url))

def categorien_name(url):
    cat_name=[]
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
    cat_name = soup.find('h2', {'class', 'category-level-1'}).get_text()
    return(cat_name)

def get_recipe_page(url):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
    for h2 in soup.find_all('h2'):
        link = h2.find('a')['href']
        r = requests.get("https://www.chefkoch.de"+link, headers=headers)
        if r.status_code == 200:
            link_soup = BeautifulSoup(r.content, "html.parser")
        recipe_link = link_soup.find('a',{'class', 'ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item'}).get('href')
        # print(recipe_link)
    return(recipe_link)



def get_recipe_info(recipe):
    html = requests.get(recipe, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
# the name of recipes
    recipe_name = soup.find('h1').get_text()
    # return(recipe_name)

    rating1 = soup.find('div', {"class": "ds-rating-avg"})
    avg_score = rating1.find('strong').get_text()

# crawl the number of users, who make evaluation
    rating2 = soup.find('div', {"class": "ds-rating-count"})
    rating_count = rating2.find('strong').get_text()

# # crawl the prepare time of recipe
    t = soup.find('span', {"class": "recipe-preptime"}).get_text()
    pre_time = re.findall('[A-Za-z0-9]', t)
    pre_time = ''.join(pre_time)

# # difficulty of recipe
    diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
    difficulty = re.findall('[A-Za-z0-9]', diff)
    difficulty = ''.join(difficulty)
    return (recipe_name, avg_score, rating_count, pre_time, difficulty)

# for h2 in soup.find_all('h2'):
#     recipe = get_recipe_page(url)
#     # print(recipe)
#     r = requests.get(recipe, headers=headers)
#     if r.status_code == 200:
#         detail_soup = BeautifulSoup(r.content, "html.parser")
#     # print(get_recipe_info(recipe))




