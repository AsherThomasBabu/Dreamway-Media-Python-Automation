import shutil
import os

tiwiw = os.listdir("C:/Users/ASHER/Desktop/-tiwiw")
t = os.listdir("C:/Users/ASHER/Desktop/-etsy")

final = os.listdir("C:/Users/ASHER/Desktop/Final")

for i in range(122):
    shutil.copy("C:/Users/ASHER/Desktop/-tiwiw/" + tiwiw[i], "C:/Users/ASHER/Desktop/Final/" + final[i])
    shutil.copy("C:/Users/ASHER/Desktop/-etsy/" + t[i], "C:/Users/ASHER/Desktop/Final/" + final[i])

print(final)