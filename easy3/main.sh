#!/bin/bash
ps -eo pid,%cpu --sort=-%cpu > cpudata.txt
touch log.log

#awk '$2 >= 60{print $1}' cpudata.txt
awk '$2 >= 10{print $1}' cpudata.txt > pid.txt


while read -r line
do
    echo $(ps -p $line) > temp.txt
    tail -n +2 input.txt >> log.log
    kill $line
done < pid.txt
rm cpudata.txt
rm pid.txt