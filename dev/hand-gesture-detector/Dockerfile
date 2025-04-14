FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND=noninteractive

# 1. Dépendances
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gdb \
    git \
    libssl-dev \
    libopencv-dev \
    pkg-config \
    tzdata \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Build Paho MQTT C
WORKDIR /tmp
RUN git clone https://github.com/eclipse/paho.mqtt.c.git && \
    cd paho.mqtt.c && \
    cmake -B build -DPAHO_ENABLE_TESTING=OFF -DPAHO_WITH_SSL=ON . && \
    cmake --build build/ --target install && \
    ldconfig

# 3. Build Paho MQTT C++
RUN git clone https://github.com/eclipse/paho.mqtt.cpp.git && \
    cd paho.mqtt.cpp && \
    cmake -B build -DPAHO_MQTT_C_PATH=/usr/local -DPAHO_BUILD_STATIC=OFF . && \
    cmake --build build/ --target install && \
    ldconfig

# 4. Dossier de travail pour ton projet
WORKDIR /workspace
