

from watchdog.observers import Observer 


class DownloadTracker():
    
    def __init__(self):
        
        self.observer = None 
        
    def initiate(self, fileDownloadHandler, filePath ):
        
        try:
            
            self.observer = Observer() 
            self.observer.schedule( fileDownloadHandler, filePath, recursive=False )
            self.observer.start()  
            
        except Exception as Error:
            
            print(f"Error occured while lauching download tracker: { Error } ") 
            
        else: 
            
            print(" Download tracker started ")
        
            
            
    def stop(self):
            
        print(" Stopping Download Tracker ") 
        self.observer.stop()
        self.observer.join()
        print(" Download Tracker Stopped ") 
    