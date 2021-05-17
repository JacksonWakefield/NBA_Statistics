import pandas as pd
#Requires exact name in player_reference as string
def getPlayerDataFrame(player_name):
    name = player_name + ".csv"
    path = "../player_data/" + name
    try:
        return pd.read_csv(path)
    except:
        raise Exception('Could not find player data for: ' + player_name + "\n Path: " + path)
