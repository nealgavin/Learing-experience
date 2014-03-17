#!/bin/bash
##just for git push
echo "git add"
var1=`git add -A .` 
var2=`git status`
var3=`git commit`
var4=`git push origin master`
echo "$var1"
echo "git status $var2"
echo "git commit $var3"
var5=`cmd< echo "commit"`
echo "git push $var4"
name="nealgavin"
pass="dream520"
echo "$name"
echo "$pass"
