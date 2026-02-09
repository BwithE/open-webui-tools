FROM ghcr.io/open-webui/open-webui:main

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    python3 python3-pip python3-venv \
    iputils-ping \
    netcat-openbsd \
    nmap \
    curl \
    wget \
    traceroute \
    iproute2 \
    tcpdump \
    aircrack-ng \
    dnsutils \
    procps \
    tshark \
    ssh \
    ftp \
    telnet \
    sudo \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*
