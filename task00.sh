#!/bin/bash

source /etc/lsb-release
echo "os version: $DISTRIB_DESCRIPTION"

echo "users with bash"
cat /etc/passwd | grep "/bash$" | cut -d: -f1

echo "Ports open"
sudo netstat -tuln

