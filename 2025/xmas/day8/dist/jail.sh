#!/bin/bash

PATH=$(/usr/bin/getconf PATH || /bin/kill $$)

#######################################################
#              |>>>                    |>>>          #
#              |                       |             #
#          _  _|_  _               _  _|_  _         #
#         |;|_|;|_|;|             |;|_|;|_|;|        #
#         \\..      /             \\..      /        #
#          \\..    /               \\..    /         #
#           \\..  /                 \\..  /          #
#            ||||                     ||||           #
#            ||||                     ||||           #
#   ______________________________________________   #
#  /______________________________________________/| #
# |                                              | | #
# |      |   |   |   |   |   |   |   |   |       | | #
# |      |___|___|___|___|___|___|___|___|       | | #
# |                                              | | #
# |              "Help me please..."             | | #
# |______________________________________________|/  #
#######################################################

function check_input() {
    if [[ $1 =~ '..' || $1 =~ './' || $1 =~ [[:space:]]'/' ]]
    then
        return 0
    fi
    if [[ $1 =~ [[:alnum:][:space:]] ]];
    then
        return 0
    fi
    if [[ $1 =~ '<' || $1 =~ '>' ]];
    then
        return 0
    fi

    return 1
}

# Todo remove this shit... it can be retrieved by the player ?! >_<
flag=`cat "/flag.txt"`

while :
do
    input=""
    echo -n "Enter the input: "
    read input
    if check_input "$input"
        then
                echo -e '\033[0;31mRestricted characters has been used\033[0m'
        else
                output=`env -i PATH=$HOME/bin/ /bin/bash --noprofile --norc --restricted -c "$input" < /dev/null`
                echo "Command executed"
        fi
done
