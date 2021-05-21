import Analysis_Tools as at

names = at.getPlayerNames()

#durantFrame = dm.getPlayerDataFrame("Stephen Curry")

#durantFrame.plot(kind = "line", x = "Date", y = "Minutes", figsize = (10, 10))

playerAverageDataFrame = at.getAllPlayerAverageDataFrame()

playerPointsHead = playerAverageDataFrame.sort_values('Points', ascending=False).head(10)

playerPointsHead.plot(x='Name', y='Points', kind='bar', figsize=(10, 10))