FROM ubuntu:latest

ENV PYTHONUNBUFFERED definitely
# Set bash as default shell, non-interactive
ENV DEBIAN_FRONTEND noninteractive\
    SHELL=/bin/bash
RUN mkdir -p /root/.huggingface/
# Build with some basic utilities
RUN apt update && apt-get update && apt-get install -y \
    openssh-server \
    python3.10-venv \
    pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen

COPY requirements.txt /workspace/requirements.txt
COPY server /workspace/server

WORKDIR /workspace
RUN python3 -m venv venv
ENV PATH="venv/venv/bin:$PATH"
RUN pip install -r requirements.txt

WORKDIR /workspace/server

RUN pip cache purge
ADD docker_start.sh /start.sh
RUN chmod a+x /start.sh

CMD [ "/start.sh" ]