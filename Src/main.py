
from fileDownloadHandler import FileDownloadHandler
from fileDownloadTracker import DownloadTracker 
import time 
from startSorting import startSorting 


# Sorting Enabled 
fileSortingEnabled=True 


def main():
    
    print(" Sort-ly ")
    
    if fileSortingEnabled:
        startSorting() 
    else:
        print(" File Sorting disabled ") 
        return 0 
        
main()