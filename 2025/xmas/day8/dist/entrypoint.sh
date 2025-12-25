#!/bin/bash

LISTEN_PORT=1337
CHALLENGE_PATH="/challenge/jail.sh"

while :
do
    exec socat TCP-LISTEN:${LISTEN_PORT},reuseaddr,fork EXEC:"$CHALLENGE_PATH,stderr";
done
