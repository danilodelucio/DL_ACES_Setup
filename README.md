# DL_ACES_Setup
This script creates a simple button, to set the ACES workflow quickly inside of Nuke.

![DL_ACES_Setup - PrintScreen](https://user-images.githubusercontent.com/47226196/157560621-d8cf5847-0861-4c51-9917-41977364390b.png)


--------------------------------------------------------------------------------------------------------
# HOW TO INSTALL
 To download from Github, click on the green button (called <strong>Code</strong>), then click on "Download ZIP".
Probably the folder should be named as <strong>"DL_ACES_Setup-main"</strong>, so rename it as <strong>"DL_ACES_Setup"</strong> (if necessary), 
then move it to your <strong>".nuke"</strong> directory.

 In your <strong>".nuke"</strong> folder, open the files <strong>"init.py"</strong> and <strong>"menu.py"</strong>. If it doesn't exist, just simply create a new
<strong>"txt"</strong> file, give their respective names, and put <strong>".py"</strong> as an extension (for both files).

![DL_ACES_Setup - PrintScreen 02](https://user-images.githubusercontent.com/47226196/157562990-1ddab487-6b62-44c0-877a-746a8162661b.png)

 In your <strong>"init.py"</strong>:
<p><code>nuke.pluginAddPath('./DL_ACES_Setup')</code>

 In your </strong>"menu.py"</strong>:
<p><code>from DL_ACES_Setup import *</code>
<blockquote>
 You just to need to make sure that your folder (<strong>"DL_ACES_Setup"</strong>), has the same name and the same 
directory when you are setting in your <strong>"init.py"</strong>.
</blockquote>

--------------------------------------------------------------------------------------------------------
# INFOS
 <p>If you want to use a <strong>custom OCIO config</strong>, replace the current path in <strong>"aces_custom"</strong> function 
(in <strong>"DL_ACES_Setup.py"</strong>), for your own path.
 
 ![DL_ACES_Setup - PrintScreen 03](https://user-images.githubusercontent.com/47226196/157563287-34e2c98b-3e71-4d64-ad4b-47071bcc5ae5.png)

 The <strong>"viewerProcess"</strong> in your Nuke, it will load the first item on <strong>"active_views"</strong> in your
 <strong>"config.ocio"</strong> file, so if you want to set a specific view when this script loads, just put it as a first item.

 ![DL_ACES_Setup - PrintScreen 04](https://user-images.githubusercontent.com/47226196/157564068-0bcbcabd-12d3-475d-bb73-9a41b2817339.png)
 
 The <strong>Colorspace</strong> for all the selected Read nodes will be changed as well, so if you want to use
 another one, just simply change from <strong>"scene_linear"</strong> to whatever you want.

 ![DL_ACES_Setup - PrintScreen 06](https://user-images.githubusercontent.com/47226196/157564472-d2726f37-bc99-4e1c-b8af-26a0178e2f70.png)
 ![DL_ACES_Setup - PrintScreen 05](https://user-images.githubusercontent.com/47226196/157564325-868ba29b-1a9c-4090-b867-10ba28356856.png)

--------------------------------------------------------------------------------------------------------
<strong>
Author: Danilo de Lucio
<p>Website: www.danilodelucio.com
<p>March/2022
</strong>
