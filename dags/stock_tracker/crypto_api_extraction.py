from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import requests


def extract_crypto_data():
    url = (
        "https://www.alphavantage.co/query"
        "?function=DIGITAL_CURRENCY_DAILY"
        "&symbol=BTC"
        "&market=EUR"
        "&apikey=demo"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    print(data)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="crypto_api_extraction",
    default_args=default_args,
    start_date=datetime(2025, 12, 27),
    schedule_interval="@daily",
    catchup=False,
    tags=["api", "crypto"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_crypto_data",
        python_callable=extract_crypto_data,
    )

    extract_task
