# Architecture Overview (Beginner-Friendly Explanation)

This project implements a modern data engineering and AI infrastructure for a healthcare platform that connects data from senior living communities, providers, and EHR systems.

The goal is to build a system that can ingest data from many sources, clean it, organize it, and transform it into analytics- and AI-ready datasets.

## This architecture follows five major layers:

### -Data Ingestion Layer
Handles collecting data from external systems such as:

EHR/EMR systems (FHIR API)

Resident management systems

IoT devices (vitals, sensors)

CSV/JSON batch uploads

We use Airbyte for ingestion.

### -Orchestration Layer
Manages all scheduled workflows.
We use Airflow to automate:

Ingestion

Transformations

Quality checks

Gold table updates

### -Storage Layer (Delta Lake + ADLS)
Data is stored in three structured layers:

Bronze (raw)

Silver (cleaned)

Gold (analytics-ready)

Delta Lake provides:

ACID transactions

Schema evolution

Versioning

Time travel

### -Transformation Layer (Databricks)
All data cleaning, standardization, and modeling happen here using:

PySpark

SQL

Databricks Notebooks

AI & Analytics Layer
Prepared datasets support:

Dashboards

Predictive models

LLM-powered insights

Vector search engines

Infrastructure as Code (Terraform + Azure)
All resources are defined using Terraform:

Azure Storage

Azure Databricks

Azure Key Vault

Azure FHIR Server

Security & Governance
Includes:

Encryption at rest & in transit

Role-based access control (RBAC)

Secret management via Key Vault

Audit logs & data lineage tracking

This architecture ensures the platform is reliable, scalable, secure, and ready to support AI applications.
