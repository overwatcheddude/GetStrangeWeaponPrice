from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

URL = 'https://backpack.tf/stats/Strange/Panic%20Attack/Tradable/Craftable/0'

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#A Request object is initialized using the URL and the header.
request = Request(URL, data=None, headers={'User-Agent': HEADER})

#BeautifulSoup object is intilized and the webpage is accessed here.
soup = BeautifulSoup(urlopen(request), 'html.parser')

#Soup finds the first tag with the entered title. This first tag usually contains attribues that contain prices.
#data-p_bptf_all is the name of the attribute that contains the price.
#Unlike the other two, marketplace.tf div tag is not unique. So I had to use findAll 3 div value tags.
#I then chose the last value tag [2], took the value in-between the tags, and removed empty spaces.
print(soup.find(title="Strange Panic Attack")['data-p_bptf_all']) #Backpack.tf price
print(soup.find(title="Strange Panic Attack")['data-p_scm']) #Steam market price
print(soup.findAll("div", {"class": "value"})[2].string.strip()) #Marketplace.tf price