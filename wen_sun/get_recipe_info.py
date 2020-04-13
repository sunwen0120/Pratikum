import pandas as pd

def get_recipe_info(recipe):
    content = {
        "categorien": [],
        "recipe_name": [],  # *
        "avg_score": [],  # *
        "difficulty": [],  # *
        "rating_count": [],  # *
        "pre_time": [],  # *
        "calorie": [],
        "comment_user": [],
        "recipe_url": []  # *
    }

    soup = setup(recipe)
    # cat_name = soup.find('span',{'itemprop':'name'}).get_text()
    # # print(cat_name)
    # content['categorien'] = cat_name
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
    pre_time = re.findall('[A-Za-z0-9]', t)
    pre_time = ''.join(pre_time)
    content['pre_time'] = pre_time

    # difficulty of recipe
    diff = soup.find('span', {"class": "recipe-difficulty"}).get_text()
    difficulty = re.findall('[A-Za-z0-9]', diff)
    difficulty = ''.join(difficulty)
    content['difficulty'] = difficulty

    # get the url of all the recipes
    content['recipe_url'] = recipe

    print(content)

    recipe_detail_list.append(content)
    return (recipe_detail_list)