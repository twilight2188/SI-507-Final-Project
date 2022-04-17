from game import *

import json
import requests
import statistics

def main():
    file = open("igdb.txt", 'w').close()
    Base_url='https://api.igdb.com/v4/games/'
    headers = {'Client-ID':'wfn7jli2sugg8reuq3nnoar0elrm0l','Authorization': 'Bearer j06sq91d8w6srpzmnbbhft4asbfht7',"Accept": "application/json"}
    query = 'the witcher 3'
    data = f"search \"{query}\";fields *;"
    response = requests.post(url = Base_url,data='fields name, total_rating,summary; sort total_rating desc; limit 80; where total_rating>75 & total_rating_count>50 & release_dates.y>2020;',headers=headers)
    Datalist = response.json()
    Gamelist=fetchdata(Datalist)
    savegame(Gamelist, 'igdb.txt')
    print(loadgame('igdb.txt'))

def fetchdata(Datalist):
    Gamelist = []
    for game in Datalist:
        Gameinfo = Game(json=game)
        gamedic = {'name':Gameinfo.name,'rating':Gameinfo.rating,'summary':Gameinfo.summary,'id':Gameinfo.id}
        Gamelist.append(gamedic)
    return Gamelist

def savegame(Gamelist,filename):
    gameFile = open(filename, 'a',encoding="utf-8")
    for game in Gamelist:
        print(game,file = gameFile)
    gameFile.close()

def loadgame(filename):
    gameFile = open(filename, 'r',encoding="utf-8")
    lines = gameFile.readlines()
    lines = [line.strip() for line in lines]
    gameFile.close()
    return lines

if __name__ == '__main__':
    main()