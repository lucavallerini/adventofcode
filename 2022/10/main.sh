#!/bin/bash

file="input"

REGISTER=1
CYCLE=0
SIGNAL_STRENGTH_CYCLES=(20, 60, 100, 140, 180, 220)
SIGNAL_STRENGTH_SUM=0
WIDTH=40
HEIGHT=6

function read_signal_strength() {
    if [[ $( echo ${SIGNAL_STRENGTH_CYCLES[*]} | grep -w "$CYCLE" ) ]]; then
        SIGNAL_STRENGTH_SUM=$(($SIGNAL_STRENGTH_SUM + $REGISTER * $CYCLE))
    fi
}

function update_screen() {
    local COL=$((($CYCLE - 1) % $WIDTH))
    
    if [[ "$COL" == $(($REGISTER - 1)) || "$COL" == $(($REGISTER + 1)) || "$COL" == "$REGISTER" ]]; then
        echo -n "##"
    else
        echo -n "  "
    fi

    if [[ $COL == $(($WIDTH - 1)) ]]; then
        echo
    fi
}

while read -r line; do
    CYCLE=$(($CYCLE + 1))
    update_screen
    read_signal_strength
    if [[ $line != "noop" ]]; then
        CYCLE=$(($CYCLE + 1))
        update_screen
        read_signal_strength
        REGISTER=$(($REGISTER + ${line##*"addx" }))
    fi
done <$file

echo
echo "Sum of signal strength: $SIGNAL_STRENGTH_SUM"
