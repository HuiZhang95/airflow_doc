from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import random


def function_with_return(task_instance):
    task_instance.xcom_push(
        key="my_xcom_value",
        value=random.uniform(a=0, b=1)
    )


with DAG(
    dag_id='18_simple_xcom_give_output_name',
    schedule_interval=None,
    tags=['tutorial', 'datascientest'],
    start_date=days_ago(0)
) as dag:

    my_task = PythonOperator(
        task_id='python_task',
        python_callable=function_with_return
    )