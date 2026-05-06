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

