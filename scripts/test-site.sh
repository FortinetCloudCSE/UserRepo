#!/bin/bash

# Using $TOP_LEVEL/DockerfileSite, generates static website files, saving to a specified directory.

# Examples:
# To output to current directory:
# ./generate-site.sh ~/.ssh/id_rsa ~/.ssh/id_rsa.pub.       .
# 
# To output to top of Git repo:
# ./generate-site.sh ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub

[[ "$#" > 3 ]] || [[ "$#" < 2 ]] && echo "Usage: ./generate-site.sh <path to private ssh key> <path to public ssh key> [output path]" && exit 0

PRIV_KEY=$1
PUB_KEY=$2
OUT_DIR=$3

TOP_LEVEL=$(git rev-parse --show-toplevel)

[[ "$#" == 2 ]] && OUT_PATH=$TOP_LEVEL || OUT_PATH=$OUT_DIR

docker build -t testcontainer:latest --build-arg ssh_prv_key="$(cat $PRIV_KEY)" --build-arg ssh_pub_key="$(cat $PUB_KEY)" -f DockerfileTest .
DOCK_CONT=$(docker run -d -p 1313:1313 testcontainer:latest)
docker cp $DOCK_CONT:/home/CentralRepo/public $OUT_PATH
docker rm -f $DOCK_CONT
