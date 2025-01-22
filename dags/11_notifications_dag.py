import random
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import datetime


def failed_task():
    raise Exception('This task did not work!')

with DAG(
    dag_id='11_notificatons_dag',
    tags=['tutorial', 'datascientest'],
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(0, minute=1)
    },
    catchup=False
) as my_dag:

    task1 = PythonOperator(
        task_id='task1',
        python_callable=failed_task,
        retries=5,
        retry_delay=datetime.timedelta(seconds=10),
        dag=my_dag,
        email_on_retry=True,
        email=['hzhang.davis@gmail.com']
    )
