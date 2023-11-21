import filetype
import os 

HOME_DIR = os.path.expanduser("~") 
DOWNLOADS_DIR = os.path.join( HOME_DIR, 'Downloads' )
DOCUMENTS_DIR = os.path.join( HOME_DIR, 'Documents' )
MUSIC_DIR = os.path.join( HOME_DIR, 'Music' )
PICTURES_DIR = os.path.join( HOME_DIR, 'Pictures' )
VIDEOS_DIR = os.path.join( HOME_DIR, 'Videos' )


def getFileType( filePath ):
    
    fileExists = os.path.exists( filePath ) 
    if fileExists:
        file = filetype.guess( filePath ) 
        mime = file.mime 
        fileType = mime.split("/")[0] 
        print( mime )
        return fileType 
        
    else:
        print('Specified Path does not exist ')
        return 'null'
    
def getRootDir( filePath ):
    
    fileType = getFileType( filePath ) 
    fileType = fileType.lower() 
    
    
    if fileType == "video":
        print("Video File Type ")
        print(f" Videos Root Dir: { VIDEOS_DIR }")
        return VIDEOS_DIR
        
    elif fileType == "image":
        print(" Picture File type ")
        print(f" Pictures Root Dir: { PICTURES_DIR }")
        return PICTURES_DIR
        
    elif fileType == "audio":
        print("Audio file type ")
        print(f"Music Root Dir: { MUSIC_DIR }")
        return MUSIC_DIR 
    
    else:
        print(" Document File Type ") 
        print(f" Document Root Dir: { DOCUMENTS_DIR }")
        return DOCUMENTS_DIR 
    
