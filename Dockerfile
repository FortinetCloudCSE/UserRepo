# syntax=docker/dockerfile:1.5-labs

#alpine has shell, busybox does not
#FROM klakegg/hugo:0.107.0-busybox AS hugo
#FROM klakegg/hugo:0.107.0-alpine AS base
FROM hugomods/hugo:std as base
#FROM hugomods/hugo:std-0.127.0 as base
#FROM FROM ghcr.io/gohugoio/hugo:v0.135.0


FROM base as dev
ADD https://github.com/FortinetCloudCSE/CentralRepo.git#prreviewJune23 /home/CentralRepo

WORKDIR /home/CentralRepo

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python

ENTRYPOINT ["/home/CentralRepo/scripts/local_copy.sh"]

FROM base as prod
ADD https://github.com/FortinetCloudCSE/CentralRepo.git#main /home/CentralRepo

WORKDIR /home/CentralRepo

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python

ENTRYPOINT ["/home/CentralRepo/scripts/local_copy.sh"]
