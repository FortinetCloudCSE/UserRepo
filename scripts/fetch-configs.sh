#!/bin/bash

root_level=$(git rev-parse --show-toplevel)
while read -r line; do
  [[ ${line:0:1} =~ \# ]] || [[ -z "$line" ]] && continue
  line=($line)
  file_resource=${line[0]}
  if (( ${#line[@]} < 2 )); then path_location=$root_level; else path_location=$root_level/${line[1]}; fi
  [[ -d $path_location ]] | mkdir -p $path_location
  wget $file_resource -P $path_location 
done < $root_level/.config_files
