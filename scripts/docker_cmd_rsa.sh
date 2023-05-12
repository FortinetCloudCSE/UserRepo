 docker build -t fortinet-hugo \
   --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" \
   --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" \
   -f DockerfileContentCreation .
 docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public  -p 1313:1313 fortinet-hugo:latest
