import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import numpy as np
import pandas as pd

# read in the crawled file
from web_scrapy.extract_info import *


urls = []
CAT_NAME = "Regional"
FILE_NAME = '../Regional.txt'
FILE_DIR = '../Regional.csv'

f = open(FILE_NAME, "r")
for line in f.readlines():
    pattern = re.compile('https://www\.chefkoch\.de/rezepte/.*\.html')
    if re.match(pattern, line):
        urls.append(line)


# extract information from the websites in urls
index = 1
for url in urls:
    print("Extracting " + "index " + str(index) + 'th website:' + str(url))
    content = get_recipe_info(CAT_NAME, url)
    df = pd.DataFrame([content])
    df = df.replace("None", np.nan).fillna(value="NA")
    if index == 1:
        df.to_csv(FILE_DIR, index=False, sep=";", encoding="utf-8")
    else:
        df.to_csv(FILE_DIR,  mode='a', header=False, index=False, sep=";", encoding="utf-8")
    index = index + 1

print('finish')
