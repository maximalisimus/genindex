#!/bin/bash
_lng=("a" "b" "c" "d" "e" "f" "g" "h" "i" "g" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z")
function genname()
{
	_res=""
	count=$((1 + RANDOM % 25 +0))
	_res="${_res}${_lng[${count}]}"
	unset count
	count=$((1 + RANDOM % 9 +0))
	_res="${_res}${count}"
	unset count
	count=$((1 + RANDOM % 25 +0))
	_res="${_res}${_lng[${count}]}"
	unset count
	count=$((1 + RANDOM % 9 +0))
	_res="${_res}${count}"
	unset count
	count=$((1 + RANDOM % 25 +0))
	_res="${_res}${_lng[${count}]}"
	unset count
	echo ${_res}
}
_name=""
_tmp=""
while [[ "${_tmp[*]}" != "0" ]]; do
	_name=$( genname )
	_tmp=$(find ./image/ -type f -iname "*${_name}*" | wc -l)
done
echo "${_name}"
exit 0
