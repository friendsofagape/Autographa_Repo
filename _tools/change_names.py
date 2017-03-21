import codecs
import os
import re
import sys.argv

# Currently I'm hard coding the 
FILE_PATH = "d:\Downloads\Bible\Hindi\Autographa\Autographa_Repo\Bibles\Hindi\ULB"
fileLists = os.listdir(FILE_PATH)
directory = os.path.dirname(FILE_PATH+"/usfm")

try:
    os.stat(directory)
except:
    os.mkdir(directory)
    
for fil in fileList:
    fc = fil.split(".")
    if fc[-1] == "usfm":
        
        
