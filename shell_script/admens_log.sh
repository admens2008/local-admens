#!/bin/env bash

case ${1,,} in 
	admens | bogga)
		echo "You are in"
		;;
	help)
		echo "Type ur username"
		;;
	*)
		echo "Incorrect!. Goodbye"
esac
