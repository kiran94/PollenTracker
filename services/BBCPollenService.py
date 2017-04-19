import re
import urllib 
from bs4 import BeautifulSoup

# Pollen Service to retrieve pollen information from the BBC URL. 
class BBCPollenService:
    
    # Gets the pollen value for today. 
    def getPollenFlag(self):
        doc = urllib.urlopen('http://www.bbc.co.uk/weather/2643743').read()
        soup = BeautifulSoup(doc)

        items = soup.findAll('div', {'class' : 'environmental-index pollen-index'})
        regex = "<span class=\"value\">(.*?)</span>"
        res = re.search(regex, str(items[0]))

        return res.group(1)