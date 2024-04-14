#!/bin/bash

prg_name=htop

if command -v $prg_name
then 
	echo "$prg_name is available, lets run it....."
else
	echo "$prg_name not available, lets install it ...."
	sudo apt update && sudo apt install -y $prg_name
fi

$prg_name
