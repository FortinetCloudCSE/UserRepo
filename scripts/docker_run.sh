#!/bin/bash
# when updating this script, update in BOTH UserRepo(for newly cloned repos) AND CentralRepo(for use in updating existing repos from the Container)

myarray=( "build" "server" "shell" "generate_toml" "update_scripts" "update_fdevsec" )

[[ "$#" > "1" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | generate_toml | update_scripts | update_fdevsec | shell ]" && exit 1

cmd="docker run --rm -it
  -v $(pwd):/home/UserRepo
  --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml
  -p 1313:1313 fortinet-hugo:latest $1"

echo "**** Here's the docker run command we're using:   $cmd ****"
$cmd
