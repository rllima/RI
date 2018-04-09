import requests as rq
from bs4 import BeautifulSoup as bs
import json as js




r = rq.get("http://www.adorocinema.com/series/serie-21504/")
soup = bs(r.content)
tableData = soup.find("table", {"class": "data_box_table margin_10b"})
tableRows = tableData.find_all('tr')
creator = tableRows[0].find("span", {"itemprop": "name"}).text
country = tableRows[2].find("td").text
genders = tableRows[3].find("td").text
status = tableRows[4].find("td").text
duration = tableRows[5].find("td").text
country = soup.find("")
title = soup.find("span", {"class": "tt_r26 j_entities" }).text
description = soup.find("p", {"itemprop": "description"}).text
numberOfEpisodes = soup.find("strong", {"itemprop" : "numberOfEpisodes"}).text
cast = soup.find("div", {"class": "media_list_02 media_list_hl margin_10b "})
listCast = []
for item in cast.find_all("p"):
    k = str.split(item.text, "\n")
    listCast.append(("Ator: " + k[2],k[5]))

jsonCast = js.dumps(listCast)
print(jsonCast)
data = {}
data["Serie"] = []
data["Serie"].append({
    'Título' : title,
    'Autor' :  creator,
    'Pais' : country,
    'Status' : status,
    'Duração' : duration,
    'Episódios' : numberOfEpisodes,
    'Elenco': jsonCast,
    'Sinopse' : description
})   



    

    

    
    







