#!/bin/bash
ts=$(date +%s%N)
wget 172.17.0.4 -O some.html --delete-after
echo "This command took $((($(date +%s%N) - $ts)/1000000)) milliseconds"
