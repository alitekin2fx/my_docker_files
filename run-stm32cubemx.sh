#!/bin/bash
docker run -it --rm \
--device /dev/dri \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v $(pwd)/workspace:/home/stm32cubemx/workspace \
-v $(pwd)/stm32cubemx/STM32Cube:/home/stm32cubemx/STM32Cube \
-v $(pwd)/stm32cubemx/.stm32cubemx:/home/stm32cubemx/.stm32cubemx \
stm32cubemx /local/usr/STMicroelectronics/STM32Cube/STM32CubeMX/STM32CubeMX

