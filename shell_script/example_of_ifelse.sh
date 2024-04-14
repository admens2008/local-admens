echo "Enter your username: "
read username

if [ "${username,,}" = admens ]; then
	echo "You're in boss"
else
	echo "wrong username"
fi
