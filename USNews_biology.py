'''
@Author: Sohel Mahmud
@Date: 17-09-16
@Description: Scrapping the Biological Science grad schools from US News Grad School ranking

'''

import urllib
from urllib.request import Request, urlopen
import webbrowser
from bs4 import BeautifulSoup

url = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-science-schools/biological-sciences-rankings/page+"

urls =  [url + str(i) for i in range(1,12)]

for url in urls:
	#Openning the particular URL in a web browser
	#webbrowser.open(url)
	req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})

	html = urllib.urlopen(req).read()
	print html

	soup = BeautifulSoup(html,'lxml')
	tags = soup.find_all('a', class_='school-name')

	for tag in tags:
		school = tag.contents[0]
		school = school.encode('utf-8')
		print school
		with open('US-Grad-Schools-Biology.txt','a') as fhand:
			fhand.write(str(school) +'\n')
