from jingjing_xu.web_scrapy.extract_info import *
import re
import numpy as np
import pandas as pd

# read in the crawled file


urls = []
FILE_NAME = 'chefkoch' + '/crawled.txt'
f = open(FILE_NAME, "r")
for line in f.readlines():
    pattern = re.compile('https://www\.chefkoch\.de/rezepte/.*\.html')
    if re.match(pattern, line):
        urls.append(line)


# extract information from the websites in urls
index = 1
for url in urls:
    print("Extracting " + "index " + str(index) + 'th website:' + str(url))
    content = get_recipe_info("Geränken", url)
    df = pd.DataFrame([content])
    df = df.replace("None", np.nan).fillna(value="NA")
    if index == 1:
        df.to_csv("/Users/sunwen/Documents/GitHub/Pratikum/web_scrapy/getrnke.csv", index=False, sep=";", encoding="utf-8")
    else:
        df.to_csv("/Users/sunwen/Documents/GitHub/Pratikum/web_scrapy/getrnke.csv",  mode='a', header=False, index=False, sep=";", encoding="utf-8")
    index = index + 1


