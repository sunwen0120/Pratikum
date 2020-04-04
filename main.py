import requests #导入requests包
from bs4 import BeautifulSoup 
url = 'https://www.chefkoch.de/user/profil/8cfc51bb8fe05e5ce1aac6e823b16dbf/Tibby.html'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)