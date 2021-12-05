#!/bin/bash

sudo docker-compose build --parallel
sudo docker login -u ${DOCKER_UNAME} -p ${DOCKER_PWORD}
sudo docker-compose push