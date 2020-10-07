import requests

from bs4 import BeautifulSoup

r=requests.get("https://timesofindia.indiatimes.com/briefs") 

soup=BeautifulSoup(r.content,'html5lib')  #html5lib is used to parse HTML from the website

headings=soup.find_all('h2')   #h2 contains the headlines

headings=headings[2:-13]  #used to remove footer

for h in headings:    #printing the scraped news
    print(h.text)
