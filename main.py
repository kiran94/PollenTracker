#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib 
import re
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('/Library/Ruby/Gems/2.0.0/gems/terminal-notifier-1.7.1/bin/terminal-notifier {}'.format(' '.join([m, t, s])))

# Gets the pollen value for today 
def getPollenFlag():
	doc = urllib.urlopen('http://www.bbc.co.uk/weather/2643743').read()
	soup = BeautifulSoup(doc)

	items = soup.findAll('div', {'class' : 'environmental-index pollen-index'})
	regex = "<span class=\"value\">(.*?)</span>"
	res = re.search(regex, str(items[0]))

	return res.group(1)


title = "Pollen Counter"
print "Running " + title
pollen = getPollenFlag()

print pollen

if (pollen == "Very High"):
	notify(title, pollen, "The pollen count is very high today.")
elif(pollen == "High"):
	notify(title, pollen, "The pollen count is high today.")