#!/bin/bash

# set Airflow home
export AIRFLOW_HOME="$(pwd)"

# initialize datebase
airflow initdb

# start web server
# airflow webserver --port 8080

# start scheduler
airflow scheduler
