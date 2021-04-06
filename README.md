# MinecraftCrackedLauncher
You can use this to launch any version you want (you just need the version.json file)

# How to use it
Copy the file `.minecraft/versions/<version>/<version>.json` (`version` is the version in which you want to play) in the folder where you have downloaded these files.
Rename it `version.json`.
If you don't have Python, install it (or ask someone to "compile" the code).
Launch `downloadMinecraft.py`. This will download the minecraft jar and the dependencies. Wait until it tells you it is finished.
Launch `extractAssets.py`. For the moment, the assets are in the jar. This file extracts them. Wait until it tells you it is finished.
Launch `createBatLauncher.py`. This will create the bat file used to launch Minecraft.

# How to launch the game
You just have to launch `launch.bat`, and Minecraft should start !
