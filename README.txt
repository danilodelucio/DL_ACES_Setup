DL_ACES_Setup v01.1

- DESCRIPTION
This script creates a simple button in Nuke, to set the ACES setup quickly.

--------------------------------------------------------------------------------------------------------
- HOW TO INSTALL
In your ".nuke" folder, open the "init.py" and "menu.py". If it doesn't exist, just simply create a new
"txt" file, give the name and put ".py" as an extension.

In your "init.py", put your own path to access the "DL_ACES_Setup" folder:
nuke.pluginAddPath('C:/DL_ACES_Setup')

In your "menu.py":
from DL_ACES_Setup import *

--------------------------------------------------------------------------------------------------------
- INFOS
If you want to use a custom OCIO config, replace the current path in "aces_custom" function 
(in "DL_ACES_Setup.py"), for your own path.

The "viewerProcess" in your Nuke, it will load the first item on "active_views" in your
"config.ocio" file, so if you want to set a specific view when this script loads, just put it as a first item.
 
The Colorspace for all the selected Read nodes will be changed as well, so if you want to use
another one, just simply change from "scene_linear" to whatever you want.

--------------------------------------------------------------------------------------------------------
Author: Danilo de Lucio
Website: www.danilodelucio.com
Date: March/2022