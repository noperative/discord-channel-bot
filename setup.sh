#!/bin/bash

rm -rf env
virtualenv --python python3 env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install git+https://github.com/Rapptz/discord.py@async
