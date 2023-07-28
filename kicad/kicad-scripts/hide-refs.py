#!/usr/bin/env python
#https://github.com/KiCad/kicad-doc/blob/master/src/pcbnew/pcbnew_python_scripting.adoc
#execfile("/media/ali-teke/KiCadSources/kicad-scripts/hide-refs.py")

from pcbnew import *
pcb = GetBoard()
for module in pcb.GetModules():
    print "* Module: %s"%module.GetReference()
    module.Value().SetVisible(False)		# set Value as Hidden
    module.Reference().SetVisible(False)	# set Reference as Hidden
print('Done.')

