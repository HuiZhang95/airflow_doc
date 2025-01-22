from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='04_task_sequence_morning',
    description='My DAG to know what to do in the morning',
    tags=['tutorial', 'datascientest'],
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(2),
    }
) as my_dag:

    def print_text(text):
        print(text)

    texts = [
        'Pulling on trousers',
        'Pull on right sock',
        'Pull on right shoe',
        'Pull on left sock',
        'Put on left shoe',
        'Take out'
    ]

    ids = [
        'trousers',
        'right_sock',
        'right_shoe',
        'sock_left',
        'left_shoe',
        'exit'
    ]

    tasks = []
    for t, i in zip(texts, ids):
        task = PythonOperator(
            task_id=i,
            python_callable=print_text,
            op_kwargs={'text': t}
        )
        tasks.append(task)

    tasks[0] >> [tasks[1], tasks[3]]
    tasks[1] >> tasks[2]
    tasks[3] >> tasks[4]
    [tasks[2], tasks[4]] >> tasks[5]

    # tasks[0] >> tasks[1]
    # tasks[0] >> tasks[3]
    # tasks[1] >> tasks[2]
    # tasks[3] >> tasks[4]
    # tasks[2] >> tasks[5]
    # tasks[4] >> tasks[5]




# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago


# my_dag = DAG(
#     dag_id='my_dag_of_the_morning',
#     description='My DAG to know what to do in the morning',
#     tags=['tutorial', 'datascientest'],
#     schedule_interval=None,
#     default_args={
#         'owner': 'airflow',
#         'start_date': days_ago(2),
#     }
# )


# def print_text(text):
#     print(text)


# texts = [
#     'Pulling on trousers',
#     'Pull on right sock',
#     'Pull on right shoe',
#     'Pull on left sock',
#     'Put on left shoe',
#     'Take out'
# ]

# ids = [
#     'trousers',
#     'right_sock',
#     'right_shoe',
#     'sock_left',
#     'left_shoe',
#     'exit'
# ]

# task1, task2, task3, task4, task5, task6 = [
#     PythonOperator(
#         dag=my_dag,
#         task_id=i,
#         python_callable=print_text,
#         op_kwargs={
#             'text': t
#         }
#     ) for t, i in zip(texts, ids)
# ]

# task1 >> task2
# task1 >> task4

# task2 >> task3

# task4 >> task5

# task3 >> task6
# task5 >> task6