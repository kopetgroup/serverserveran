#!/bin/sh
while :
do

	FILE=/var/www/html/TheBots/bots/kopet
	if [ -f $FILE ]; then
	   echo "File $FILE exists."
	else
	   echo "File $FILE does not exist."
		 exit
	fi

	sleep 1
done
