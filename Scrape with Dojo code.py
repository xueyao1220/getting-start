import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.idealo.de/preisvergleich/OffersOfProduct/4964793_-kato-1-ghost-bikes.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

