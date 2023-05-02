#!/bin/bash

# Using $TOP_LEVEL/DockerfileSite, generates static website files, saving to a specified directory.

# Examples:
# To output to current directory:
# ./generate-site.sh .       .
# 
# To output to top of Git repo:
# ./generate-site.sh

TOP_LEVEL=$(git rev-parse --show-toplevel)

[[ "$#" > 1 ]] && echo "Usage: ./generate-site.sh [output path]" && exit 0
[[ "$#" < 1 ]] && OUT_PATH=$TOP_LEVEL || OUT_PATH=$1

docker build -t app-image:latest -f $TOP_LEVEL/DockerfileSite $TOP_LEVEL
DOCK_CONT=$(docker run -d app-image:latest)
docker cp $DOCK_CONT:/home/app/public $OUT_PATH/static-site-files
docker rm -f $DOCK_CONT
