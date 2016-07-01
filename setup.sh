#!/bin/bash

rm -rf env
virtualenv --python python3.5 env
source env/bin/activate
pip3.5 install -r requirements.txt
pip3.5 install git+https://github.com/Rapptz/discord.py@async
