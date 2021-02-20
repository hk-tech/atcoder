#!/bin/sh

for dir in a b c d e f;
do
  mkdir $dir
  cp /Users/hiroto/Documents/work/atcoder/utils/template_submit.py $dir/submit.py
done