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

gold_notebook_task = {
    "notebook_path": "/Users/my.email@databricks.com/Gold Analytics",
}

gold_job_config = {
    "existing_cluster_id": "{{ var.value.databricks_cluster_id }}",
    "notebook_task": gold_notebook_task,
}

with DAG(
    dag_id="silver_to_gold_dag",
    default_args=default_args,
    description="Transform Silver Delta tables into Gold analytics tables",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["gold", "databricks", "analytics"],
) as dag:

    silver_to_gold = DatabricksSubmitRunOperator(
        task_id="run_gold_notebook",
        databricks_conn_id="databricks_default",
        json=gold_job_config,
    )
