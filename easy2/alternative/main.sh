#!/bin/bash
ps -eo pid,%mem --sort=-%mem > cpudata.txt
touch log.log

#awk '$2 >= 60{print $1}' cpudata.txt
awk '$2 >= 0{print $1}' cpudata.txt > pid.txt


while read -r line
do
    echo $(ps -p $line -eo CMD,PID,%cpu) $(date +%d-%b_%H-%M) >> log.log
done < pid.txt
rm cpudata.txt
rm pid.txt
bash ./main.sh | at 6pm