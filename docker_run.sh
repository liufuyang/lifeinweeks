#!/bin/bash
set -e
eval $(docker-machine env default)
./docker_build.sh

./start_postgres_local.sh

docker stop lifeinweeks && true
docker rm lifeinweeks && true

echo $(pwd)
mkdir -p backend/log

docker run --rm -p 8000:8000 -p 443:443 --name lifeinweeks \
	-e "LOGGING_FILENAME=/var/www/app/log/lifeinweeks.log" \
	-e "DB_HOST=192.168.99.100" \
	-e "DB_PORT=54328" \
	-e "DB_USER=postgres" \
	-e "DB_PASS=password" \
	-e "DB_NAME=lifeinweeks" \
	-v $(pwd)/log:/var/www/app/log \
	-v $(pwd)/backend/config:/etc/nginx/ssl \
	liufuyang/lifeinweeks:latest	
