#!/bin/bash
list1="chen chen01 chen02"
for ((i=0;i<3;i++));
do
echo "$i  ${list1[$i]}"
done
read -t 10 -p "please input dbname:" dbname
echo "Your name is $dbname"

if [[ $dbname -eq 0 ]];then
source ./db011.sh
elif [[ $dbname -eq 1 ]];then
echo "dbname is $dbname"
elif [[ $dbname -eq 2 ]];then
echo "dbname is $dbname"
else
echo "ok"
fi