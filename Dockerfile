# set base image (host OS)
FROM nvidia/cuda:11.0-base-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive 

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
# RUN mkdir /app
# WORKDIR /app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /usr/src/app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# All users can use /home/user as their home directory
ENV HOME=/home/user
RUN chmod 777 /home/user

# Install Miniconda and Python 3.8
ENV CONDA_AUTO_UPDATE_CONDA=false
ENV PATH=/home/user/miniconda/bin:$PATH
RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh \
 && conda install -y python==3.8.3 \
 && conda clean -ya \
 && conda update -n base -c defaults conda

# CUDA 11.0-specific steps
RUN conda install -y -c pytorch \
    cudatoolkit=11.0.221 \
    "pytorch=1.7.1=py3.8_cuda11.0.221_cudnn8.0.5_0" \
    "torchvision=0.8.2=py38_cu110" \
 && conda clean -ya

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/

# install dependencies
RUN pip3 install -r requirements.docker.txt
RUN pip3 install -e .

# copy the content of the local src directory to the working directory
COPY plant_disease_classification_api/ .
