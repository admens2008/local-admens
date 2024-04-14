#!/bin/env bash

#######################################
# Author: Nana Yaw	
# Date: 8th April, 2024
# This script outputs the node health
#
# version: v1
#######################################

set -x # debug mode
set -e # exit the script when there's an error
set -o pipefail
df -h

free -g

nproc

ps -ef | grep ssh | awk -F" " '{print $2}'
