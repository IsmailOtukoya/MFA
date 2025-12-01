from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

silver_notebook_task = {
    "notebook_path": "/Users/my.email@databricks.com/Silver Transformations",
}

silver_job_config = {
    "existing_cluster_id": "{{ var.value.databricks_cluster_id }}",
    "notebook_task": silver_notebook_task,
}

with DAG(
    dag_id="bronze_to_silver_dag",
    default_args=default_args,
    description="Transform Bronze Delta tables into cleaned Silver tables",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["silver", "databricks", "transformations"],
) as dag:

    bronze_to_silver = DatabricksSubmitRunOperator(
        task_id="run_silver_notebook",
        databricks_conn_id="databricks_default",
        json=silver_job_config,
    )
