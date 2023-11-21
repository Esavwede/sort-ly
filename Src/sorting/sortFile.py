
from loadSortingConfig import loadSortConfig 
from aiSort import * 


#### Sample File Paths 

audioPath = r"C:\Users\OGAGAOGHENE\Downloads\sunrise-groove-176565.mp3"
videoPath = r"C:\Users\OGAGAOGHENE\Downloads\This is why Udemy earnings are dropping.mp4.mp4"
documentPath = r"C:\Users\OGAGAOGHENE\Downloads\Sort-ly Algoritm.pdf"
imagePath = r"C:\Users\OGAGAOGHENE\Downloads\klusterthon.jpg.jpg"


def sort(filePath):
    
    #file sorting 
    print("Sorting File")
    sortConfig = loadSortConfig()
    compressSortedFile = sortConfig['compressSortedFile'] #Boolean 
    rootFilePath = getRootDir(filePath)
    
    
sort( audioPath )