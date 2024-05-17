from airflow import DAG # type: ignore
from datetime import datetime
import os
import sys
from airflow.operators.python_operator import PythonOperator # type: ignore


# Set the path to the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pipelines.extract_reddit_pipeline import extract_reddit_pipeline
from pipelines.aws_s3_pipeline import upload_to_s3_pipeline

print(f"Project root: {project_root}")


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 16),
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='reddit_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline'],
)

#extraction from reddit
extract_reddit = PythonOperator(
    task_id='extract_reddit',
    python_callable = extract_reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{file_postfix}',
        'subreddit': 'worldnews',
        'limit': 100,
        'time_filter':'day'
    },
    dag=dag 
)

#upload to S3
upload_to_s3 = PythonOperator(
    task_id='upload_to_s3',
    python_callable = upload_to_s3_pipeline,
    dag=dag 
)

extract_reddit >> upload_to_s3

