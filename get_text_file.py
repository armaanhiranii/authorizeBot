#get text file

import os
import glob

def get_text():

    mypath = "/Users/armaanhirani/Downloads/*.*"

    
    text_file = max(glob.glob(mypath), key=os.path.getmtime)

    return text_file

print(get_text())


