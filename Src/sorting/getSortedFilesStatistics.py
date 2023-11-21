
import json 

sortedFilesStatisticsPath = r".\data\sorting\sortedFilesStatistics.json"


def getSortedFileStatistics():
    
    with open( sortedFilesStatisticsPath , 'r') as file:
        
        data = json.load( file ) 
        print(data) 
        
        
getSortedFileStatistics() 