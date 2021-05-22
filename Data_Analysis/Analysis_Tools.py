import pandas as pd
import numpy as np
import json
import csv

#returns data frame for particular player
def getPlayerDataFrame(player_name):
    name = player_name + ".csv"
    path = "../player_data//" + name
    file = open(path, 'r', encoding='utf-8')
    try:
        return pd.read_csv(file)
    except:
        raise Exception('Could not find player data for: ' + player_name + "\n Path: " + path)

#returns the data frame for the allPlayerAverage
def getAllPlayerAverageDataFrame():
    path = "../allPlayerAverage.csv"
    file = open(path, 'r', encoding='utf-8')
    try:
        return pd.read_csv(file)
    except:
        raise Exception('Could not find: ' + path + ", consider running buildAllPlayerAverage in Analysis_Tools.py")

def getAllPlayerTotalDataFrame():
    path = "../allPlayerTotal.csv"
    file = open(path, 'r', encoding='utf-8')
    try:
        return pd.read_csv(file)
    except:
        raise Exception('Could not find: ' + path + ", consider running buildAllPlayerAverage in Analysis_Tools.py")

#ALL = all player names
#PHO = all players on the Phoenix Suns
#Returns array of all player names in the Player_Data json
def getPlayerNames(team = "ALL"): #TO-DO
    playerNames = []
    
    if(team == "ALL"):
        
        path = "../PlayerReference.json"
        
        with open(path, encoding='utf8') as PlayerReference:    
            playerNames_json = json.load(PlayerReference)
            playerNames = playerNames_json.keys()
    
    return playerNames

#returns the average from all games in a specific category
def getPlayerAverage(player_name, category_name, digits_to_round = 2):
    playerFrame = getPlayerDataFrame(player_name)
    
    category_data = []
    try:
        category_data = playerFrame[category_name]
    except:
        raise Exception('Could not find category: "' + category_name + '" for player: ' + player_name)
    
    try:
        return round(category_data.mean(), digits_to_round)
    except:
        raise Exception('Attempted to get average of non-numeric column')

#returns total from all games in a specific category
def getPlayerTotal(player_name, category_name, digits_to_round = 2):
    playerFrame = getPlayerDataFrame(player_name)
    
    category_data = []
    try:
        category_data = playerFrame[category_name]
    except:
        raise Exception('Could not find category: "' + category_name + '" for player: ' + player_name)
    
    try:
        return round(category_data.sum(), digits_to_round)
    except:
        raise Exception('Attempted to get total of non-numeric column')

#returns the maximum value from all games in a specific category
def getPlayerMax(player_name, category_name, digits_to_round = 2):
    playerFrame = getPlayerDataFrame(player_name)
    
    category_data = []
    try:
        category_data = playerFrame[category_name]
    except:
        raise Exception('Could not find category: "' + category_name + '" for player: ' + player_name)
    
    try:
        return round(category_data.max(), digits_to_round)
    except:
        raise Exception('Attempted to get max of non-numeric column')

#returns minimum value from all games in a specific category
def getPlayerMin(player_name, category_name, digits_to_round = 2):
    playerFrame = getPlayerDataFrame(player_name)
    
    category_data = []
    try:
        category_data = playerFrame[category_name]
    except:
        raise Exception('Could not find category: "' + category_name + '" for player: ' + player_name)
    
    try:
        return round(category_data.min(), digits_to_round)
    except:
        raise Exception('Attempted to get min of non-numeric column')



    

            
            
            

        
    
    
