import requests as rq
from bs4 import BeautifulSoup as bs
import json as js


r = rq.get("https://en.wikipedia.org/wiki/Grey%27s_Anatomy")
soup = bs(r.content)
title = soup.find("h1",{"id": "firstHeading"}).text
print(title)
table_infos = soup.find("table", {"class":"infobox vevent"}).find_all("tr")
print(table_infos)
genres = table_infos[2].find("div").text.strip()
print(genres)

