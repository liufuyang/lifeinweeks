#!/bin/bash
eval $(docker-machine env default)
./docker_build.sh

docker run -p 8000:8000 --name lifeinweeks \
	liufuyang/lifeinweeks:latest	
