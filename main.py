from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="airflow_workshop",
    schedule_interval="0 0 * * *",
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    task_hello_world = PythonOperator(
        task_id="hello_world",
        python_callable=hello_world,
    )


def hello_world():
    print("Hello World")