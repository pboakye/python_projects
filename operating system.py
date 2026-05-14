import os
import shutil
from os import makedirs

extensions_directory = {".pdf" : "Documents",
                          ".jpg" : "Pictures",
                          ".docx" :"Documents",
                          ".xlsx" :"Documents",
                          ".mp3" : "Music",
                          ".png" : "Pictures",
                           ".mkv" : "Video"
                          }
system_files = r"C:\Users\PRINCE\Desktop"
files = os.listdir(system_files)
for file in files:
    print(f"checking files {files}")
    os.path.splitext(file)
    name,extension = os.path.splitext(file)
    if extension in extensions_directory:
        folder_name = extensions_directory[extension]
        docs_folder = os.path.join(system_files, "Documents")
        if not os.path.exists(docs_folder):
            makedirs(docs_folder)
        source = os.path.join(system_files, file)
        destination = os.path.join(docs_folder, file)
        shutil.move(source, destination)
        print(f"Done! Moved {file} to {folder_name}")












