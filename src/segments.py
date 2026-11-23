"""Canopy customer segmentation: scaling, k-means, profiles, and a surrogate decision tree.

The DAG in dags/canopy_segments.py and the development notebook both call these functions.
Keep the settings below unchanged: the grading compares the outputs with reference results
computed with exactly these settings.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier, export_text

FEATURES = ["orders_per_year", "avg_order_value", "days_since_last_order", "categories_purchased",
            "discount_share", "return_rate", "tenure_months"]
K_RANGE = range(4, 8)        # candidate numbers of clusters: 4, 5, 6, 7
RANDOM_STATE = 0             # fixed seed for k-means and the decision tree
N_INIT = 10                  # k-means runs with 10 different starting centers and keeps the best


def load_customers(path):
    """Read the customer file into a DataFrame. (Provided.)"""
    return pd.read_csv(path)


def write_csv(table, path):
    """Write a DataFrame to CSV without the index, creating the folder when needed. (Provided.)"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(path, index=False)


def scale_features(df):
    """Scale every feature in FEATURES to the range 0 to 1.

    Use MinMaxScaler. Fit the scaler on df[FEATURES] and return the scaled values
    (a NumPy array with one row per customer and one column per feature, in FEATURES order).
    """
    raise NotImplementedError


def fit_kmeans(X, k):
    """Fit k-means with k clusters on the scaled features X and return the fitted model.

    Use KMeans with n_clusters=k, n_init=N_INIT, and random_state=RANDOM_STATE.
    """
    raise NotImplementedError


def evaluate_k(X, ks=K_RANGE):
    """Return one row per k with the two measurements used to choose k.

    Columns, in order:
      k                        the number of clusters
      avg_distance_to_center   average distance from each customer to the center of the
                               customer's cluster (the elbow method), rounded to 4 decimals
      silhouette               silhouette score of the clustering, rounded to 4 decimals

    Hint: model.transform(X) returns each customer's distance to every center; the distance
    to the customer's own center is the smallest value in each row.
    """
    raise NotImplementedError


def assign_clusters(df, X, k):
    """Return a DataFrame with two columns, customer_id and cluster, one row per customer.

    The cluster is the k-means label (0 to k - 1) from fit_kmeans(X, k).
    """
    raise NotImplementedError


def profile_clusters(df, assignments):
    """Return one row per cluster: the number of customers and the average of each feature.

    Columns, in order: cluster, customers, then FEATURES. Averages use the original
    (unscaled) values and are rounded to 2 decimals. Rows are sorted by cluster.
    """
    raise NotImplementedError


def train_surrogate(df, assignments, depth):
    """Train a decision tree that predicts each customer's cluster from the original features.

    Use DecisionTreeClassifier with max_depth=depth and random_state=RANDOM_STATE.
    Train on df[FEATURES] (unscaled) with the cluster from assignments as the label.
    Return the fitted tree.
    """
    raise NotImplementedError


def agreement(tree, df, assignments):
    """Return the share of customers (0 to 1) whose tree prediction matches the k-means cluster."""
    raise NotImplementedError


def tree_rules(tree):
    """Return the tree's rules as text, using export_text with the FEATURES names."""
    raise NotImplementedError
