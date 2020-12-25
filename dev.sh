#!/bin/bash
#
ABSOLUT_FILENAME=$(readlink -e "$0")
filesdir=$(dirname "$ABSOLUT_FILENAME")
#
temp_dir=$(mktemp 2>/dev/null) || temp_dir=${filesdir}/tmpdir$$
temp_files=$(mktemp 2>/dev/null) || temp_files=${filesdir}/tmpfile$$
function show_dir()
{
	if [[ -z "$2" ]]; then
		find "$1" -maxdepth 1 -type d | ./modules/reverse.sh | cut -d '/' -f1 | ./modules/reverse.sh | awk '!/^$/{print $0}' | sort > ${temp_dir}
	else
		find "$1" -maxdepth 1 -type d | ./modules/reverse.sh | cut -d '/' -f1 | ./modules/reverse.sh | awk '!/^$/{print $0}' | grep -Ev "*${2}*" | sort > ${temp_dir}
	fi
}
function show_file()
{
	if [[ -z "$2" ]]; then
		find "$1" -maxdepth 1 -type f | ./modules/reverse.sh | cut -d '/' -f1 | ./modules/reverse.sh | awk '!/^$/{print $0}' | sort > ${temp_files}
	else
		find "$1" -maxdepth 1 -type f | ./modules/reverse.sh | cut -d '/' -f1 | ./modules/reverse.sh | awk '!/^$/{print $0}' | grep -Ev "*${2}*" | sort > ${temp_files}
	fi
}
function return_ext()
{
	_ext=$(echo "$1" | rev | cut -d '.' -f1 | rev)
	echo "${_ext[*]}"
}
show_dir "/home/mikl/003/" "html"
cat ${temp_dir}
echo ""
show_file "/home/mikl/003/"
cat ${temp_files}
echo ""
show_file "/home/mikl/003/" ".html"
echo ""
cat ${temp_files}
echo ""
while read line; do
	my_ext=$(return_ext "$line")
	echo "${my_ext}"
done < ${temp_files}
rm -rf "${temp_dir}"
rm -rf "${temp_files}"
exit 0
