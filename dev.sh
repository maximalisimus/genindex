#!/bin/bash
#
ABSOLUT_FILENAME=$(readlink -e "$0")
filesdir=$(dirname "$ABSOLUT_FILENAME")
#
temp_dir=$(mktemp 2>/dev/null) || temp_dir=${filesdir}/tmpdir$$
temp_files=$(mktemp 2>/dev/null) || temp_files=${filesdir}/tmpfile$$
function show_dir()
{
	find "$1" -maxdepth 1 -type d | rev | cut -d '/' -f1 | rev | awk '!/^$/{print $0}' | sort > ${temp_dir}
}
function show_file()
{
	find "$1" -maxdepth 1 -type f | rev | cut -d '/' -f1 | rev | awk '!/^$/{print $0}' | sort > ${temp_files}
}
function return_ext()
{
	_ext=$(echo "$1" | rev | cut -d '.' -f1 | rev)
	echo "${_ext[*]}"
}
show_dir "/home/mikl/003/"
cat ${temp_dir}
show_file "/home/mikl/003/"
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
