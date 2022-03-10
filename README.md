DL_ACES_Setup v01.1

- DESCRIPTION
This script creates a simple button in Nuke, to set the ACES workflow quickly.

--------------------------------------------------------------------------------------------------------
- HOW TO INSTALL
To download from Github, click on the green button (called Code), then click on "Download ZIP".
Probably the folder should be named as "DL_ACES_Setup-main", so rename it as "DL_ACES_Setup" (if necessary), 
then move it to your ".nuke" directory.

In your ".nuke" folder, open the files "init.py" and "menu.py". If it doesn't exist, just simply create a new
"txt" file, give their respective names, and put ".py" as an extension (for both files).

In your "init.py":
nuke.pluginAddPath('./DL_ACES_Setup')

In your "menu.py":
from DL_ACES_Setup import *

You just to need to make sure that your folder ("DL_ACES_Setup"), has the same name and the same 
directory when you are setting in your "init.py".

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