#!/bin/bash
tempfile=`mktemp -t tmp.XXXXXX`
exec 5> $tempfile

echo "This is test for file " >&5
echo "welcome !">&5
exec 5>-
echo "file name: $tempfile" >&1
cat $tempfile
ls

