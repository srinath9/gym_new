import requests
import os
from bs4 import BeautifulSoup

fop = open("chennai.txt","r")
for url in fop.readlines():
	
# url = "http://www.ixigo.com/bay-of-life-surfing-and-sup-chennai-india-ne-1700892"

	response = requests.get(url)

	data = response.content
	soup = BeautifulSoup(response.content)
	print type(soup.find(id="aboutText"))
	

	# for link in soup.find_all("h1"):
	# 	string = "TITLE : " +link.get_text().strip() + "\n"
	# 	naming = link.get_text().strip().replace(" ","_")
	# 	newpath = r'/home/srinath/Music/net_tut/city/chennai/'+ naming
	# 	if not os.path.exists(newpath):
	# 		os.makedirs(newpath)
		
	# 	fopen = open(newpath+"/"+naming+".txt","ar")

		# string = "DESCRIPTION: " + about_text[0].get_text() +"\n"
		# fopen.write(string)

		# for addr in soup.find_all("span", { "class" :"famous-for" }):
		# 	string = "FAMOUS FOR: "+addr.get_text().strip() + "\n"
		# 	fopen.write(string)

		# x = 0
		# for addr in soup.find_all("div", { "class":"ne-summary-row-item"}):
		# 	if x == 0:
		# 		attach = "TYPE OF CATEGORY : "
		# 	else:
		# 		attach = "TIME OF DURATION : "
		# 	string =attach +addr.get_text().strip()+"\n"
		# 	fopen.write(string)
		# 	x =x+1
			
		# for addr in soup.find_all("h1"):
		# 	string = "TITLE : " +addr.get_text().strip() + "\n"
		# 	fopen.write(string)
			

		# for addr in soup.find_all("span", { "class":"entity-header-text"}):
		# 	string = "LOCATION : "+addr.get_text().strip()+ "\n"
		# 	fopen.write(string)

		# for addr in soup.find_all("div", { "class":"f-l-section"}):
		# 	li = addr.find_all("li")
		# 	fopen.write("OTHERS IN GOA: ")
		# 	for x in li:
		# 		fopen.write(x.get_text()+"\n")


		# for addr in soup.find_all("div", { "class":"tip"}):
		# 	string = "REVIEW : "+addr.get_text().strip()+ "\n"
		# 	fopen.write(string)

# for pictures

# for addr in soup.find_all("img"):
# 	print addr.get("src")
# 	img = addr.get("src")
# 	response1 = requests.get(url)
# 	if response1.status_code == 200:
# 		print "done"
		
# 	data1 = response1.text
	
# 	naming = addr.get("alt").replace(" ","_")
# 	print naming
# 	newpath = r'/home/srinath/Music/net_tut/city/goa/'+ naming
# 	if not os.path.exists(newpath): os.makedirs(newpath)
	
	# fopen = open(newpath+"/"+naming+".txt","ar")
	
	# print soup1
			
	
# fopen.close()