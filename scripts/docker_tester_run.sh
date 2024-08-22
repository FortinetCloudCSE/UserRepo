#!/bin/bash
# when updating this script, update in BOTH UserRepo(for newly cloned repos) AND CentralRepo(for use in updating existing repos from the Container)

myarray=( "build" "server" "shell" "generate_toml" "update_scripts" "update_fdevsec" )

[[ "$#" > "1" ]] || [[ ! " ${myarray[*]} " =~ " $1 " ]] && echo "Usage: ./scripts/docker_run.sh [ build | server | generate_toml | update_scripts | update_fdevsec | shell ]" && exit 1

case "$1" in
  "server" | "shell" | "build" )
    cmd="docker run --rm -it
      -v $(pwd):/home/UserRepo
      --mount type=bind,source=$(pwd)/hugo.toml,target=/home/CentralRepo/hugo.toml
      -p 1313:1313 hugotester:latest $1"
    ;;

  "generate_toml" | "update_scripts" | "update_fdevsec")
    cmd="docker run --rm -it
    -v $(pwd):/home/UserRepo
    hugotester:latest $1"
    ;;

  *)
    cmd=""
    ;;
esac

echo "**** Here's the docker run command we're using:   $cmd ****"
$cmd
