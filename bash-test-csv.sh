#!/bin/bash
declare -a _csv_array
declare -a str
_csv=$(cat template/icons.csv | tr ',' '|' | xargs)
_csv_array=( $_csv )
unset _csv
for i in ${_csv_array[*]}; do
	if [[ "$i" == *"$1"* ]]; then
		tmp=$(echo "${i}" | tr '|' ' ')
		str=( $tmp )
		echo "${str[0]}.png"
	fi
done
#tmp=$(echo "${_csv_array[0]}" | tr '|' ' ')
#str=( $tmp )
unset tmp
#echo "${str[0]} ${str[3]} ${str[5]}"
_datetime=$(date +"%d-%b-%Y %H:%M")
echo "${_datetime[*]}"
exit 0
