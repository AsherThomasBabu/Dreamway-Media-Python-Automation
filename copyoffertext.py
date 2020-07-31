import shutil
import os

folder = os.listdir("C:/Users/ASHER/Desktop/Final")

for file in folder:
    shutil.copy("C:/Users/ASHER/Desktop/special-offer.txt","C:/Users/ASHER/Desktop/Final/" + file)