import os
import sys
import threading
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import numpy as np
import pandas as pd

# read in the crawled file
from web_scrapy.extract_info import *

class myThread(threading.Thread):
    def __init__(self, threadID, cat_name, file_name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.cat_name = cat_name
        self.file_name = file_name
    def run(self):
        print("Thread begin：" + self.cat_name)
        main(self.cat_name, self.file_name)
        print("Thread exit：" + self.cat_name)

def main(cat_name,file):
    urls = []
    file_name = '../' + file + '.txt'
    file_dir = '../' + file + '.csv'

    f = open(file_name, "r")
    for line in f.readlines():
        pattern = re.compile('https://www\.chefkoch\.de/rezepte/.*\.html')
        if re.match(pattern, line):
            urls.append(line)

    # extract information from the websites in urls
    index = 1
    for url in urls:
        print("Extracting " + "index " + str(index) + 'th website:' + str(url))
        content = get_recipe_info(cat_name, url)
        df = pd.DataFrame([content])
        df = df.replace("None", np.nan).fillna(value="NA")
        print(file)
        if index == 1:
            df.to_csv(file_dir, index=False, sep=";", encoding="utf-8")
            time.sleep(5)
        else:
            df.to_csv(file_dir,  mode='a', header=False, index=False, sep=";", encoding="utf-8")
            time.sleep(5)
        index = index + 1

    print('finish')

if __name__ == "__main__":
    # create thread
    thread1 = myThread(1, "Menüart", "Beilage")
    thread2 = myThread(2, "Menüart", "Dessert")
    thread3 = myThread(3, "Menüart", "Fruehstueck")
    thread4 = myThread(4, "Menüart", "Salat")
    thread5 = myThread(5, "Menüart", "Suppen")
    thread6 = myThread(6, "Menüart", "Vorspeisen")
    thread7 = myThread(7, "Regional", "Regional")

    # begin new thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    print('finish all')