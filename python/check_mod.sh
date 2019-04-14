#/bin/bash
lsmod |awk '{print $1}'|sort  >> ./`date +%Y%m%d`_iuap_mod_check.log
mod_log=./mod.log
file1=./`date +%Y%m%d`_iuap_mod_check.log
for line1 in $(cat $mod_log )
	do
		grep $line1 $file1 > /dev/null
			if [$? -eq 0];then
				echo $?
			fi
	done
rm -rf $file1

