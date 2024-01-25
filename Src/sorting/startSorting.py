
from sorting.fileDownloadEventHandler import FileDownloadEventHandler
from sorting.fileDownloadTracker import DownloadTracker 
from sorting.downloadManager import DownloadManager
import time 

downloadsPath = r"C:\Users\OGAGAOGHENE\Downloads"


def startSorting():
    
    print(" Starting File Sorting ") 
        
    downloadManager = DownloadManager()
    fileDownloadEventHandler = FileDownloadEventHandler( downloadManager ) 
    downloadTracker = DownloadTracker() 
    downloadTracker.initiate(fileDownloadEventHandler, downloadsPath ) 
    
    print(" File Sorting Started ") 
     # Sort loop 
    
    try:
        while True:    
            time.sleep(1)
            pass
        
    except KeyboardInterrupt:
        downloadTracker.stop() 