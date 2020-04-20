from wen_sun.setup import setup


def function():
    dict = {'a': 1, 'b': 2, 'b': '3'}
    list = []
    list.append(dict)
    a = "abcd"
    return list, a

b = function()[0]
c = function()[1]
# print(b,c)


url = 'https://www.chefkoch.de/rezepte/1010591206190843/Lothars-beste-Nuernberger-Elisenlebkuchen.html'
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

                    if len(name)>1:
                        dict['name'] = name
                        rating = comm_soup.find('span', {"class": "rating-small"})
                        rating = rating.findChild()
                        rating = rating['class'][1]
                        dict['rating'] = rating

                        soup2 = setup('https://www.chefkoch.de/'+link)
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



print(get_comment_user(url))
