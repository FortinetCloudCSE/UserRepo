 docker build -t fortinet-hugo \
   --build-arg ssh_prv_key="$(cat ~/.ssh/id_ed25519)" \
   --build-arg ssh_pub_key="$(cat ~/.ssh/id_ed25519.pub)" \
   -f DockerfileContentCreation .
 docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public  -p 1313:1313 fortinet-hugo:latest
