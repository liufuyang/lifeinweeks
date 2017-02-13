#!/bin/bash
eval $(docker-machine env default)
./docker_build.sh

docker stop lifeinweeks
docker rm lifeinweeks

echo $(pwd)
mkdir -p backend/log

docker run --rm -p 8000:8000 -p 443:443 --name lifeinweeks \
	-v $(pwd)/log:/var/www/app/log \
	-v $(pwd)/backend/config:/etc/nginx/ssl \
	liufuyang/lifeinweeks:latest	
