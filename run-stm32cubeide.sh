#!/bin/bash
docker run -it --rm -d --privileged \
--device /dev/dri \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v /dev/bus/usb/:/dev/bus/usb \
-v $(pwd)/workspace:/home/stm32cubeide/workspace \
-v $(pwd)/stm32cubeide/.eclipse:/home/stm32cubeide/.eclipse \
-v $(pwd)/stm32cubeide/STM32Cube:/home/stm32cubeide/STM32Cube \
-v $(pwd)/stm32cubeide/STM32CubeIDE:/home/stm32cubeide/STM32CubeIDE \
-v $(pwd)/stm32cubeide/.stm32cubemx:/home/stm32cubeide/.stm32cubemx \
stm32cubeide /opt/st/stm32cubeide/stm32cubeide

