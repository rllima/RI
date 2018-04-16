import requests as rq
from bs4 import BeautifulSoup as bs
import json as js




r = rq.get("http://www.imdb.com/title/tt0413573/?ref_=nv_sr_1")
soup = bs(r.content)
cast_table = soup.find("table", {"class" : "cast_list"}).find_all("span",{"class": "itemprop"})
for item in cast_table:
    actor = item.text
    print(actor)

character_list = soup.find("table", {"class": "cast_list"}).find_all("td",{"class": "character"})
for item in character_list:
    actor_name = item.find("div").a.text
    print(actor_name)
    
resume = soup.find("div", {"itemprop": "description"}).text
print(resume)
genres = soup.find("div", {"itemprop": "genre"}).find_all("a")
genre = []
for item in genres:
    genre.append(item.text);
print(genre)

details = soup.find("div", {"id": "titleDetails"})
title =  soup.find("div",{"class": "title_wrapper"})

numberOfSeasons = title.find("div",{"class": "originalTitle"})
print(numberOfSeasons)