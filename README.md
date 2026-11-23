# Canopy Customer Segments

Pipeline that groups Canopy customers by purchasing behavior with k-means, describes each group, and explains the groups with a shallow decision tree. Apache Airflow orchestrates the pipeline in a GitHub Codespace.

## Repository

| Path | Contents |
|---|---|
| `data/canopy_customers.csv` | 1,500 customers, 7 prepared features |
| `src/segments.py` | Functions for scaling, clustering, profiles, and the surrogate tree |
| `dags/canopy_segments.py` | Airflow DAG |
| `notebooks/development.ipynb` | Environment check, function tests, and experiments |
| `output/` | Files the DAG writes |
| `docs/graph_view.png` | Screenshot of a successful run in the Graph view |
| `tools/package_submission.py` | Creates the submission zip |

## Start

1. Open a codespace on this repository: **Code > Codespaces > Create codespace on main**. The first build installs Airflow and Jupyter and takes several minutes.
2. Open `notebooks/development.ipynb` and run **Step 0: Verify the Environment**.
3. To run the pipeline, start Airflow with `bash start_airflow.sh`, open port 8080 from the **Ports** tab, unpause **canopy_segments**, and trigger the DAG.

## Submit

Commit and push all work, then run `python tools/package_submission.py` and submit `canopy_segments_submission.zip` with the repository link.

---

## Results

*Complete each section. Use the numbers in the output files.*

### Number of Clusters

Chosen k:

Justification (elbow method, silhouette score, and the meaning of the groups):

### Cluster Descriptions

| Cluster | Customers | Description | Proposed name |
|---|---|---|---|
| | | | |

### Surrogate Tree

Chosen depth:

Justification (agreement with the clusters and readability of the rules):

### Tree Rules Compared with the Profiles

Which features does the tree use to separate the clusters? Do the rules agree with the cluster averages? Where does the tree disagree with the clusters, and which customers are those?
