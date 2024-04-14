#!/bin/bash

command=/usr/bin/htop

if [ -f $command ]
then
	echo "Command is available, lets run it..."
else
	echo "Command is not available, installing it...."
	sudo apt update && sudo apt install -y htop
fi

$command
