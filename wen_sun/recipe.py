
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

# def pause():
#     time.sleep(random.uniform(15, 30))

def categorien_name(url):
    cat_name=[]
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
    cat_name = soup.find('h2', {'class', 'category-level-1'}).get_text()
    return(cat_name)
print(categorien_name(url))

def get_recipe_page(url):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
    link = soup.find('div',{'class', 'category-column'}).find('h2').find('a')['href']
    r = requests.get("https://www.chefkoch.de"+link, headers=headers)
    if r.status_code == 200:
        link_soup = BeautifulSoup(r.content, "html.parser")
    recipe_link = link_soup.find('a',{'class', 'ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item'}).get('href')
    r = requests.get(recipe_link, headers=headers)
    if r.status_code == 200:
        detail_soup = BeautifulSoup(r.content, "html.parser")
        # print(recipe_link)
    return(recipe_link)

# for n in soup.findall('h2', {'class', 'category-level-1'}):
#     recipe = get_recipe_page(url)
#     print(get_recipe_info(recipe))

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
    pre_time = re.findall('[A-Za-z0-9]+', t)
    # pre_time = ''.join(pre_time)

# # difficulty of recipe
    diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
    difficulty = re.findall('[A-Za-z0-9]', diff)
    difficulty = ''.join(difficulty)

# # crawl the calorie of the recipe
#     caro = soup.find('span', {"class": "recipe-kcalories"})
#     if len(caro) == 0:
#         calorie = "NA"
#     else:
#         caro = soup.find('span', {"class": "recipe-kcalories"}).get_text()
#         calorie = re.findall('[A-Za-z0-9]', caro)
#         calorie = ''.join(calorie)
    return(recipe_name,avg_score,rating_count,pre_time,difficulty)

for n in soup.findall('h2', {'class', 'category-level-1'}):
    recipe = get_recipe_page(url)
    print(get_recipe_info(recipe))