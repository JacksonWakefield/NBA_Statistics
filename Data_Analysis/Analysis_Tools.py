import pandas as pd
import numpy as np
import Data_Frame_Manager as dm
import json

#ALL = all player names
#PHO = all players on the Phoenix Suns
def getPlayerNames(team = "ALL"):
    playerNames = []
    
    if(team == "ALL"):
        
        path = "../PlayerReference.json"
        
        with open(path, encoding='utf8') as PlayerReference:    
            playerNames_json = json.load(PlayerReference)
            playerNames = playerNames_json.keys()
    
    return playerNames

def getPlayerAverage(player_name, category_name, digits_to_round = 2):
    playerFrame = dm.getPlayerDataFrame(player_name)
    
    category_data = []
    try:
        category_data = playerFrame[category_name]
    except:
        raise Exception('Could not find category: "' + category_name + '" for player: ' + player_name)
    
    try:
        return round(category_data.mean(), digits_to_round)
    except:
        raise Exception('Attempted to get average of non-numeric column')
    
