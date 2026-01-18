from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    return main() 

default_args = {
    "description": "DAG to fetch weather data from API every 5 minutes",
    "start_date": datetime(2025, 1, 1),
    "catchup": False    
}

with DAG(
    dag_id="weather-api-orchestrator", 
    default_args=default_args,
    schedule=timedelta(minutes=5)  
) as dag:
    task1 = PythonOperator(
        task_id="ingest_data_task",
        python_callable=safe_main_callable
    )