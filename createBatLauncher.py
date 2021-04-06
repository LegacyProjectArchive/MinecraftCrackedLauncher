import os

nativesArg = "\"-Djava.library.path=libraries\""

jarsArg = "-classpath \"minecraft.jar;"
for file in os.listdir("libraries"):
    if file[-4:] == ".jar":
        jarsArg += "libraries\\" + file + ";"
jarsArg = jarsArg[:-1]+ "\""

name = input("Enter name : ")
uuid = input("Enter UUID : ")

if name == "":
    name = "Unknown"

if uuid == "":
    uuid = "0"

prgmArgs = f"--version mcp, --assetsDir assets --username {name} --accessToken --uuid {uuid}"

fileContent = \
f"""java {nativesArg} -Dfile.encoding=UTF-8 {jarsArg} net.minecraft.client.main.Main {prgmArgs}
PAUSE"""

with open("launch.bat", "w") as file:
    file.write(fileContent)

print("launch.bat created successfully !")
os.system("PAUSE")
