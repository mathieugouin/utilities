#!/bin/bash

# Model
#identify -format '%[EXIF:Model]\n' IMG_2202.JPG

# Date
#identify -format '%[EXIF:DateTime]\n' IMG_2202.JPG

# Auto folder sort

# TBD Adjust here
rel_path=..
# for f in $(ls *.[jJ][pP][gG])
ls *.[jJ][pP][gG] | while read f
do
    echo Procesing image: $f ...
    d=$(identify -format '%[EXIF:DateTime]\n' "$f" | sed 's/:/-/g;s/ .*//')
    if [ -z "$d" ]
    then
        echo Image $f does not contain any date information, skipping.
        continue
    fi
    y=$(echo $d | cut -d '-' -f 1)
    final_dir=$rel_path/$y/$d
    mkdir -p $final_dir
    echo "    moving to $final_dir"
    mv "$f" $final_dir/
done
