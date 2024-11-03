# 🐬 ClickHouse ETL with Airflow 🚀

Welcome to **ClickHouse ETL with Airflow**, a project that streamlines the extraction and loading of data between ClickHouse tables using Apache Airflow! 🌟

## 📚 Overview

This project automates the process of extracting data from one ClickHouse table and inserting it into another, making your data workflow efficient and reliable. With Airflow managing the orchestration, you can easily schedule and monitor your ETL processes.

## 🔧 Features

- **🔄 Data Extraction:** Seamlessly extract data from a specified ClickHouse table.
- **📥 Data Loading:** Insert the extracted data into another ClickHouse table.
- **🕒 Scheduling:** Utilize Apache Airflow to schedule and automate the ETL workflow.
- **📊 Monitoring:** Keep track of your data pipeline's performance and status through Airflow's web interface.

## ⚙️ Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)

### Usage

1. **Configure Connection to ClickHouse**: Fill in the ClickHouse connection details in the `.env` file. Ensure that you specify the `CLICKHOUSE_HOST`, `CLICKHOUSE_PORT`, `CLICKHOUSE_USER`, `CLICKHOUSE_PASSWORD`, `CLICKHOUSE_DATABASE`, `CLICKHOUSE_FROM_TABLE`, and `CLICKHOUSE_TO_TABLE` variables.

2. **Set Up Your DAG**: Define your data pipeline by configuring the DAG (Directed Acyclic Graph) in Airflow to handle your ETL process.

3. **Run Airflow with Docker Compose**: Start Airflow and all necessary services by running:
   ```bash
   docker-compose up```

4. **Log In to Airflow**: Access the Airflow web interface at http://localhost:8080 and log in using the following credentials:

    Username: airflow
    Password: airflow

5. **Execute the DAG**: In the Airflow web interface, locate the DAG you created and manually trigger it or wait for it to run as per the scheduled interval.

And you're all set! Your ETL process will now be managed and monitored through Apache Airflow.
