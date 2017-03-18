#!/bin/sh

NOW=$(date +"%d-%m-%Y-%H-%m")
PYFILE="/home/folder/logs/handleMouseEvent.py"
LOGFILE="/home/folder/logs/log_$NOW.txt"

python3 $PYFILE > $LOGFILE
