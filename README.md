# spider-onsite-1


# Instructions to run the tasks

easy1
- run client.sh on client machine
- run server.sh on client machine
- give the filename in server

easy2
- run the below command on main.sh
$sudo crontab -e
and then put "00 18 * * * ./main.sh"

or
run script.sh
(this method uses "at" command and not crontab)


easy3
- run main.sh by
$bash ./main.sh


medium2
- enter the virtual env and then run the python server
$source venv/bin/activate
$python3 main.py
