import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=New+Germany%2C+MN"
r = requests.get(url)
soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    print(link.get("href"))

g_data = soup.find_all("div",{"class":"info"})

for item in g_data:
    print(item.contents[0].find_all("a",{"class":"business-name"})[0].text)
    print(item.contents[1].find_all("p",{"class":"adr"})[0].text)
    try:
        print(item.contents[1].find_all("div",{"itemprop":"telephone"})[0].text)

    except:
        pass





