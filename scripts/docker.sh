#!/bin/bash

docker-compose build --parallel
docker login -u ${DOCKER_UNAME} -p ${DOCKER_PWORD}
docker-compose push