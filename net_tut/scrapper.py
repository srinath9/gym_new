import requests
from bs4 import BeautifulSoup
import codecs

f = codecs.open("srinath.txt","a","utf-8")

url = "http://www.ixigo.com/bay-of-life-surfing-and-sup-chennai-india-ne-1700892"
response =requests.get(url)
soup = BeautifulSoup(response.content)

data =soup.find(id="aboutText")
f.write(data.get_text().replace("  ","").replace("\n",""))