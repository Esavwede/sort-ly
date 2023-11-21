
import logging 
from system.Application_Monitoring import Application_Monitoring
from sorting.startSorting import startSorting 


# Application Monitoring
Application_Monitoring() 

# Application Logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=
    [
        logging.FileHandler('app.log') 
    ]
)


# Sorting Enabled or Disable 
fileSortingEnabled=True 


def main(): 
    
    if fileSortingEnabled:
        
        logging.info('File Sorting  Enabled ')
        startSorting() 
     
    else:
        logging.info('File Sorting Disabled ')
        return 0 
        
main()