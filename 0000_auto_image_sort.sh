#!/bin/bash

# Model
#identify -format '%[EXIF:Model]\n' IMG_2202.JPG

# Date
#identify -format '%[EXIF:DateTime]\n' IMG_2202.JPG

# Auto folder sort

# TBD Adjust here
rel_path=../001-Photos_triées
find . -type f \( -iname "*.jpg" -o -iname "*.png" \) | while read f
do
    echo Procesing image: $f ...
    d=$(magick identify -format '%[EXIF:DateTime]\n' "$f" | sed 's/:/-/g;s/ .*//')
    if [ -z "$d" ]
    then
        echo Image $f does not contain any date information, skipping.
        continue
    fi
    y=$(echo $d | cut -d '-' -f 1)
    final_dir="$rel_path/$y/$d"
    mkdir -p $final_dir
    # verbose, do not overwrite an existing file
    \mv -vn "$f" $final_dir/
done
