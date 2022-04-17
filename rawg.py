from game import *

import json
import requests
import statistics

def main():
    base_url = "https://api.rawg.io/api/games"
    headers = {'page':2,'page_size':40,'dates':'2022-01-01,2022-04-15','ordering':'-metacritic','key':'5d53699543f048298c19ee28b26eedae'}
    for i in range(1,3):
        headers['page'] = i
        response = requests.get(base_url,headers)
        Datalist = response.json()['results']
        Gamelist=fetchdata(Datalist)
        savegame(Gamelist, 'rawg.txt')
    print(loadgame('rawg.txt'))

def fetchdata(Datalist):
    Gamelist = []
    for game in Datalist:
        Gameinfo = Game(json=game)
        gamedic = {'name':Gameinfo.name,'release_year':Gameinfo.release_year,'metacritic':Gameinfo.metacritic,'genres':Gameinfo.genres,'id':Gameinfo.id}
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