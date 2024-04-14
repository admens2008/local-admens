echo "Who are you?"
read you

if [ "${you,,}" = gowa ]; then
	echo "CORRECT"
else
	echo "IMPOSTER"
fi
