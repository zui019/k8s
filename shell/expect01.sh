#!/usr/bin/expect
set timeout 100
set password "hello"
spawn  ./a.sh
expect "name:"
send "$password\n"
interact
