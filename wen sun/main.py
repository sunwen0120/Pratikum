
import requests
from bs4 import BeautifulSoup
import urllib
import re

dict = {
    "categorien": [],
    "recipe_name": [],
    "avg_score": [],
    "difficulty": [],
    "rating_count": [],
    "ingredient": [],
    "user_url": [],
    "pre_time": []
}

url = 'https://www.chefkoch.de/rs/s0g26/Beilagen-Rezepte.html'
r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, "html.parser")
    # print(soup)

# crawl the recipe name
# for head in soup.find_all("h2", {"class": "ds-h3 ds-heading-link"}):
#     recipe_name = head.get_text()
#     print(recipe_name)

b = 'https://www.chefkoch.de/rezepte/1778601287739038/Rosmarinkartoffeln-aus-dem-Ofen.html'
r1 = requests.get(b)
if r1.status_code == 200:
    soup = BeautifulSoup(r1.content, "html.parser")

# the name of recipes
recipe_name = soup.find('h1')
print(recipe_name.get_text())

# crawel the ingredient of recipe
table = soup.find('table', {"class": "ingredients table-header"})
ingredient_table = []
for tr in table.findAll('tr'):
    td = tr.findAll('td')
    ingredient_table.append({
        "ingredient": td[1].get_text(),
        "amount": td[0].get_text()
    })
print(ingredient_table)

# crawl the average score of recipe
rating1 = soup.find('div', {"class": "ds-rating-avg"})
avg_score = rating1.find('strong').get_text()

print(avg_score)

# crawl the number of users, who make evaluation
rating2 = soup.find('div', {"class": "ds-rating-count"})
rating_count = rating2.find('strong').get_text()
print(rating_count)

# crawl the prepare time of recipe
t = soup.find('span', {"class": "recipe-preptime"}).get_text()
pre_time = re.findall('[A-Za-z0-9]', t)
pre_time = ''.join(pre_time)
print(pre_time)

# time = t.next_sibling
# prog = re.compile('[A-Za-z0-9]')
# time = prog.findall(t)
# print(t.next_sibling.strip())

# difficulty of recipe
diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
difficulty = re.findall('[A-Za-z0-9]', diff)
difficulty = ''.join(difficulty)
print(difficulty)

# crawl the calorie of the recipe
caro = soup.find('span', {"class": "recipe-kcalories"}).get_text()
calorie = re.findall('[A-Za-z0-9]', caro)
calorie = ''.join(calorie)
print(calorie)

