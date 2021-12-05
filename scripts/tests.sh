#!/bin/bash

  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv --assume-yes


  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r test_requirements.txt


for service in frontend class-generator stats-generator calculator
do
    python3 -m pytest --pyargs $service --cov-report term-missing --cov=app
    
done