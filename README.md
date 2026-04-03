# COVID-19 Global Trends Dashboard

Interactive Flask web app visualising monthly COVID-19 data for 5 countries (2020 to 2024).

## Setup

```bash
pip install flask plotly pandas jupyter
```

## Step 1 - Run the notebook (Part A)

Open and run all cells in `notebook.ipynb`. This loads the raw CSV, inspects it with `head()` and `info()`, handles missing values and outliers, computes rolling means, and saves `COVID_Country_Sample_cleaned.csv`.

```bash
jupyter notebook notebook.ipynb
```

## Step 2 - Run the Flask app

```bash
flask run
```

Then open **http://127.0.0.1:5000** in your browser.

## File Structure

```
notebook.ipynb                      - Part A: load, inspect, clean, save
app.py                              - Flask app (loads cleaned CSV)
templates/index.html                - Dashboard UI (Plotly + fetch)
static/style.css                    - Responsive styles
COVID_Country_Sample.csv            - Raw dataset
COVID_Country_Sample_cleaned.csv    - Cleaned dataset (produced by notebook)
README.md
```
