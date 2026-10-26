# COVID-19 Global Trends Dashboard

Interactive Flask web app for exploring monthly COVID-19 data for five countries (January 2020 to December 2024), backed by a Jupyter notebook that cleans the raw dataset.

## Features

- **Data cleaning notebook** (`notebook.ipynb`): loads the raw CSV, inspects it, fills the missing `new_vaccinations` values with 0, caps outliers per country at the 3×IQR outer fence, computes 3-month rolling means, and writes `COVID_Country_Sample_cleaned.csv`.
- **Interactive dashboard**: choose a country (Canada, India, Japan, United Kingdom, United States) and a metric (New Cases, New Deaths, New Vaccinations, Cases per Million); the chart updates via `fetch` without a page reload.
- **Rolling mean overlay**: optional 3-month rolling mean line.
- **JSON API**: `GET /data?country=<country>&metric=<metric>` returns dates, values and rolling means; unknown countries or metrics return HTTP 400.
- **Insights section** with notes on wave patterns, vaccination rollout, normalisation, caveats and data-handling choices.

## Tech Stack

- Python, pandas, Jupyter (data cleaning)
- Flask (server, Jinja2 template, JSON endpoint)
- Plotly.js 2.35.2 loaded from CDN (charts; no frontend build step)
- Plain HTML/CSS

## Project Structure

```
notebook.ipynb                      - Part A: load, inspect, clean, save the cleaned CSV
app.py                              - Flask app: "/" dashboard and "/data" JSON endpoint
templates/index.html                - Dashboard UI (controls, Plotly chart, insights)
static/style.css                    - Responsive styles
COVID_Country_Sample.csv            - Raw dataset (5 countries x 60 months)
COVID_Country_Sample_cleaned.csv    - Cleaned dataset produced by the notebook (committed)
```

## Prerequisites

- Python 3
- pip

## Setup

```bash
pip install flask pandas jupyter
```

## Usage

### 1. (Optional) Regenerate the cleaned data

The cleaned CSV is already committed, so this step is only needed if you change the raw data or cleaning logic. Open and run all cells in the notebook:

```bash
jupyter notebook notebook.ipynb
```

or run it headlessly:

```bash
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
```

### 2. Run the Flask app

From the repository root:

```bash
flask run
```

or

```bash
python app.py
```

(the latter starts Flask in debug mode). Then open http://127.0.0.1:5000 in your browser.

### API example

```bash
curl "http://127.0.0.1:5000/data?country=Canada&metric=new_cases"
```

Valid `metric` values: `new_cases`, `new_deaths`, `new_vaccinations`, `cases_per_million`.

## Data

Dataset columns: `date`, `country`, `new_cases`, `new_deaths`, `new_vaccinations`, `population`, `cases_per_million`, `vaccinations_per_hundred`. The cleaned file adds `<metric>_rolling` columns for the four charted metrics. The dashboard attributes the data to Our World in Data's COVID-19 dataset (monthly sample).

No environment variables are required.
