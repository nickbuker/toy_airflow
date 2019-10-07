# Toy Airflow

## Author
Nick Buker

## Introduction
The contents of this repo began as a simple toy project to help teach myself [Apache Airflow](https://airflow.apache.org/). Upon realizing that Airflow is pretty darn awesome, I decided to turn this project into a lightning talk for [PuPPy](https://www.pspython.com/app/).

## Requirements
- Python 3.7
- Installation of the contents of the `requirements.txt` file

## Running the project
1. Create a suitable environment (Python 3.7 with contents of `requirements.txt` file installed).
2. Navigate to the root directory of this project.
3. Run the following command to launch the webserver:
```
$ bash launch_webserver.sh
```
4. Open the webserver at address http://0.0.0.0:8080 with your browser of choice. Navigate to the DAGs tab and switch `nick_toy_airflow` DAG to On.
5. Open a new terminal and navigate to the root directory of this project.
6. Run the following command to launch the scheduler:
```
$ bash launch_scheduler.sh
```
7. The DAG should run once per minute until you kill the scheduler or turn the job off from the webserver. Text files will appear and then be deleted from the `output/` directory.

## Project structure
```
├── README.md
├── dags/
│   └── toy_airflow.py
├── launch_scheduler.sh
├── launch_webserver.sh
├── output/
├── requirements.txt
└── src/
    ├── file_creator.py
    └── file_deletor.py
```
- `dags/` - The directory that Airflow scans to detect DAGs
- `launch_scheduler.sh` - Simple Bash script for launching the Airflow scheduler
- `launch_webserver.sh` - Simple Bash script for launching the Airflow webserver
- `output/` - Directory where code outputs files
- `requirements.txt` - Python libraries required for this project
- `src/` - The directory containing the Python code that forms the tasks in the DAG.
