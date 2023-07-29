FROM debian:bookworm-slim
ARG USER_NAME=stm32cubeide

# Enable udev for detection of dynamically plugged devices
ENV UDEV=on

ENV DEBIAN_FRONTEND=noninteractive
ENV LICENSE_ALREADY_ACCEPTED=1

RUN apt-get update && \
    apt-get -y install unzip openjdk-17-jre libswt-gtk-4-java \
    libgtk-3-0 libgbm-dev libusb-1.0-0 libncurses5 udev

COPY en.st-stm32cubeide_1.12.0_14980_20230301_1550_amd64.sh.zip /tmp/stm32cubeide-installer.sh.zip

## Unzip STM32 Cube IDE and delete zip file
WORKDIR /tmp
RUN unzip -p stm32cubeide-installer.sh.zip > stm32cubeide-installer.sh && \
    rm stm32cubeide-installer.sh.zip

## Extract STM32 Cube IDE and delete installer
WORKDIR /tmp
RUN mkdir -p stm32cubeide-installer && \
    sh stm32cubeide-installer.sh --quiet --noexec --target stm32cubeide-installer && \
    rm stm32cubeide-installer.sh

## Installing STM32CubeIDE
WORKDIR /tmp/stm32cubeide-installer
RUN mkdir -p /opt/st/stm32cubeide && \
    tar zxf st-stm32cubeide*.tar.gz -C /opt/st/stm32cubeide && \
    sh ./st-stlink-server*.sh --quiet -- -f && \
    sh ./st-stlink-udev-rules-*-linux-noarch.sh --quiet && \
    sh ./segger-jlink-udev-rules-*-linux-noarch.sh --quiet

## cleanup
RUN apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

## Add a user without password
RUN useradd -m $USER_NAME && \
    echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USER_NAME
WORKDIR /home/$USER_NAME

## Sets the default shell
ENV SHELL /bin/bash

