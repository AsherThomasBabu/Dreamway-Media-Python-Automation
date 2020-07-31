import shutil
import os

folder = os.listdir("C:/Users/ASHER/Desktop/Final")
for i in range(len(folder)):
    temp = folder[i].lower()
    os.rename("C:/Users/ASHER/Desktop/Final/"+folder[i],"C:/Users/ASHER/Desktop/Final/"+temp)