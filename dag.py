# Attempt at automating process via airflow instead of running each task through main.py

from airflow import DAG
from airflow.operators.python import PythonOperator
import scrape, transform
from db import db_loader

default_args = {
    'retries': 1
}

dag = DAG(
    'player_stats_workflow',
    default_args=default_args,
    description='Player stats ETL process',
    schedule_interval=None  # Set to run manually
)

def scrape_task():
    scrape.scrape_skater_data()
    scrape.scrape_goalie_data()

def transform_task():
    transform.transform_skaters()
    transform.transform_goalies()

def load_task():
    db_loader.load_to_db()

t1 = PythonOperator(
    task_id='scrape_task',
    python_callable=scrape_task,
    dag=dag
)

t2 = PythonOperator(
    task_id='transform_task',
    python_callable=transform_task,
    dag=dag
)

t3 = PythonOperator(
    task_id='load_task',
    python_callable=load_task,
    dag=dag
)

t1 >> t2 >> t3 