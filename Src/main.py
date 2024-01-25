
from system.Application_Monitoring import Application_Monitoring
from sorting.startSorting import startSorting 


# Application Monitoring
Application_Monitoring() 

# Sorting Enabled or Disable 
fileSortingEnabled=True 


def main(): 
    
    if fileSortingEnabled:
        
        print(" File Sorting Enabled ")
        startSorting() 
     
    else:
        
        print("File Sorting Disabled ") 
        return 0 
        
main()