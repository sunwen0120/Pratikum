
import requests
from bs4 import BeautifulSoup
import urllib

url = "https://www.chefkoch.de/rezepte/kategorien/"
headers = {'user-agent':'Mozilla/5.0'}

def categorien_name(url):
    cat_name=[]
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

    for categorien in soup.find_all('h2', {'class', 'category-level-1'}):
        # cat_name = categorien.get_text()
        cat_name.append({
            "categorien name":categorien.get_text().lstrip().rstrip()
        })
    return(cat_name)

print(categorien_name(url))

# link = soup.find('div',{'class', 'category-column'}).find('h2').find('a')['href']
# # print(link)
#
# r = requests.get("https://www.chefkoch.de"+link, headers=headers)
# if r.status_code == 200:
#     link_soup = BeautifulSoup(r.content, "html.parser")
#     # print(link_soup)
# koch_link = link_soup.find('a',{'class', 'ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item'}).get('href')
#
# r = requests.get(koch_link, headers=headers)
# if r.status_code == 200:
#     detail_soup = BeautifulSoup(r.content, "html.parser")
#     print(detail_soup)
#
# def get_recipe_info():
