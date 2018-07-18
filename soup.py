import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://modevs.herokuapp.com/'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1')

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name
