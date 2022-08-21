timestamp=$(date +%d-%b-%H_%M)
filename="default_file"



while true
do
    echo "listening in port 8000"
    nc -l -p 8000 > 'output.txt'
    timestamp=$(date +%d-%b-%H_%M)
    echo "enter the file name you want to store the recieved data as"
    read filename
    cp output.txt "$filename".txt
    echo "$filename $timestamp" > log.log
done