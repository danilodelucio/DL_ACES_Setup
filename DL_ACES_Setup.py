# --------------------------------------------------------------
#  DL_ACES_Setup.py
#  Version: v01.1
#  Author: Danilo de Lucio
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates a simple button in Nuke, to set the ACES setup quickly.
# --------------------------------------------------------------

import nuke

def colorspaceReads():
    for i in nuke.selectedNodes("Read"):
        i["colorspace"].setValue("scene_linear")

def aces_1_0_3():
    s = nuke.root()
    s["colorManagement"].setValue(1)
    s["OCIO_config"].setValue(0)
    colorspaceReads()

def aces_1_1():
    s = nuke.root()
    s["colorManagement"].setValue(1)
    s["OCIO_config"].setValue(1)
    colorspaceReads()

def aces_custom():
    s = nuke.root()
    s["colorManagement"].setValue(1)
    s["OCIO_config"].setValue(3)
    s["customOCIOConfigPath"].setValue("C:/OpenColorIO-Config-ACES-1.2/aces_1.2/config.ocio")
    colorspaceReads()

nuke.menu('Nuke').addCommand('ACES/Aces 1.0.3', 'aces_1_0_3()')
nuke.menu('Nuke').addCommand('ACES/Aces 1.1', 'aces_1_1()')
nuke.menu('Nuke').addCommand('ACES/Aces Custom', 'aces_custom()')