from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

URL = 'https://backpack.tf/stats/Strange/Gold%20Botkiller%20Minigun%20Mk.II/Tradable/Craftable/0'
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

request = Request(URL, data=None, headers={'User-Agent': HEADER})

soup = BeautifulSoup(urlopen(request), 'html.parser')

#print(soup.title)