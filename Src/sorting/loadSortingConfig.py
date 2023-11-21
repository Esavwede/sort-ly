
import json 

jsonFilePath = r".\data\config\sortingConfig.json"

def loadSortConfig():
    
    print(" Loading Sorting Configurations ") 
    
    # Load Sorting Configuration File 
    with open(jsonFilePath,'r') as file:
        
        data = json.load(file) 
        return data 
        
        
loadSortConfig()    