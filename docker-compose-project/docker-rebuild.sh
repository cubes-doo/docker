#!/bin/sh
set -a
. "$(cd $(dirname "$0"); pwd)/.env"
set +a

docker-compose stop
docker-compose rm
docker-compose up -d --force-recreate