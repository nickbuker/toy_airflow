#!/bin/bash

# Setup script to Ubuntu 18.04 EC2 instance

# get updates
apt update && updgrade -y

# # get pre-requisites
# sudo apt install build-essential zlib1g-dev libncurses5-dev \
#     libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

# # install Python 3.6
# sudo apt install python3.6

# update pip
pip3 install --upgrade pip3

# install python packages
pip3 install -r requirements.txt
