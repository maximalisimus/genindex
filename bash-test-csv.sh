#!/bin/bash
_csv=$(cat template/icons.csv | tr ',' '|' | xargs)
declare -a _csv_array
_csv_array=( $_csv )
unset _csv
declare -a str
tmp=$(echo "${_csv_array[0]}" | tr '|' ' ')
str=( $tmp )
unset tmp
echo "${str[0]} ${str[3]} ${str[5]}"
exit 0
