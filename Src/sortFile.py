
from loadSortingConfig import loadSortConfig 

def sort():
    
    #file sorting 
    print("Sorting File")
    sortConfig = loadSortConfig() 
    
    if sortConfig['compressSortedFiles']:
        
        print(" Compress Sorted File: True ") 
    else:
        
        print(" Compress Sorted File False ") 
        
    print(" File sorted to: ")
    
sort()