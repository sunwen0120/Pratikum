import json
import csv

def writeCSV(data_list):
    f = csv.writer(open('test.csv', 'w', encoding='utf-8'))
    f.writerow(
        ['categorien', 'recipe_name', 'avg_score', 'difficulty', 'rating_count', 'pre_time', 'calorie', 'comment_user',
         'recipe_url'])
    for item in data_list:
        f.writerow([item['categorien'],
                    item['recipe_name'],
                    item['avg_score'],
                    item['difficulty'],
                    item['rating_count'],
                    item['pre_time'],
                    item['calorie'],
                    item['comment_user'],
                    item['recipe_url']]
                   )

