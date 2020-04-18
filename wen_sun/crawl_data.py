import re
from wen_sun.setup import setup


def parse_html(url):
    recipe_info_list = []
    soup = setup(url)
    # 页面跳转
    link = soup.find('div', {'class', 'category-column'}).find('h2').find('a')['href']
    subpage = "https://www.chefkoch.de" + link
    soup_cat = setup(subpage)


    # page turning automatically
    for i in range(1, 2):
        page = soup_cat.find('ul', {'class', 'ds-pagination'})
        for li in page.find_all('li'):
            link_a = li.find('a', {'class', 'ds-page-link bi-paging-jump'})
            if link_a != None:
                link = link_a['href']
                soup_recipe = setup(link)
                for article in soup_recipe.find_all('article', {'class', 'rsel-item ds-grid-float ds-col-12 ds-col-m-8'}):
                    new_url = article.find('a')['href']
                    recipe_info_list.extend(get_recipe_info(new_url))

                    # break
    return(recipe_info_list)


# def categorien_name(url):
#     soup = setup(url)
#     cat_name = soup.find('h2', {'class', 'category-level-1'}).get_text()
#     return (cat_name)

# crawel the ingredient of recipe
def get_recipe_ingredient(recipe):
    soup = setup(recipe)
    tableAll = soup.findAll('table', {"class": "ingredients table-header"})
    ingredient_table = []
    for table in tableAll:
        for tr in table.findAll('tr'):
            td = tr.findAll('td')
            if td != []:
                ingredient_table.append(
                td[1].get_text().lstrip().rstrip())
    return(ingredient_table)

# 取每项菜谱材料数量
def get_recipe_ingredient_1(recipe):
    soup = setup(recipe)
    table = soup.find('table', {"class": "ingredients table-header"})
    ingredient_table = []
    for tr in table.findAll('tr'):
        td = tr.findAll('td')
        ingredient_table.append({
            "matriel" : td[1].get_text().lstrip().rstrip(),
            "amount" : td[0].get_text().lstrip().rstrip()
        })
    return(ingredient_table)

# recipe = 'https://www.chefkoch.de/rezepte/1010591206190843/Lothars-beste-Nuernberger-Elisenlebkuchen.html'
def get_comment_user(recipe):
    soup = setup(recipe)
    comment_link = soup.find('span',{'class': 'ds-from-m rat-show-action'}).find('a')['href']
    comm_soup = setup(comment_link)
    comment_table = comm_soup.find('table',{'class':'votes-rating-cell'})
    for tr in comment_table.find_all('tr'):
        td = tr.find_all('td')
        comment_user = td.find('a')['href']
# print(get_comment_user(recipe))


def get_recipe_info(recipe):
    print(recipe)
    recipe_detail_list = []
    content = {
        "categorien": [],
        "recipe_name": [],  # *
        "avg_score": [],  # *
        "difficulty": [],  # *
        "rating_count": [],  # *
        "pre_time": [],  # *
        "calorie": [],
        "ingredient":[],
        "comment_user": [],
        "recipe_url": []  # *
    }

    soup = setup(recipe)
    # crawl the categorien name
    cat_name_list = []
    for li in soup.find_all('li',{"itemprop": "itemListElement"}):
        cat_name = li.find('span',{'itemprop': "name"}).get_text()
        cat_name_list.append(cat_name)
    content['categorien'] = cat_name_list[3]

    # crawl the name of recipes
    recipe_name = soup.find('h1').get_text()
    content['recipe_name'] = recipe_name

    # crawl the average score of recipes
    rating1 = soup.find('div', {"class": "ds-rating-avg"})
    avg_score = rating1.find('strong').get_text()
    content['avg_score'] = avg_score

    # crawl the number of users, who make evaluation
    rating2 = soup.find('div', {"class": "ds-rating-count"})
    rating_count = rating2.find('strong').get_text()
    content['rating_count'] = rating_count

    # crawl the prepare time of recipe
    t = soup.find('span', {"class": "recipe-preptime"}).get_text()
    pre_time = re.findall('[A-Za-z0-9]+', t)
    # pre_time = ''.join(pre_time)
    content['pre_time'] = pre_time

    # difficulty of recipe
    diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
    difficulty = re.findall('[A-Za-z0-9]+', diff)
    # difficulty = ''.join(difficulty)
    content['difficulty'] = difficulty

    # crawl the calorie of the recipe
    try:
        caro = soup.find('span', {"class": "recipe-kcalories"}).get_text()
        calorie = re.findall('[A-Za-z0-9]+', caro)
        # calorie = ''.join(calorie)
        content['calorie'] = calorie
    except:
        content['calorie'] = 'None'

    # crawl the ingredients of recipes
    ingredient = get_recipe_ingredient(recipe)
    for i in ingredient:
        # print(i)
        content['ingredient'].append(i)
    # print(ingredient)


    # get the url of all the recipes
    content['recipe_url'] = recipe

    print(content)

    recipe_detail_list.append(content)

    return (recipe_detail_list)