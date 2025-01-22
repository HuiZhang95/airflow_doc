from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import random


def function_with_return():
    return random.uniform(a=0, b=1)


with DAG(
    dag_id='17_simple_xcom_dag',
    schedule_interval=None,
    tags=['tutorial', 'datascientest'],
    start_date=days_ago(0)
) as dag:

    my_task = PythonOperator(
        task_id='python_task',
        python_callable=function_with_return
    )