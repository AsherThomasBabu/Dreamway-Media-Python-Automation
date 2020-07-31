import shutil
import os

folder = os.listdir("C:/Users/ASHER/Desktop/Final")
for i in range(len(folder)):
    shutil.make_archive(folder[i]+"-etsy", 'zip',"C:/Users/ASHER/Desktop/Final/" + folder[i])