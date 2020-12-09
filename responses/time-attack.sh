#!/bin/bash
ts=$(date +%s%N)
# wget 127.0.0.1:9000 --tries=100 -O normal.html
for i in {1..1000}; do wget -q 'http://127.0.0.1:9000/malicious' -O normal.html --delete-after; done;
echo "This command took $((($(date +%s%N) - $ts)/1000000)) milliseconds"
