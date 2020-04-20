import re
from wen_sun.setup import setup, pause

def parse_html(url):
    recipe_info_list = []
    pause()
    soup = setup(url)
    # 页面跳转
    column_list = []
    for column in soup.findAll('h2', {'class', 'category-level-1'}):
        link = column.find('a')['href']
        column_list.append(link)
    link = column_list[4]   # need more change to finish the 4,5 categorien
    subpage = "https://www.chefkoch.de" + link
    soup_cat = setup(subpage)
    # print(link)

    # page turning automatically
    for i in range(1, 2):
        page = soup_cat.find('ul', {'class', 'ds-pagination'})
        for li in page.find_all('li'):
            link_a = li.find('a', {'class', 'ds-page-link bi-paging-jump'})
            if link_a != None:
                link = link_a['href']
                pause()
                soup_recipe = setup(link)
                for article in soup_recipe.find_all('article', {'class', 'rsel-item ds-grid-float ds-col-12 ds-col-m-8'}):
                    new_url = article.find('a')['href']
                    recipe_info_list.extend(get_recipe_info(new_url))
                break

    return(recipe_info_list)




# crawel the ingredient of recipe
def get_recipe_ingredient(recipe):
    pause()
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


# extract user link
def get_comment_user(recipe):
    dict = {}
    comment_user = []

    # request the website of rating list

    soup = setup(recipe)
    comment_link = soup.find('span', {'class': 'ds-from-m rat-show-action'}).find('a')['href']
    comm_soup = setup(comment_link)
    comment_table = comm_soup.find('table', {'class': 'voting-table'})
    for tr in comment_table.find_all('tr'):
        for td in tr.find_all('td'):
            if td != []:
                a_tag = td.find('a')
                if a_tag != None:
                    profile_url = a_tag.get('href')
                    name = a_tag.get_text()
                    if profile_url != 'http://www.chefkoch.de/benutzer/hitliste':
                        link = profile_url

                        # dict['profile_url'] = link

                    if len(name) > 1:
                        dict['name'] = name
                        rating = comm_soup.find('span', {"class": "rating-small"})
                        rating = rating.findChild()
                        rating = rating['class'][1]
                        dict['rating'] = rating

                        # pause()
                        soup2 = setup('https://www.chefkoch.de/' + link)
                        table = soup2.find('table', {"id": "user-details"})
                        # get the sex of user
                        img = table.findAll('img')
                        if img:
                            dict['sex'] = img[0]['alt']
                        else:
                            dict['sex'] = 'None'

                        # get the age of user
                        age = table.find('td', {"class": 'nobr'}).find_next('td').text.strip()
                        if age:
                            dict['age'] = age
                        else:
                            dict['age'] = 'None'
                        # get the marriage status of user
                        marriage_status = table.find('strong', text='Beziehungsstatus:')
                        if marriage_status:
                            marriage_status = marriage_status.find_next('td').text.strip()
                            dict['marriage_status'] = marriage_status
                        else:
                            dict['marriage_status'] = 'None'

                        # get the job of user
                        job = table.find('strong', text='Beruf:')
                        if job:
                            job = job.find_next('td').text.strip()
                            if job != 'n/a':
                                dict['job'] = job
                            else:
                                dict['job'] = 'None'

                            # if the dict contains 4 'None' then we do not append it
                        keys = list(dict.values())
                        if keys.count('None') < 4:
                            comment_user.append(dict)
                            # print(comment_user)
    return comment_user

url = 'https://www.chefkoch.de/rezepte/2690541421778074/Aloha-Quarkmaeusle.html'

def get_recipe_info(recipe):
    # print(recipe)
    recipe_detail_list = []
    content = {
        "categorien": [],
        "recipe_name": [], # *
        "tags":[],
        "avg_score": [],  # *
        "difficulty": [],  # *
        "rating_count": [],  # *
        "pre_time": [],  # *
        "calorie": [],
        "ingredient":[],
        "comment_user": [],
        "recipe_url": []  # *
    }

    pause()
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

    # get the tags of recipes
    tags = []
    properties = soup.findAll('a', {"class": "ds-tag bi-tags"})
    for property in properties:
        tag = property.get_text()
        tag = tag.strip().replace('\n', '')
        tag = tag.replace(" ", "")
        tags.append(tag)
    content['tags'] = tags

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
    pre_time = re.findall('[A-Za-z0-9]', t)
    pre_time = ''.join(pre_time)
    content['pre_time'] = pre_time

    # difficulty of recipe
    diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
    difficulty = re.findall('[A-Za-z0-9]', diff)
    difficulty = ''.join(difficulty)
    content['difficulty'] = difficulty

    # crawl the calorie of the recipe
    try:
        caro = soup.find('span', {"class": "recipe-kcalories"}).get_text()
        calorie = re.findall('[A-Za-z0-9]', caro)
        calorie = ''.join(calorie)
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

    # get the detail information of comment users and their profile url

    comment_user = get_comment_user(recipe)
    for i in comment_user:
        print(i)
        content['comment_user'].append(i)




    # print(content)

    recipe_detail_list.append(content)

    return (recipe_detail_list)

get_recipe_info(url)
