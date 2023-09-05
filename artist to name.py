import os
import eyed3

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            audiofile = eyed3.load(file_path)
            artist = audiofile.tag.artist
            new_filename = f"{artist}.mp3"
            new_file_path = os.path.join(directory, new_filename)
            i = 1
            while os.path.exists(new_file_path):
                new_filename = f"{artist} ({i}).mp3"
                new_file_path = os.path.join(directory, new_filename)
                i += 1
            os.rename(file_path, new_file_path)

current_directory = os.getcwd()
rename_files(current_directory)