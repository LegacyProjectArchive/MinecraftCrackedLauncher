import os
import zipfile

with zipfile.ZipFile("minecraft.jar") as jar:
    print("Getting all files in minecraft.jar...")
    allFiles = jar.namelist()
    print("Evaluating which files to extract...")
    filesToExtract = [file for file in jar.namelist() if file[:6] == "assets"]
    print("Extracting files...")
    jar.extractall(members=filesToExtract)

print("Successfully extracted assets !")
os.system("PAUSE")
