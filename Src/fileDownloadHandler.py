
from watchdog.events import FileSystemEventHandler



class FileDownloadHandler( FileSystemEventHandler ):
    
    def __init__(self):
        
        self.downloadedFilePaths = []
        
    def on_created(self, event):
        
        filepath = event.src_path 
        
        if event.is_directory:
            return 
        
        print(" Download Started ") 
        
        
    def on_modified(self, event):
        
        filepath = event.src_path 
        
        print(f" - { filepath }")
        
        if event.is_directory:
            return
            
        if filepath in self.downloadedFilePaths:
            return
        else:
            
            self.downloadedFilePaths.append( filepath )
            print(f" File Downloaded : { filepath }") 
            