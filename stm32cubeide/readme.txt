Before starting to build the docker image, download en.st-stm32cubeide_1.12.0_14980_20230301_1550_amd64.sh.zip from https://www.st.com/en/development-tools/stm32cubeide.html
# Firmware upgrade
java -jar /opt/st/stm32cubeide/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.500.202301161003/tools/bin/STLinkUpgrade.jar
# To solve "libusb requires write access to USB device nodes" error: copy USB rules to your host machine just like below
https://www.codementor.io/@hbendali/getting-started-with-stm8-development-tools-on-gnu-linux-zu59yo35x

RUN apt-get update && apt install sudo

#RUN /lib/systemd/systemd-udevd --daemon
#RUN udevadm control --reload-rules
#RUN udevadm trigger

