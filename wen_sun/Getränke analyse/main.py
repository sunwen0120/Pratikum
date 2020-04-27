#%%

import pandas as pd
import numpy as np
import re
from collections import Counter
import matplotlib.pyplot as plt

# print(pd.options.display.max_column)
df = pd.read_csv("Getranke.csv",sep=';', encoding ='utf-8')
# print(df.isnull().sum())

df = df.drop_duplicates(['recipe_name'])

y = df[df['recipe_url'] =='[]']
index = y.index.tolist()
df = df.drop(index =[13689])
df.shape


# i = 0
# for item in df['recipe_url']:
#     i = i+1
#     if item == '[]':
#         print(type(item))
#         print(i)
#         print(item)


df


#%%

# data pre-processing
import ast

# Drop the duplicates
# df = df.drop_duplicates(['recipe_name'])
# print("Number of data (recipes) : " + str(df.shape))

# Look for null value in the data
# print(df.isnull().sum())


# If NaN for calorie and comment user -> change it to none!
values_cal = {'calorie': 'none'}
df = df.fillna(value=values_cal)
values_com = {'comment_user': 'no comment'}
df = df.fillna(value=values_com)

df

# type(df['recipe_url'][0].split('/')[4])

# cat_index = []
# for item in df.raws:
#     print(item['recipe_url'])
#     cat_index.append(item['recipe_url'].split('/')[4])
# cat_index

list_cat_no = []
# cat_index.split('/')[4]
i = 0
for item in df['recipe_url']:
    list_cat_no.append(item.split('/')[4])

# add one column "recipe_id" into the dataset and set it as the index of dataset
df['recipe_id'] = list_cat_no
df = df.set_index(["recipe_id"])
df

#%%

data_com = df['comment_user']

# data_com[0:10]
# data_com.index

data_com = data_com[0:10]

df_com = pd.DataFrame()


for index, item in data_com.iteritems():

    # print(index)
    # print(item)
    if (item != 'no comment'):
        array = ast.literal_eval(item)
#         df_com['recipe_id'] = data_com.index
        df_array = pd.DataFrame(array)
        df_array['recipe_id'] = index
        df_com = pd.concat([df_com,df_array])

df_com.set_index(["recipe_id"])
print(df_com)




#%%

# list_a =[]
# list_a.append(df.iloc[:,[3]])

# del list_a[:0]

# df['avg_score'].value_counts()





#%%



#%%


