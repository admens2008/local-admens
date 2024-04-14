#!/bin/env bash

multiply() {
	mul=$(($1 * $2))
	echo "$1 multiply $2 is: $mul"
}

multiply 10 5
