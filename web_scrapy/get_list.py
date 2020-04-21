import requests
from bs4 import BeautifulSoup
import re
import time
from general import *
import numpy as np


# find all list url
def find_link_urls(urls, base_url):

    time.sleep(0.5)
    r = requests.get(base_url)

    if r.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")

        for a in soup.findAll('a', {"class": "ds-page-link bi-paging-jump"}):
            urls.append(a['href'])

    urls = list(set(urls))

    return urls


# find all recipe href in the list rul
def append_list(base_url):
    url_list = []

    # request the website of rating list
    time.sleep(0.5)
    r = requests.get(base_url)

    if r.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")

        for a in soup.findAll('a', {"class": "ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item"}):
            url_list.append(a['href'])

    return url_list


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name):
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    return crawled


def get_last_url(urls_list):
    temp = []
    for url in urls_list:
        index = re.findall("[s][0-9]*[g]", url)
        index = re.findall("[0-9]+", str(index))
        temp.append(int(index[0]))
    return np.argmax(np.array(temp))


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


##################################### main() ###################################################
base_url = "https://www.chefkoch.de/rs/s0g47/Suessspeisen-Backen-Rezepte.html"
create_project_dir("Suessspeisen-Backen")
crawled_path = create_data_files("Suessspeisen-Backen")
index = 1

url = find_link_urls([], base_url)
len_url = len(url)
last_url_index = get_last_url(url)
new_urls = find_link_urls(url, url[last_url_index])
len_new_urls = len(new_urls)


while len_url < len_new_urls:
    len_url = len_new_urls
    url = new_urls
    last_url_index = get_last_url(url)
    new_urls = find_link_urls(url, url[last_url_index])
    len_new_urls = len(new_urls)
    print(len_new_urls)


for url in new_urls:
    recipe_list = append_list(url)
    for data in recipe_list:
        append_to_file(crawled_path, data)
        print("Crawled:" + str(index))
        index += 1







    









