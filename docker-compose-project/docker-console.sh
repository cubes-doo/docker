#!/bin/sh
set -a
. "$(cd $(dirname "$0"); pwd)/.env"
set +a
docker exec -it ${PROJECT_NAME}_webserver bash