
import os 
import time 

class Download:
    
    def __init__(self, filepath, downloadCompleteCallback ):
        
        self.filepath = filepath
        self.prevSize = 0
        self.currentSize = 0 
        self.complete = False 
        self.downloadCompleteCallback = downloadCompleteCallback
        
        
    def checkDownloadComplete(self):
        
        time.sleep(10) 
        print("Checking if Download Complete ") 
        currentSize = os.path.getsize( self.filepath ) 
        
        if self.prevSize == currentSize:
            self.complete = True 
            print("DOWNLOAD COMPLETED")
        else:
            self.prevSize = currentSize
            
            
    def startTracker(self):
        
        print("Download Tracker Started ") 
        while self.complete == False:
            
            self.checkDownloadComplete()
        
        self.downloadComplete() 
            
            
    def downloadComplete(self):
        
        self.downloadCompleteCallback( self.filepath ) 
        del self 
        

class DownloadManager:
    
    def __init__(self):
        
        self.incompleteDownloads = []
        self.completedDownloadsPath = [] 
        
    def manageDownload(self, filepath ):
        
        print(" Managing File Download ")
        
        newDownload = Download(filepath, self.downloadComplete)
        newDownload.startTracker() 
        self.incompleteDownloads.append( newDownload )
    
        
    def downloadComplete(self, filepath ):
        
        self.completedDownloadsPath.append( filepath )
        print(" File Path Added To Completed Downloads Path ")
        
        print( self.incompleteDownloads ) 
        # AI processor 