#!/bin/sh
if [ $# -eq 0 ]; then 
    figlet
else
    figlet "$@"
fi