"""Canopy customer segmentation pipeline.

Tasks:
  evaluate_k        writes output/k_evaluation.csv
  assign_clusters   writes output/cluster_assignments.csv
  profile_clusters  writes output/cluster_profile.csv
  train_surrogate   writes output/tree_rules.txt and output/tree_agreement.csv

Dependencies: evaluate_k runs first; assign_clusters runs next; profile_clusters and
train_surrogate both need the assignments and run in parallel.
"""
import sys
from datetime import datetime
from pathlib import Path

from airflow.sdk import dag, task

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))
DATA = PROJECT / "data" / "canopy_customers.csv"
OUT = PROJECT / "output"

K = None            # TODO: set to the number of clusters the team chooses (4 to 7)
TREE_DEPTH = None   # TODO: set to the tree depth the team chooses (3 or 4)


@dag(schedule=None, start_date=datetime(2025, 1, 1), catchup=False, tags=["canopy"])
def canopy_segments():

    @task
    def evaluate_k():
        """Write the elbow and silhouette measurements for every k in K_RANGE."""
        import segments as s
        # TODO: load the customers, scale the features, evaluate k, and write output/k_evaluation.csv

    @task
    def assign_clusters():
        """Write each customer's cluster for k = K."""
        import segments as s
        # TODO: write output/cluster_assignments.csv

    @task
    def profile_clusters():
        """Write the size and feature averages of each cluster."""
        import segments as s
        # TODO: read the assignments and write output/cluster_profile.csv

    @task
    def train_surrogate():
        """Write the tree rules and the tree's agreement with the clusters."""
        import segments as s
        # TODO: write output/tree_rules.txt and output/tree_agreement.csv
        # tree_agreement.csv has one row with two columns: tree_depth, agreement (rounded to 4 decimals)

    # TODO: create the four tasks and set the dependencies described at the top of the file


canopy_segments()
