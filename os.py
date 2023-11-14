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
        # New Path
        newPath = os.path.join(specified_path, prefix)
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        else:
            print('Folder already exists')
            
        data = format_folder(filePath, prefix)
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
    for file in os.listdir(current_path):
        if file.lower().endswith(f".{prefix}"):
            old_file = os.path.join(current_path, file)
            new_file = ''.join(file.split("-"))
            new_file = os.path.join(current_path, file)
            rename_file(old_file, new_file) # Renames Files
            arr.append(new_file)  
        else:
            continue

    if arr:
        arr = sorted(arr)
    return arr


if __name__ == '__main__':
    current_dir = "/Users/josh-v/Downloads"
    prefix = 'jpg'
    os.chdir(current_dir)
    create_folder("/Users/josh-v/Documents", current_dir, prefix) 