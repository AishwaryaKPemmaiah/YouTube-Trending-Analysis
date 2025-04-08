from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.pipeline import load_data, preprocess_data, analyze_data

with DAG(
    "youtube_trending_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    task_load = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    task_preprocess = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data,
    )

    task_analyze = PythonOperator(
        task_id="analyze_data",
        python_callable=analyze_data,
    )

    task_load >> task_preprocess >> task_analyze
