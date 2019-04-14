for ((i=1;i<=30;i++))
do
echo $i
if [ $i -eq 50 ];
then
break
fi
done


i=50
if [ $i -eq 50 ]
then
echo hahah
fi


累加
j=1
let j+=1
echo $j



list1=`docker ps -q`
echo "${list1}" >> ~/.docker_id.log
for i in `head -n 30 ~/.docker_id.log`
do
echo docker stop $i
done
