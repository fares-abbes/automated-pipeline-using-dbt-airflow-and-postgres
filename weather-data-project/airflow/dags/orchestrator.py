from airflow import DAG

from datetime import datetime
default_args = {
    "owner": "airflow", 
    "start_date": datetime,
}
DAG(
    dag_id="weather-api-administrator", 
    default_args=default_args,
    schedule=...
)
with DAG(
    task1