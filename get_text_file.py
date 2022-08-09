import os
import glob

def get_text(mypath):

    text_file = max(glob.glob(mypath), key=os.path.getmtime)

    return text_file



