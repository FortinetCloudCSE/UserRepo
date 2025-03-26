# syntax=docker/dockerfile:1.5-labs

# Base Hugo image (uses Alpine 3.21)
FROM hugomods/hugo:std as base

############################
# DEV STAGE
############################
FROM base as dev

# Add repo
ADD https://github.com/FortinetCloudCSE/CentralRepo.git#prreviewJune23 /home/CentralRepo
WORKDIR /home/CentralRepo

# Force install CA certs from HTTP and configure apk to use HTTP; due to sudden issues with HTTPS; temporary fix until it's working again
RUN apk --no-cache --allow-untrusted --repository http://dl-cdn.alpinelinux.org/alpine/v3.21/main \
    add ca-certificates && \
    update-ca-certificates && \
    sed -i 's|https://dl-cdn.alpinelinux.org|http://dl-cdn.alpinelinux.org|g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache python3 py3-pip tini-static && \
    ln -sf python3 /usr/bin/python && \
    ln -sf /sbin/tini-static /sbin/tini

ENTRYPOINT ["/sbin/tini", "--", "/home/CentralRepo/scripts/local_copy.sh"]

############################
# PROD STAGE
############################
FROM base as prod

# Add repo
ADD https://github.com/FortinetCloudCSE/CentralRepo.git#main /home/CentralRepo
WORKDIR /home/CentralRepo

# Force install CA certs from HTTP and configure apk to use HTTP; due to sudden issues with HTTPS; temporary fix until it's working again
RUN apk --no-cache --allow-untrusted --repository http://dl-cdn.alpinelinux.org/alpine/v3.21/main \
    add ca-certificates && \
    update-ca-certificates && \
    sed -i 's|https://dl-cdn.alpinelinux.org|http://dl-cdn.alpinelinux.org|g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache python3 py3-pip tini-static && \
    ln -sf python3 /usr/bin/python && \
    ln -sf /sbin/tini-static /sbin/tini

ENTRYPOINT ["/sbin/tini", "--", "/home/CentralRepo/scripts/local_copy.sh"]
