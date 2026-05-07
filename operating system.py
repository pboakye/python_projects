import os
system_files = r"C:\Users\PRINCE\Downloads"
files = os.listdir(system_files)
print(files)
for file in files:
    print(f"checking files {files}")
    os.path.splitext()
    name,extension = os.path.splitext(file)
    import shutil
    docs_folder = os.path.join(system_files ,"Documents")
    if not os.path.exists(docs_folder):
        os.makedirs(docs_folder)
        if extension == ".pdf":
            source = os.path.join(system_files,file)
            destination = os.path.join(docs_folder,file)
            shutil.move(source,destination)
            print(f"Moved {file} Successfully")
            extensions_directory = {".pdf" : "Documents",
                          ".jpg" : "Pictures",
                          ".docx" :"Documents",
                          ".xlsx" :"Documents",
                          ".mp3" : "Music",
                          ".png" : "Pictures"
                          }
            if extension in extensions_directory:
                folder_name = extensions_directory[extension]


