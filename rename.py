import os

def rename_files(directory, prefix):
    if not os.path.exists(directory):
        print("Directory not found!")
        return
    
    files = os.listdir(directory)
    for index, file in enumerate(files):
        old_path = os.path.join(directory, file)

        if not os.path.isfile(old_path) or file.startswith('.'):
            continue

        file_extension = os.path.splitext(file)[1]

        new_name = f"{prefix}_{index + 1}{file_extension}"
        new_path = os.path.join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        except OSError as e:
            print(f"Error renaming {file}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    name_prefix = input("Enter the prefix for renaming: ").strip()
    if not os.path.isdir(folder_path):
        print("Invalid directory path!")
    else:
        rename_files(folder_path, name_prefix)
