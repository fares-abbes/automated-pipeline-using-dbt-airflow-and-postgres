from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator 
from airflow.providers.docker.operators import DockerOperator
from datetime import datetime, timedelta
import sys


def safe_main_callable():
    from insert_records import main
    return main() 

default_args = {
    "description": "DAG to fetch weather data from API every 5 minutes",
    "start_date": datetime(2025, 1, 1),
    "catchup": False    
}

with DAG(
    dag_id="weather-dbt-orchestrator", 
    default_args=default_args,
    schedule=timedelta(minutes=5)  
) as dag:
    task1 = PythonOperator(
        task_id="ingest_data_task",
        python_callable=safe_main_callable
    )
    task2 = DockerOperator(
        task_id="dbt_run_task",
        image="ghcr.io/dbt-labs/dbt-postgres:1.9.latest",
        command="run",
        working_dir="/usr/app",
        Mounts=[
            Mount=[
                target="/usr/app",
                type="bind"
            ]
            
        ],
        network_mode="bridge",
        docker_url="unix://var/run/docker.sock",
        auto_remove=True,
