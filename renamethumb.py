import shutil
import os

files = os.listdir("C:/Users/ASHER/Desktop/Thumb")
for i in range(len(files)):
    os.rename("C:/Users/ASHER/Desktop/Thumb/" + files[i],"C:/Users/ASHER/Desktop/Thumb/thumb-" + files[i])
