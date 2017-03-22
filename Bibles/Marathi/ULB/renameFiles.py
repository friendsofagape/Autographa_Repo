import os
import re

for f in os.listdir("."):
     if f.split(".")[-1] == "usfm":
             nf=re.match("(\d{2})_(\d) (.{2}).*$", f) # The regex pattern
             try:
                     os.rename(f, nf.group(1) + "_" + nf.group(2) + nf.group(3) + ".usfm")             
             except:
                     pass
