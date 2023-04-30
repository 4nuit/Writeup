#!/bin/bash

PATH=$(getconf PATH)

if [[ "$1" == *","* ]] || [[ "$1" == *"_"*  ]] || [[ "$1" == *"~"* ]]; then
        echo "CAPS ONLY >:("
        exit

fi

eval "${1^^}"
