#!/bin/env bash

sub() {
	sub=$(($1 - $2))
	return $sub
}

sub 10 6
result=$?  # Capture the return value of the function
echo $result
