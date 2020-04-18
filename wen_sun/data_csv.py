
import csv

def writeCSV(data_list):
    file = open('./wen_sun/chefkoch_data.csv', 'w+', encoding='utf-8')
    f = csv.writer(file)
    f.writerow(
        ['recipe_id','categorien', 'recipe_name', 'avg_score', 'difficulty', 'rating_count', 'pre_time', 'calorie', 'ingredient',
         'comment_user','recipe_url'])
    for item in data_list:

        ingredient = ''
        for i in item["ingredient"]:
            ingredient = ingredient + i + ','

        f.writerow([item['recipe_url'].split('/')[4],
                    item['categorien'],
                    item['recipe_name'],
                    item['avg_score'],
                    item['difficulty'],
                    item['rating_count'],
                    item['pre_time'],
                    item['calorie'],
                    ingredient[:-1],
                    item['comment_user'],
                    item['recipe_url']]
                   )

    file.close()