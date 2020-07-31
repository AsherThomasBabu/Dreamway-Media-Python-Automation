import shutil
import os

files = os.listdir("C:/Users/ASHER/Desktop/Wedding")

new = []

for i in range(000, len(files), 5):
    split_str = files[i].split(".",1)
    substr = split_str[0]
    new.append(substr)
    os.mkdir("C:/Users/ASHER/Desktop/Final/" + str(i).zfill(3))
    for j in range(5):
        shutil.move("C:/Users/ASHER/Desktop/Wedding/" + files[i+j], "C:/Users/ASHER/Desktop/Final/" + str(i).zfill(3))

print(new)
