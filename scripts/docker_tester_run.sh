#!/bin/bash

myarray=( "build" "server" "shell" "generate_toml" "update_scripts" "update_fdevsec" )

envarray=( "prod" "dev")

[[ "$#" > "2" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] || [[ ! " ${envarray[*]} " =~ " $2 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | generate_toml | update_scripts | update_fdevsec | shell ] [ prod | dev ]" && exit 1


case "$2" in
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

case "$1" in
  "server" | "shell" | "build" )
    cmd="docker run --rm -it
      -v $(pwd):/home/UserRepo
      --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml
      -p 1313:1313 $container_name:latest $1"
    ;;

  "generate_toml" | "update_scripts" | "update_fdevsec")
    cmd="docker run --rm -it
    -v $(pwd):/home/UserRepo
    $container_name:latest $1"
    ;;

  *)
    cmd=""
    ;;
esac

echo "************ Here's the docker run command we're using:  "
echo "$cmd"
echo "************"
$cmd
