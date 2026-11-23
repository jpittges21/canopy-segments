#!/usr/bin/env bash
# Start Airflow in a GitHub Codespace.
# The browser reaches Airflow through the Codespace's public address;
# running tasks report back to Airflow through the local address.
if [ -n "$CODESPACE_NAME" ]; then
  export AIRFLOW__API__BASE_URL="https://${CODESPACE_NAME}-8080.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
fi
export AIRFLOW__CORE__EXECUTION_API_SERVER_URL="http://localhost:8080/execution/"
airflow standalone
