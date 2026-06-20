from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="primeira_dag",
    schedule="@minutely",
    start_date=datetime(2026, 6, 20),
    catchup=False,
)
def primeira_dag():
    @task
    def primeira_atividade():
        print("Minha primeira atividade! - Hello World")
        sleep(2)

    @task
    def segunda_atividade():
        print("Minha segunda atividade! - World")
        sleep(2)

    @task
    def terceira_atividade():
        print("Minha terceira atividade! - Hello World")
        sleep(2)

    @task
    def quarta_atividade():
        print("Minha quarta atividade! - Hello World")
        sleep(2)

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4


primeira_dag()