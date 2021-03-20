from urllib.request import urlopen
from bs4 import BeautifulSoup

site = urlopen('https://rudis.com/product-category/steals-deals/weekly-specials/')

bs = BeautifulSoup(site, "html.parser")
h2 = bs.find_all(['h2'])
print('List all the header2 tags (These are the Items on clearance on the deals page) :', *h2, sep='\n\n')
