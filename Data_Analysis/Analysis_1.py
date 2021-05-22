#Contains some basic plotting functions

import Analysis_Tools as at
import pandas as pd

#types of charts - taken from pd docs
#represents type_of_chart parameter
'''
The kind of plot to produce:

‘line’ : line plot (default)
‘bar’ : vertical bar plot
‘barh’ : horizontal bar plot
‘hist’ : histogram
‘box’ : boxplot
‘kde’ : Kernel Density Estimation plot
‘density’ : same as ‘kde’
‘area’ : area plot
‘pie’ : pie plot
‘scatter’ : scatter plot
‘hexbin’ : hexbin plot.
'''

#plots head/tail average of Y = category, X = name for any stat
#
def plotSingleAxisAverage(Y, numNames = 10, head = True, sizeX = 10, sizeY = 10, type_of_chart = "line"):
    dataframe = at.getAllPlayerAverageDataFrame().sort_values(Y, ascending = not head).head(numNames)
    dataframe.plot(x = "Name", y = Y, figsize = (sizeX, sizeY), kind = type_of_chart)

plotSingleAxisAverage("Assists", numNames = 10, type_of_chart="bar")
    