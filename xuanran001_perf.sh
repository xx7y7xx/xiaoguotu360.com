#!/bin/bash

WWW="/var/www/html/__xuanran001__"
LOG="$WWW/xuanran001_perf.log"
GP="$WWW/xuanran001_perf.gp"

now="`date +"%Y-%m-%d %T"`"

if [ ! -f $LOG ]; then
  echo "Time,time namelookup,time connect,time appconnect,time pretransfer,time redirect,time starttransfer,time total" > $LOG
fi

echo -n "$now," >> $LOG
echo `/usr/bin/curl --max-time 30 -w "@$WWW/curl-format.txt" -o /dev/null -s "http://www.xuanran001.com/index.html"` >> $LOG

gnuplot $GP
