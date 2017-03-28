import requests
from bs4 import BeautifulSoup

url = "http://medcitynews.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content)

links = soup.find_all("a")

g_data = soup.find_all("p",{"class":"title"})
g_title = soup.find_all("h1",{"class":"title"})

for item in g_data:
    try:
        print(item.contents[1].text)
    except:
        pass

for item2 in g_title:
    try:
        print(item2.contents[1].text)
    except:
        pass










