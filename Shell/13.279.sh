#!/bin/bash
#option

while [ -n "$1" ]
do
	case "$1" in
	a) echo find a ---  ;;
	b) echo find b ---- ;;
	6) echo fine 6 ----- ;;
	--) shift 
		break ;;
	*) echo "$1 is not option";;
	esac
	shift
done
