#!/bin/bash

# set Airflow home
AIRFLOW_HOME="$(pwd)"
export AIRFLOW_HOME

# initialize datebase
airflow initdb

# start web server
airflow webserver --port 8080
