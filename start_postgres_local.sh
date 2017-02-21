#!/bin/sh
eval $(docker-machine env default)

docker stop lifeinweeks-postgres
docker rm lifeinweeks-postgres

docker run --name lifeinweeks-postgres -d \
	-e POSTGRES_PASSWORD=password \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_DB=lifeinweeks \
	-p 54328:5432 \
	-d postgres:9.3
