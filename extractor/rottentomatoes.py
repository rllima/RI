import requests as rq
from bs4 import BeautifulSoup as bs
import json as js


r = rq.get("https://www.rottentomatoes.com/tv/lost_in_space/")
soup = bs(r.content)
title = soup.find("h1", {"class":"title"}).text
print(title)
resume = soup.find("div", {"id": "movieSynopsis"}).text
genre = soup.find("td", text = "Genre:").parent.text
print(genre)
cast = soup.find_all("div",{"class":"cast-item media inlineBlock "})
cast_list = []
for item in cast:
    actor = item.find("div").find("a").text.strip()
    characther = str.replace(item.find("span",{"class": "characters subtle smaller"}).text,"as ","")
    cast_list.append([actor,characther])
print(cast_list)
rate = soup.find("div",{"class":"critic-score meter"}).span.text
print(rate)

