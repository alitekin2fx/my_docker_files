FROM debian:bookworm-slim
ARG USER_NAME=stm32cubemx

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get -y install unzip libc6-i386 openjdk-17-jre libgtk-3-0 libgbm-dev

COPY auto-install.xml /tmp/auto-install.xml
COPY en.stm32cubemx-lin_v6-7-0.zip /tmp/en.stm32cubemx-lin_v6-7-0.zip

WORKDIR /tmp
RUN unzip -q en.stm32cubemx-lin_v6-7-0.zip && \
    ./SetupSTM32CubeMX-6.7.0 auto-install.xml

# cleanup
RUN apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

## Add a user without password
RUN useradd -m $USER_NAME && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $USER_NAME
WORKDIR /home/$USER_NAME

## Sets the default shell
ENV SHELL /bin/bash

