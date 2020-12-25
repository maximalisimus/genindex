#!/bin/bash
var="${1:-$(</dev/stdin)}"
copy=${var}
len=${#copy}
for((i=$len-1;i>=0;i--)); do reverse="$reverse${copy:$i:1}"; done
echo "$reverse"
