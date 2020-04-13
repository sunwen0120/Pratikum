import requests
from bs4 import BeautifulSoup
import wen_sun.data_csv as data_csv
import wen_sun.crawl_data as get_recipe_info
import urllib
import random
import re
import sys
import time

recipe_detail_list = []
URL = "https://www.chefkoch.de/rezepte/kategorien/"



# def categorien_name(url):
#     cat_name = []
#     r = requests.get(url, headers=headers)
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.content, "html.parser")
#     cat_name = soup.find('h2', {'class', 'category-level-1'}).get_text()
#     return (cat_name)



# crawl all the recipe in the first categorien in several pages


if __name__ == "__main__":
    parse_html(URL)
    data_csv.writeCSV(recipe_detail_list)