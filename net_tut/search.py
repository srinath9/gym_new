
import requests
import os
from bs4 import BeautifulSoup
fopen = open("chennai.txt","w")

url = "http://www.ixigo.com/activities-in-around-chennai-lp-1140451"

response = requests.get(url)

data = response.content

soup = BeautifulSoup(data)
print "done"

for link in soup.find_all("div" , {"class":"ne-title"}):
	x = link.find_all("a")
	print x[0].get("href")
	fopen.write("http://www.ixigo.com"+x[0].get("href")+"\n")
