import os
import shutil
from automtionCommands import create_folder, sort_directory

def runCleanUp(newDirectory, currentDir, prefixData):
    # Chck if prefix actually is a prefix 
    try:
        for prefix in prefixData:
            print(prefix)
            prefix = ''.join(prefix.split())
            create_folder("/Users/josh-v/Documents", current_dir, prefix) # Error with file
    except Exception as e:
       print(e)




if __name__ == '__main__':
    current_dir = "/Users/josh-v/Downloads"
    os.chdir(current_dir)
    prefixData = sort_directory(current_dir)
    runCleanUp("/Users/josh-v/Documents", current_dir, prefixData)
