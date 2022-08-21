#!/bin/bash
ps -eo pid,%cpu --sort=-%cpu > cpudata.txt
touch log.log

#awk '$2 >= 60{print $1}' cpudata.txt
awk '$2 >= 5{print $1}' cpudata.txt > pid.txt


while read -r line
do
    echo $(ps -p $line) >> log.log
    kill $line
done < pid.txt
rm cpudata.txt
rm pid.txt