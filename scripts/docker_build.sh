#!/bin/bash

envarray=( "prod" "dev")

[[ "$#" > "1" ]] || [[ ! " ${envarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_build.sh [ prod | dev ]" && exit 1

case "$1" in
  "prod" )
    container_name="fortinet-hugo"
    ;;

  "dev" )
    container_name="hugotester"
    ;;
  *)
    cmd=""
    ;;
esac

docker build -t $container_name . --target=$1

echo "**** Built a $1 container named: $container_name ****"