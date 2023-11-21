
from sorting.fileDownloadHandler import FileDownloadHandler
from sorting.fileDownloadTracker import DownloadTracker 
import time 

downloadsPath = r"C:\Users\OGAGAOGHENE\Downloads"


def startSorting():
    
    print(" Starting File Sorting ") 
        
    fileDownloadHandler = FileDownloadHandler() 
    downloadTracker = DownloadTracker() 
    downloadTracker.initiate(fileDownloadHandler, downloadsPath ) 
    
    print(" File Sorting Started ") 
     # Sort loop 
    
    try:
        while True:    
            time.sleep(1)
            pass
        
    except KeyboardInterrupt:
        downloadTracker.stop() 
        
        
