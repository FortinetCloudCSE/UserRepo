 docker run --rm -it -v $(pwd)/content/:/home/CentralRepo/content -v $(pwd)/config.toml:/home/CentralRepo/config.toml -v $(pwd)/docs:/home/CentralRepo/public -v $(pwd)/layouts:/home/UserRepo/layouts -p 1313:1313 fortinet-hugo:latest shell