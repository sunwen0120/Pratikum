import requests
from bs4 import BeautifulSoup
import urllib

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

for head in soup.find_all("h2", {"class": "ds-h3 ds-heading-link"}):
    recipe_name = head.get_text()
    print(recipe_name)

b = 'https://www.chefkoch.de/rezepte/1728511281966781/Semmelknoedel-aus-der-Form.html'
r = requests.get(b)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, "html.parser")

for head in soup.find_all("div", {"class": "ds-rating-count"}):
    for
    rating_count = head.get_text()
    print(rating_count)




