from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

URL = 'https://backpack.tf/stats/Strange/Gold%20Botkiller%20Minigun%20Mk.II/Tradable/Craftable/0'

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#A Request object is initialized using the URL and the header.
request = Request(URL, data=None, headers={'User-Agent': HEADER})

#BeautifulSoup object is intilized and the webpage is accessed here.
soup = BeautifulSoup(urlopen(request), 'html.parser')

#Soup finds the first tag with the entered title. This first tag usually contains attribues that contain prices.
#data-p_bptf_all is the name of the attribute that contains the price.
print(soup.find(title="Strange Gold Botkiller Minigun Mk.II")['data-p_bptf_all'])