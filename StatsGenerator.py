
#HEADER

import json

import Scraper_Master

import csv

def Update_Player_Statistics(year):
    
    player_stats = {}
    player_reference = {}
    
    
    
    #with open('PlayerReference.json', 'r', encoding='utf8') as Player_Reference:
    #    player_reference = json.load(Player_Reference)
    with open('SunsReference.json', 'r', encoding='utf8') as Player_Reference:
        player_reference = json.load(Player_Reference)

    
    urls = []
    
    for key in player_reference:
        urls.append("https://www.basketball-reference.com/" + player_reference[key] + "/gamelog/" + str(year) + "/")
    
    columns = ["Date", "Team", "Opponent", "Home(0)/Away(1)", "Margin", "Minutes", "FGA", "FGM", \
               "3PA", "3PM", "Rebounds", "Assists", "Steals", "Blocks", "Turnovers", "Fouls", "Points"]
    
    soup_columns = ["date_game", "team_id", "opp_id", "game_location", "game_result", "mp", "fga", "fg", \
                    "fg3a", "fg3", "trb", "ast", "stl", "blk", "tov", "pf", "pts"]
    
    for url in urls:
    
        player_soup = Scraper_Master.Scrape_From_Source(url)
        
        player_name = player_soup.find(name = "h1", attrs = {"itemprop" : "name"}).text.split(" 20")[0][1:]
        
        
        player_data_all = []
        
        player_data_rows = player_soup.find(name="div", attrs = {"id": "all_pgl_basic"}).findAll(name="tr")
        
        for row in player_data_rows:
            
            if("Rk" in row.text):
                continue
            
            player_data_individual = {}
            
            index = 0
            
            for column in soup_columns:
                
                #clean out header rows
                if("Did Not Play" in row.text or "Inactive" in row.text or "Did Not Dress" in row.text or "Not With Team" in row.text):
                    continue    
                try:
                    player_data_cell_text = row.find(name="td", attrs = {"data-stat" : column}).text
                except:
                    print(row.text)
                #little adjustments
                if(column == "game_location"):
                    if(player_data_cell_text == ""):
                        player_data_cell_text = 0
                    else:
                        player_data_cell_text = 1
                
                elif(column == "game_result"):
                    player_data_cell_text = player_data_cell_text[1:-1]
                    player_data_cell_text = player_data_cell_text.replace("(", "")
                
                player_data_individual[columns[index]] = player_data_cell_text
                index += 1
                
            player_data_all.append(player_data_individual)
        
        player_stats[player_name] = player_data_all
        
        print(player_name)
       
    for name in player_stats:
        with open('player_data/'+ name + '.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = columns)
            #rint(player_stats.keys())
            writer.writeheader()
        
            for games in player_stats[name]:
                writer.writerow(games)
                
            csvfile.close()
        

Update_Player_Statistics(2021)
