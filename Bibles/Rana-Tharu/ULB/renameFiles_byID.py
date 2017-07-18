'''
Rename the usfm files in a directory based on the \id tag  
'''
import os
import re
import codecs
import pdb

def getBookNum(bookCode):
    bk = {"MAT":"41", "MRK":"42", "LUK":"43", "JHN":"44", "ACT":"45", "ROM":"46", "1CO":"47", "2CO":"48", "GAL":"49", "EPH":"50", "PHP":"51", "COL":"52", "1TH":"53", "2TH":"54", "1TI":"55", "2TI":"56", "TIT":"57", "PHM":"58", "HEB":"59", "JAS":"60", "1PE":"61", "2PE":"62", "1JN":"63", "2JN":"64", "3JN":"65", "JUD":"66", "REV":"67"}
    try:
        return(bk[bookCode])
    except KeyError:
        return("UNK***_" + bookCode)

files = os.listdir(".")

for file in files:
    try:
        if(file.split(".")[-1].lower()=="usfm" or file.split(".")[-1].lower()=="sfm"):
            f=codecs.open(file, mode='rb', encoding="utf-8")
            fc = f.read()
            f_id=re.search("\\\\id\s+(.{3})", fc, re.U)
            os.rename(file, getBookNum(f_id.group(1)) + "_" + str(f_id.group(1)) + ".usfm")
            f.close()
    except Exception as e:
        # pdb.set_trace()
        print(file, e.message)
        pass
