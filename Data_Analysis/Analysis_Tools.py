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

#replaces specific text in all csvs in player_data folder --> subject = target
def replaceAllInPlayerData(subject, target):
    names = getPlayerNames()
    
    
    for name in names:
        path = "../player_data/" + name + ".csv"
        
        new_file_content = ""
        
        #read and create string with new file
        fin = open(path, "r+", encoding='utf8')
        
        for line in fin:
            stripped_line = line.strip()
            new_line = stripped_line.replace(subject, target).replace(" ", "")
            new_file_content += new_line + "\n"
        
        fin.close()
        
        #delete contents and write back
        fout = open(path, "w", encoding='utf8')
        
        fout.truncate(0)
        fout.write(new_file_content)
        fout.close()

#build the allPlayerAverage CSV
def buildAllPlayerAverage(digits_to_round = 2):
    path = "../allPlayerAverage.csv"
    
    #taken from StatsGenerator (does not include non-numeric columns)
    columns = ["Name", "Margin", "Minutes", "FGA", "FGM", "3PA", "3PM", "Rebounds", "Assists", "Steals", "Blocks", "Turnovers", "Fouls", "Points"]
    
    playerNames = getPlayerNames()
    
    allPlayerAverage_dict = {}
    
    #feelin' loopy
    for name in playerNames:
        playerDataIndividual = {}
        for column in columns:
            
            if(column == "Name"):
                playerDataIndividual[column] = name
            else:
                average = getPlayerAverage(name, column, digits_to_round)
                playerDataIndividual[column] = average
        
        allPlayerAverage_dict[name] = playerDataIndividual
    
    with open(path, 'w', encoding='utf-8', newline='') as averageFile:
        averageFile.truncate(0)
        
        writer = csv.DictWriter(averageFile, fieldnames=columns)
        writer.writeheader()
        
        for name in playerNames:
            writer.writerow(allPlayerAverage_dict[name])

            
            
            

        
    
    
