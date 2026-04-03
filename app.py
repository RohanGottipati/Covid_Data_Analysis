import os
import json
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Load cleaned CSV produced by notebook.ipynb
# Run the notebook first to generate COVID_Country_Sample_cleaned.csv
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_CSV = os.path.join(BASE_DIR, "COVID_Country_Sample_cleaned.csv")

NUMERIC_COLS = ["new_cases", "new_deaths", "new_vaccinations", "cases_per_million"]

METRIC_LABELS = {
    "new_cases": "New Cases",
    "new_deaths": "New Deaths",
    "new_vaccinations": "New Vaccinations",
    "cases_per_million": "Cases per Million",
}

DF = pd.read_csv(CLEANED_CSV, parse_dates=["date"])

COUNTRIES = sorted(DF["country"].unique().tolist())
DATE_MIN = DF["date"].min().strftime("%B %Y")
DATE_MAX = DF["date"].max().strftime("%B %Y")


# ---------------------------------------------------------------------------
# Part B - Flask Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Root route - renders the dashboard."""
    initial_data = _build_chart_data("Canada", "new_cases")
    return render_template(
        "index.html",
        countries=COUNTRIES,
        date_min=DATE_MIN,
        date_max=DATE_MAX,
        metric_labels=METRIC_LABELS,
        initial_data=json.dumps(initial_data),
        default_country="Canada",
        default_metric="new_cases",
    )


@app.route("/data")
def data():
    """Part D - JSON API endpoint.

    Query params:
        country  - e.g. Canada
        metric   - one of new_cases, new_deaths, new_vaccinations, cases_per_million
    """
    country = request.args.get("country", "Canada")
    metric = request.args.get("metric", "new_cases")

    if country not in COUNTRIES:
        return jsonify({"error": f"Unknown country: {country}"}), 400
    if metric not in METRIC_LABELS:
        return jsonify({"error": f"Unknown metric: {metric}"}), 400

    return jsonify(_build_chart_data(country, metric))


def _build_chart_data(country: str, metric: str) -> dict:
    subset = DF[DF["country"] == country].sort_values("date")
    return {
        "country": country,
        "metric": metric,
        "metric_label": METRIC_LABELS[metric],
        "dates": subset["date"].dt.strftime("%Y-%m-%d").tolist(),
        "values": subset[metric].tolist(),
        "rolling": subset[f"{metric}_rolling"].round(2).tolist(),
    }


if __name__ == "__main__":
    app.run(debug=True)
