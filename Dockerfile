# syntax=docker/dockerfile:1.5-labs

FROM klakegg/hugo:0.107.0-alpine AS hugo

ADD https://github.com/FortinetCloudCSE/CentralRepo.git#main /home/CentralRepo

WORKDIR /home/CentralRepo