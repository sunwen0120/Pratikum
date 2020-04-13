import requests
from bs4 import BeautifulSoup
import re

# define a dictionary to store the information
content: dict = {
        "categorize": [],
        "recipe_name": [],
        "tags": [],
        "avg_score": [],
        "difficulty": [],
        "ingredient": [],
        "rating_count": [],
        "calorie": [],
        "preparation_time": [],
        "comment_user": [],
        "recipe_url": [],
    }


# extract useful information form the website
def get_recipe_info(dict, categorize, url):

    # categorize is hide in url
    categorize = categorize
    recipe_url = url

    r = requests.get(url)

    if r.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")

        # get recipe name
        recipe_name = soup.find('h1').get_text()

        # get the average score of recipes
        rating1 = soup.find('div', {"class": "ds-rating-avg"})
        avg_score = rating1.find('strong').get_text()

        # count the number of ratings
        rating2 = soup.find('div', {"class": "ds-rating-count"})
        rating_count = rating2.find('strong').get_text()

        # get the preparation time of recipe
        t = soup.find('span', {"class": "recipe-preptime"}).get_text()
        preparation_time = re.findall('[0-9]+[\s][A-Za-z]+', t)

        # get the difficulty of recipe
        diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
        difficulty = re.findall('[A-Za-z]+', diff)

        # get the ingredient of recipe
        ingre = soup.body.findAll(text='Zutaten')


        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)



        #for headline in soup.find_all("h2", {"class": "ds-h3 ds-heading-link"}):
            #print(headline.text)
        print(recipe_name)
        print(avg_score)
        print(preparation_time)
        print(ingre)
        print(difficulty)



get_recipe_info(content,"d","https://www.chefkoch.de/rezepte/485321142610150/Nougat-Taler.html")

