import os
import json
import sys
import platform
import urllib.request

def getAllowedSystems(lib):
    if "rules" in lib:
        allowedSystems = []
        notAllowedSystems = []
        for rule in lib["rules"]:
            if rule["action"] == "allow":
                if "os" in rule:
                    allowedSystems.append(rule["os"]["name"])
                else:
                    allowedSystems = list(allSystems)
            else:
                notAllowedSystems.append(rule["os"]["name"])
        for syst in allSystems:
            if syst in allowedSystems and syst in notAllowedSystems:
                allowedSystems.remove(syst)
    else:
        allowedSystems = list(allSystems)
    return allowedSystems

def downloadFile(data):
    print("Downloading " + data["url"])
    urllib.request.urlretrieve(data["url"], "libraries/" + data["path"].split("/")[-1])

system = platform.system()

if system == "Windows":
    system = "windows"
elif system == "Linux":
    system = "linux"
else:
    print("Could not recognize your system. For the moment, only windows and linux are supported", file=sys.stderr)
    sys.exit(0)

os.mkdir("libraries/")

with open("version.json", "r") as file:
    content = file.read()

jsonContent = json.loads(content)

minecraftUrl = jsonContent["downloads"]["client"]["url"]
print("Downloading " + minecraftUrl);
urllib.request.urlretrieve(minecraftUrl, "minecraft.jar")

allSystems = ["windows", "linux"]

for lib in jsonContent["libraries"]:
    allowedSystems = getAllowedSystems(lib)
    if system in allowedSystems:
        downloads = lib["downloads"]
        downloadFile(downloads["artifact"])
        if "classifiers" in downloads:
            classifiers = downloads["classifiers"]
            if "natives-" + system in classifiers:
                downloadFile(classifiers["natives-" + system])

print("Downloaded minecraft and its dependencies successfully !")
os.system("PAUSE")
