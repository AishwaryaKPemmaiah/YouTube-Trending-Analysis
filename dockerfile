# Start from the official Apache Airflow image
FROM apache/airflow:2.8.1

# Switch to root to install OS dependencies
USER root

# Install OS-level dependencies (if any, optional)
# RUN apt-get update && apt-get install -y build-essential

# Switch back to airflow user
USER airflow

# Set working directory inside the container
WORKDIR /opt/airflow

# Copy your DAGs and source code into the container
COPY ./dags /opt/airflow/dags
COPY ./src /opt/airflow/src
COPY ./requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt
