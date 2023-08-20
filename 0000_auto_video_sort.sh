#!/bin/bash

# Date
#ffmpeg -i $f -dump 2>&1 | grep creation_time | head -n 1

# Auto folder sort

# TBD Adjust here
rel_path=../001-Vidéos_triés
find . -type f \( -iname "*.mp4" -o -iname "*.avi" \) | while read f
do
    echo Procesing video: $f ...
    d=$(ffmpeg -i $f -dump 2>&1  | grep creation_time | head -n 1 | grep -Po '\d\d\d\d-\d\d-\d\d')
    if [ -z "$d" ]
    then
        echo Video $f does not contain any date information, skipping.
        continue
    fi
    y=$(echo $d | cut -d '-' -f 1)
    final_dir="$rel_path/$y/$d"
    mkdir -p $final_dir
    # verbose, do not overwrite an existing file
    \mv -vn "$f" $final_dir/
done
