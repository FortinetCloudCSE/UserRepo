#!/bin/bash

myarray=( "build" "server" "shell" "" )

[[ "$#" > "1" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | shell ]" && exit 1

cmd="docker run --rm -it 
  -v $(pwd)/content:/home/CentralRepo/content 
  -v $(pwd)/docs:/home/CentralRepo/public 
  --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml
  -p 1313:1313 fortinet-hugo:latest $1"
echo $cmd
$cmd
