# standard library imports
import datetime as dt
import os
import sys
# third party imports
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# custom imports
sys.path.append(os.path.join('.'))
from src.file_creator import FileCreator
from src.file_deletor import FileDeletor


default_args = {
    'owner': 'Nick Buker',
    'start_date': dt.datetime(2019, 10, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# Create DAG
dag = DAG(
    dag_id='nick_toy_airflow',
    default_args=default_args,
    catchup=False,  # don't forget to set to False!
    schedule_interval='* * * * *',
)

# Instantiate creator objects
creator_1 = FileCreator(file=os.path.join('output', 'out_1.txt'))
creator_2 = FileCreator(file=os.path.join('output', 'out_2.txt'))
deletor = FileDeletor(del_dir='output')

# Create tasks
task_1 = PythonOperator(
    task_id='task_1',
    python_callable=creator_1.create,
    dag=dag
)
task_2 = PythonOperator(
    task_id='task_2',
    python_callable=creator_2.create,
    dag=dag
)
task_3 = PythonOperator(
    task_id='task_3',
    python_callable=deletor.delete,
    dag=dag,
)

# Specify dependencies
[task_1, task_2] >> task_3

# This is equivalent to:
# task_3.set_upstream([task_1, task_2])
