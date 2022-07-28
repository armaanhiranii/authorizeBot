#get text file

import os
import glob

def get_text():

    mypath = r"C:\Users\conf.asst5\downloads\*.*"

    
    text_file = max(glob.glob(mypath), key=os.path.getmtime)

    return text_file




