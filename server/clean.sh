#!/bin/bash

folder=archives

latest=`ls $folder -r | head -n1` || -1
name=$((latest + 1))
path=$folder/$name

if [ -z "$(ls images/raw)" ]; then
    echo "It was clean!"
else
    mkdir -p $path/raw

    mv build/output.mp4 $path
    mv build/timelapse.mp4 $path

    mv images/raw/* $path/raw/
    rm -rf images/processed/*

    echo "Cleand!"
fi
