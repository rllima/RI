import requests as rq
from bs4 import BeautifulSoup as bs
import json as js


r = rq.get("http://www.tvguide.com/tvshows/the-flash/644014/")
soup = bs(r.content)
title = soup.find("div", {"class":"tvobject-masthead-wrapper content-wrapper"}).find("h1").text.strip()
print(title)
resume = soup.find("div", {"class":"tvobject-masthead-wrapper content-wrapper"}).find("div",{"class":"tvobject-masthead-description"}).text.strip()
print(resume)
cast = soup.find("div", {"data-section-id": "cast"})
print(cast)
