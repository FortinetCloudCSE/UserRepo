#!/bin/bash

myarray=( "build" "server" "shell" "generate_toml" "update_scripts" "update_fdevsec" " )

[[ "$#" > "1" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | generate_toml | update_scripts | update_fdevsec | shell ]" && exit 1

cmd="docker run --rm -it
  -v $(pwd)/content:/home/CentralRepo/content
  -v $(pwd)scripts:/home/UserRepo/scripts
  -v $(pwd)/layouts:/home/UserRepo/layouts
  --mount type=bind,source=$(pwd)/Dockerfile,target=/home/UserRepo/DockerFile
  --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml
  -p 1313:1313 fortinet-hugo:latest $1"
echo $cmd
$cmd
