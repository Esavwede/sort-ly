from sorting.util.functions.sorting import extract_extension
from watchdog.events import FileSystemEventHandler


class FileDownloadEventHandler( FileSystemEventHandler ):
    
    def __init__(self, downloadManager ):
        
        self.downloadManager = downloadManager 
        
    def on_created(self, event):
        
        filepath = event.src_path 
        
        if event.is_directory:
            return 
        
        print(" New file created ") 
        print( filepath )
        
        
    def on_modified(self, event):
        
        if event.is_directory:
           return
       
        filepath = event.src_path 
        fileExtension = extract_extension( filepath )       
       
        
        if fileExtension == "tmp" or fileExtension == "crdownload" or "":
            return 
        
          
        if filepath in self.activeDownloads:
            print( filepath + "MODIFIED") 
            return
        
        else:

            self.downloadManager.manageDownload(filepath)
            print(f" Added file for download tracking : { filepath }")
            