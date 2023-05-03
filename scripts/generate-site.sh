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
[[ "$#" < 1 ]] && OUT_PATH=$TOP_LEVEL || OUT_PATH=$(pwd)

docker build -t app-image:latest --build-arg ssh_prv_key="$(cat ~/.ssh/id_ed25519)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_ed25519.pub)" -f DockerfileBuild .
DOCK_CONT=$(docker run -d app-image:latest)
docker cp $DOCK_CONT:/home/CentralRepoTest/public $OUT_PATH
docker rm -f $DOCK_CONT
