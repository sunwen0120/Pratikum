import requests
from bs4 import BeautifulSoup
import re
import time

def get_comment_user_1(url):

    comment_user = []

    # request the website of rating list
    time.sleep(0.5)
    r = requests.get(url)

    if r.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")

        # get the voting table
        table = soup.find('table', {"class": "voting-table"})
        rows = table.findAll('tr')
        for row in rows[1:]:
            # use a dictionary to store the information of every user
            dict = { }

            # get the name of the user
            name = row.findAll('a')
            if len(name) > 1:

                # get the rating of the user
                rating = row.find('span', {"class": "rating-small"})
                rating = rating.findChild()

                rating = rating['class'][1]
                dict['rating'] = rating

                cm_time = row.find('td', {"class": "votes-date-cell"}).get_text()
                cm_time = re.findall('[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}', cm_time)
                # cm_time = re.findall('[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s[0-9]{2}:[0-9]{2}', cm_time)
                dict['comment_time'] = cm_time[0]
                dict['name'] = name[0].get_text()

                profile_url = 'https://www.chefkoch.de' + name[0]['href']

                # get the age, sex of the user
                time.sleep(0.5)
                w = requests.get(profile_url)

                if w.status_code == 200:
                    soup2: BeautifulSoup = BeautifulSoup(w.content, "html.parser")
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

    return comment_user

url = 'https://www.chefkoch.de/rezepte/wertungen/1122481218552589/Schichtdessert-mit-Weintrauben.html'

try:
    print(get_comment_user_1(url))
except:
    print('none')
