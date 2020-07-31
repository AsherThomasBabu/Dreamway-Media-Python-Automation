import shutil
import os

folder = os.listdir("C:/Users/ASHER/Desktop/Final")

for i in range(len(folder)):
    dest = os.listdir("C:/Users/ASHER/Desktop/Final/" + folder[i])

    source = dest.copy()

    for j in range(7):
        dest[j] = dest[j].lower().replace(" ", "-")
        temp = dest[j].partition(".")[2]
        dest[j] = dest[j].replace(".", "-")+"."+temp
        os.rename("C:/Users/ASHER/Desktop/Final/" + folder[i] + "/" + source[j], "C:/Users/ASHER/Desktop/Final/" + folder[i] + "/" + dest[j])
