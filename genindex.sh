#!/bin/bash
ABSOLUT_FILENAME=$(readlink -e "$0")
filesdir=$(dirname "$ABSOLUT_FILENAME")
### Load Config ##
_sh_files=$(find "$filesdir/config" -maxdepth 1 -type f -iname "*.sh" | xargs)
_files=( $_sh_files )
unset _sh_files
for i in ${_files[*]}; do
	source $i
done
### load language ###
source "${filesdir}/config/configured.txt"
source "${filesdir}/config/lang/${_language}"
### Load Modules ###
_sh_files=$(find "$filesdir/modules" -maxdepth 1 -type f -iname "*.sh" | xargs)
_files=( $_sh_files )
unset _sh_files
for i in ${_files[*]}; do
	source $i
done
### End source ###
while [ -n "$1" ]; do
	case "$1" in
		-font) if [[ -n "$2" ]]; then
					echo "$2"
					shift
				else
					echo "Please enter the parameters two"
				fi
			;;
		-bgcolor) if [[ -n "$2" ]]; then
					echo "$2"
					shift
				else
					echo "Please enter the parameters two"
				fi
			;;
		-exclude) if [[ -n "$2" ]]; then
					echo "$2"
					shift
				else
					echo "Please enter the parameters two"
				fi
			;;
		-h* | --h*) _help ;;
		*) _unknown ;;
	esac
	shift
done
exit 0
