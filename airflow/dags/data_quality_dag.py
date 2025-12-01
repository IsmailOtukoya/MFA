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

dq_notebook_task = {
    "notebook_path": "/Users/my.email@databricks.com/Data Quality Checks",
}

dq_job_config = {
    "existing_cluster_id": "{{ var.value.databricks_cluster_id }}",
    "notebook_task": dq_notebook_task,
}

with DAG(
    dag_id="data_quality_dag",
    default_args=default_args,
    description="Run data quality checks on Silver and Gold tables",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["quality", "databricks", "dq"],
) as dag:

    run_data_quality = DatabricksSubmitRunOperator(
        task_id="run_dq_notebook",
        databricks_conn_id="databricks_default",
        json=dq_job_config,
    )
