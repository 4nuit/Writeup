#!/bin/bash

if [[ "$1" == *","* ]]; then
        echo "CAPS ONLY >:("
        exit

fi

eval "${1^^}"
