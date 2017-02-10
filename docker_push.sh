#!/bin/bash
eval $(docker-machine env default)

./docker_build.sh

docker login 

docker push liufuyang/lifeinweeks:latest
