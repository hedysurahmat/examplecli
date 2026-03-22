import os,shutil
for f in os.listdir():
    if f.endswith(".txt"):
        os.makedirs("txt",exist_ok=True)
        shutil.move(f,"txt/"+f)
