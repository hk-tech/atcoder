#!/bin/sh

dirs=`find ./* -maxdepth 0 -type d`

for dir in $dirs;
do
  echo $dir
  cp /Users/hiroto/Documents/work/atcoder/utils/template_submit.py $dir/submit.py
done
