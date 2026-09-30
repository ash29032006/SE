# ML Regression Notebook & CI/CD Pipeline

## Overview
This module contains the Jupyter notebook (`notebook085d1cc1d4.ipynb`) used to set up and validate the repository's GitHub Actions CI/CD workflow ([`ci-cd.yml`](../.github/workflows/ci-cd.yml)).

## Contents
- `notebook085d1cc1d4.ipynb`: Demonstrates linear regression (`height` vs `weight`), train/test splitting (`sklearn.model_selection`), and polynomial regression comparison.

## CI/CD Pipeline Stages
1. **`lint`**: Converts `ml_cicd/notebook085d1cc1d4.ipynb` to a Python script via `jupyter nbconvert` and checks it with `pylint`.
2. **`build-test`**: Executes the notebook end-to-end and exports an HTML report (`public/index.html`).
3. **`deploy`**: Publishes the generated HTML report to GitHub Pages on pushes to `main`.

## Running Locally
```bash
pip install -r ../requirements.txt
jupyter nbconvert --to notebook --execute notebook085d1cc1d4.ipynb --output executed_notebook.ipynb
```
