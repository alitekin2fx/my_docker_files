#!/bin/bash
docker run -it --rm \
--device /dev/dri \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v $(pwd)/kicad/kicad-scripts:/home/kicad/kicad-scripts \
-v $(pwd)/kicad/kicad-config:/home/kicad/.config/kicad/7.0 \
-v $(pwd)/kicad/kicad-share:/home/kicad/.local/share/kicad/7.0 \
-v $(pwd)/workspace:/home/kicad/workspace \
kicad-devel kicad

