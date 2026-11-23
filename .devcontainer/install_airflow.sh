#!/usr/bin/env bash
# Install Apache Airflow (with the official constraints file), the analysis libraries, and Jupyter support.
set -e
AIRFLOW_VERSION=3.1.7
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install --upgrade pip
pip install "apache-airflow==${AIRFLOW_VERSION}" pandas scikit-learn --constraint "${CONSTRAINT_URL}"
pip install matplotlib ipykernel
airflow version
