import os
import shutil

def list_directory(destination_path):
    # List Directory
    try:
        print(os.listdir(destination_path))
    except FileNotFoundError as e:
        print(e)
    except Exception as ex:
        print(ex)
        
def sort_directory(sourcePath):
    list = []
    os.chdir(sourcePath)
    for file in os.listdir():
        findDot = file.rfind('.')
        if findDot < 0 or file[findDot:] == '.DS_Store':
            continue
        else:
            prefix = file[findDot:]
            if prefix not in list:
                list.append(prefix)
    return list

def rename_file(old_file_path, new_file_path):
    try:
        # Change File Name
        os.rename(old_file_path, new_file_path)
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)

def move_files(destination_path, current_path, data):
    # Move Files from Current Path to New Path
    try:
        for file in data:
            old_file = os.path.join(current_path, file)
            shutil.move(old_file, destination_path)
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)

def create_folder(specified_path, filePath, prefix):
    try:
        # Specified Path - Documents Folder
        # File Path - Downloads Folder - Folder to Sort
        
        # print(checkPrefix)  #.docx
        # print(prefix)   #DOCX
        checkPrefix = prefix
        prefix = prefix.replace('.', '').upper()
        
    
        newPath = os.path.join(specified_path, prefix)  
        # NewPath uses Specified Path - Folder produced in NewPath
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            
       # Formats data of Downloads Folder, Uses check prefixes   
        print(filePath)
        data = format_folder(filePath, checkPrefix)  # Bug 
        print(data)

        # Checks if data is available
        if not data:  
            return 
        move_files(newPath, specified_path, data)
        
    except FileExistsError as f:
        print(f)
    except Exception as e:
        print(e)

def format_folder(current_path, prefix):
    arr = []
    print(arr)
    for file in os.listdir(current_path):
        print(file)
        if file.lower().endswith(f"{prefix}"):
            old_file = os.path.join(current_path, file)
            new_file = ''.join(file.split("-"))
            new_file = os.path.join(current_path, file)
            rename_file(old_file, new_file) # Renames Files
            arr.append(new_file)  
            
    if arr:
        arr = sorted(arr)
    return arr


