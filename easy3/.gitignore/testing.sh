#!/bin/bash
ps -eo pid,%cpu --sort=-%cpu > cpudata.txt


echo "hey"
awk '$2 >= 60{print $1}' cpudata.txt
awk '$2 >= 60{print $1}' cpudata.txt > pid.txt

while read -r line
do
   echo "kill $line"
done < pid.txt