#!/bin/bash

package=top

sudo apt install -y $package >> package_install_results.log

if [ $? -eq 0 ]
then
	echo "Package successful"
	echo "$package can be found here:"
	which $package
else	
	echo "$package failed to install" >> package_install_failure.log
fi
