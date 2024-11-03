from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import clickhouse_connect as cc
import time

def example(execution_date, **kwargs):
    # ClickHouse Settings
    host = os.getenv('CLICKHOUSE_HOST')
    port = os.getenv('CLICKHOUSE_PORT')
    user = os.getenv('CLICKHOUSE_USER')
    password = os.getenv('CLICKHOUSE_PASSWORD')
    database = os.getenv('CLICKHOUSE_DATABASE')

    # Start connection with ClickHouse
    client = cc.get_client(host=host, port=port, username=user, password=password, database=database)

    # Building the query
    query = "example"  # Insert your query here

    initial_time = time.time()
    client.command(query)
    end_time = time.time()
    elapsed_time = end_time - initial_time
    print(f"Query for the day {execution_date} completed successfully! Elapsed time: {elapsed_time}")  # Printing completion message and execution time

def create_dag():
    dag = DAG(
        'example_dag',
        default_args={
            'owner': 'Nicolas',
            'retries': 2,  # Number of attempts before giving up
            'retry_delay': timedelta(minutes=2),  # Interval between attempts
            'email_on_failure': False,  # Disabling email notifications on failure
        },
        description='DAG to extract data from the clickhouse table and do something with that.',
        start_date=datetime(2024, 1, 1),  # Start date for processing
        end_date=datetime(2024, 10, 24),  # End date for processing (Optional)
        schedule_interval='@daily',  # Setting the DAG to run daily
        max_active_runs=1,  # Ensures only one instance of the DAG runs at a time (Ideal for running on less powerful servers)
        catchup=True,  # Enabling backfilling
    )

    task = PythonOperator(
        task_id='example',
        python_callable=example,
        provide_context=True,
        op_kwargs={'execution_date': '{{ ds }}'},  # Passing the execution date in the function
        dag=dag,
    )

    return dag

globals()['example'] = create_dag()
