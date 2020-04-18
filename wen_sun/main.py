
import wen_sun.data_csv as data_csv
import wen_sun.crawl_data as crawl_data

import urllib
import random
import re
import sys
import time

global_recipe_list = []
URL = "https://www.chefkoch.de/rezepte/kategorien/"



# crawl all the recipe in the first categorien in several pages


if __name__ == "__main__":
    global_recipe_list = crawl_data.parse_html(URL)
    data_csv.writeCSV(global_recipe_list)
    print('finish')