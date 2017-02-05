#!/bin/sh
set -a
. "$(cd $(dirname "$0"); pwd)/.env"
set +a
docker-compose stop
