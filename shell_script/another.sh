#!/bin/env bash

echo Who are you?
read you
if [ "${you,,}" = franca ]; then
	echo CORRECT! $you, you are welcome!
elif [ "${you,,}" = help ]; then
	echo Pls enter your name to gain access
else
	echo INCORRECT! Not Eligible! Goodbye
fi
