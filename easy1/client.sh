#!/bin/bash
timestamp=$(date +%d-%b-%H_%M)
filename="default_file"



while true
do
    echo "listening in port 8000"
    touch $filename.txt
    nc -l -p 8000 > "output.txt"
    echo "enter the file name : "
    read filename
    cp output.txt "$filename.txt"
    echo "transfer successful"
    sleep 3
done