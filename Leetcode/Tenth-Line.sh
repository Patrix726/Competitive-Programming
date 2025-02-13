#!/bin/bash
filename="file.txt"
# lines=wc $filename
if [ -f $filename ]; then
    awk 'NR == 10 {print $0}' $filename
fi