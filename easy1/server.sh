#!/bin/bash
filename="default_file"


while true
do
    echo "enter the name of the file you want to send : "
    read filename
    timestamp=$(date +%d-%b_%H-%M)
    echo "ip address and port number of client"
    read ip_address port_number
    nc -N $ip_address $port_number < "$filename.txt"
    echo "$filename $timestamp" >> log.log
    echo "transfer successful"
    sleep 3
done