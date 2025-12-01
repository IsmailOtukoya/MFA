from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

# Default args for this DAG
default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

# This config tells Databricks what to run
# In a real setup you would replace notebook_path and cluster config
bronze_notebook_task = {
    "notebook_path": "/Users/black.ismail@databricks.com/Bronze Ingestion",
}

# Option 1: use an existing cluster (set in Airflow Variables)
bronze_job_config = {
    "existing_cluster_id": "{{ var.value.databricks_cluster_id }}",
    "notebook_task": bronze_notebook_task,
}

with DAG(
    dag_id="ingest_bronze_dag",
    default_args=default_args,
    description="Ingest raw data into Bronze Delta tables in Databricks",
    schedule_interval="@daily",  # or "0 * * * *" for hourly
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["bronze", "databricks", "ingestion"],
) as dag:

    ingest_bronze = DatabricksSubmitRunOperator(
        task_id="run_bronze_notebook",
        databricks_conn_id="databricks_default",  # configured in Airflow UI
        json=bronze_job_config,
    )
