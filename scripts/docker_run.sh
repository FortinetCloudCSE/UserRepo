#!/bin/bash

myarray=( "build" "server" "shell" "" )

[[ "$#" > "1" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | shell ]" && exit 1

cmd="docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public -v $(pwd)/layouts:/home/UserRepo/layouts -p 1313:1313 fortinet-hugo:latest $1"
echo $cmd
$cmd
