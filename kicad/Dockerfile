FROM debian:bookworm AS build

# install build dependencies 
RUN apt-get update && \
    apt-get install -y build-essential cmake libbz2-dev libcairo2-dev libglu1-mesa-dev \
    libgl1-mesa-dev libglew-dev libx11-dev libwxgtk3.2-dev \
    mesa-common-dev pkg-config python3-dev python3-wxgtk4.0 \
    libboost-all-dev libglm-dev libcurl4-openssl-dev \
    libgtk-3-dev \
    libngspice0-dev \
    ngspice-dev \
    libocct-modeling-algorithms-dev \
    libocct-modeling-data-dev \
    libocct-data-exchange-dev \
    libocct-visualization-dev \
    libocct-foundation-dev \
    libocct-ocaf-dev \
    unixodbc-dev \
    zlib1g-dev \
    shared-mime-info \
    git \
    gettext \
    ninja-build \
    swig4.0

WORKDIR /src

RUN set -ex; \
    git clone https://gitlab.com/kicad/code/kicad.git --branch=7.0 --depth=1; \
    git clone https://gitlab.com/kicad/libraries/kicad-symbols.git --depth=1; \
    git clone https://gitlab.com/kicad/libraries/kicad-footprints.git --depth=1; \
    git clone https://gitlab.com/kicad/libraries/kicad-templates.git --depth=1;
    
WORKDIR /src/kicad

# We want the built install prefix in /usr to match normal system installed software
# However to aid in docker copying only our files, we redirect the prefix in the cmake install
RUN set -ex; \
    mkdir -p build/linux; \
    cd build/linux; \
    cmake \
      -G Ninja \
      -DCMAKE_BUILD_TYPE=Release \
      -DKICAD_SCRIPTING_WXPYTHON=ON \
      -DKICAD_USE_OCC=ON \
      -DKICAD_SPICE=ON \
      -DKICAD_BUILD_I18N=ON \
      -DCMAKE_INSTALL_PREFIX=/usr \
      ../../; \
    ninja; \
    cmake --install . --prefix=/usr/local/

RUN set -ex; \
    cd /src/kicad-symbols; \
    cmake \
      -G Ninja \
      -DCMAKE_RULE_MESSAGES=OFF \
      -DCMAKE_VERBOSE_MAKEFILE=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      . \
    ninja; \
    cmake --install . --prefix=/usr/local/

RUN set -ex; \
    cd /src/kicad-footprints; \
    cmake \
      -G Ninja \
      -DCMAKE_RULE_MESSAGES=OFF \
      -DCMAKE_VERBOSE_MAKEFILE=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      . \
    ninja; \
    cmake --install . --prefix=/usr/local/

RUN set -ex; \
    cd /src/kicad-templates; \
    cmake \
      -G Ninja \
      -DCMAKE_RULE_MESSAGES=OFF \
      -DCMAKE_VERBOSE_MAKEFILE=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      . \
    ninja; \
    cmake --install . --prefix=/usr/local/
    
FROM debian:bookworm-slim AS runtime
ARG USER_NAME=kicad

# install runtime dependencies 
RUN apt-get update && \
    apt-get install -y libbz2-1.0 \
    libcairo2 \
    libglu1-mesa \
    libglew2.2 \ 
    libx11-6 \
    libwxgtk3.2* \
    libpython3.11 \
    python3 \ 
    python3-pip \
    python3-wxgtk4.0 \
    libcurl4 \
    libngspice0 \
    ngspice \
    libocct-modeling-algorithms-7.6 \
    libocct-modeling-data-7.6 \
    libocct-data-exchange-7.6 \
    libocct-visualization-7.6 \
    libocct-foundation-7.6 \
    libocct-ocaf-7.6 \
    unixodbc \
    zlib1g \
    shared-mime-info \
    sudo

COPY --from=build /usr/local/bin /usr/bin
COPY --from=build /usr/local/share /usr/share
COPY --from=build /usr/local/lib /usr/lib
COPY --from=build /usr/share/kicad /usr/share/kicad

# fix the linkage to libkicad_3dsg
RUN ldconfig -l /usr/bin/_pcbnew.kiface

# install kikit
RUN pip3 install kikit --break-system-packages

# cleanup
RUN apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

## Add a user without password
RUN useradd -m $USER_NAME && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $USER_NAME
WORKDIR /home/$USER_NAME

## Sets the default shell
ENV SHELL /bin/bash

