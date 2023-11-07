
from fileDownloadHandler import FileDownloadHandler
from fileDownloadTracker import DownloadTracker 
import time 

downloadsPath = r"C:\Users\OGAGAOGHENE\Downloads"

def main():
    
    print(" Sort-ly ")
    
    
    fileDownloadHandler = FileDownloadHandler() 
    downloadTracker = DownloadTracker() 
    downloadTracker.initiate(fileDownloadHandler, downloadsPath ) 
    
    # program loop 
    
    try:
        while True:
            
            time.sleep(1)
            pass
    except KeyboardInterrupt:
        downloadTracker.stop() 
        
main()