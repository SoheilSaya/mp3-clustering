import os
import shutil

# Assume the list of lists is called files
files = [
['Mohsen Ebrahimzadeh - Darde Del (Remix).mp3',
    'Mohsen Ebrahimzadeh - Doneh Doneh (Remix).mp3',
    'Mohsen Ebrahimzadeh - Doneh Doneh (Remix)2.mp3'],
['Shahab Tiam - Bi Hashiyeh (Iromusic).mp3',
    'Shahab Tiam - Ki Nemidooneh (Iromusic).mp3'],
['Aref - Eshgh.mp3',
    'Aref - Hala Khaili Direh.mp3']

]

# Assume the current directory is called source_dir
source_dir = os.getcwd()

# Iterate over the list of lists
for file_list in files:
    # Create a folder name based on the first file in each inner list
    namestr=f'{file_list[0].split(" ")[0]} {file_list[0].split(" ")[1]}'
    folder_name = namestr
    # Create the destination directory path
    dest_dir = os.path.join(source_dir, folder_name)
    # Make the destination directory if it does not exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # Iterate over the files in each inner list
    for file in file_list:
        # Create the source file path
        src_path = os.path.join(source_dir, file)
        # Create the destination file path
        dest_path = os.path.join(dest_dir, file)
        # Move the file from source to destination
        shutil.move(src_path, dest_path)
