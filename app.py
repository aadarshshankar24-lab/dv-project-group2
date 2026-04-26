from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load dataset once at startup
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "internet_gdp_data.csv")
df = pd.read_csv(DATA_PATH)

@app.route("/")
def index():
    """Serve the main visualization page."""
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    """Return full dataset as JSON for frontend charts."""
    return jsonify(df.to_dict(orient="records"))

@app.route("/api/summary")
def get_summary():
    """Return summary statistics by region and year."""
    summary = (
        df.groupby(["Region", "Year"])
        .agg(avg_internet=("Internet Users", "mean"),
             avg_gdp=("GDP per Capita", "mean"))
        .reset_index()
        .round(2)
    )
    return jsonify(summary.to_dict(orient="records"))

@app.route("/api/years")
def get_years():
    """Return list of available years."""
    return jsonify(sorted(df["Year"].unique().tolist()))

@app.route("/api/regions")
def get_regions():
    """Return list of available regions."""
    return jsonify(sorted(df["Region"].unique().tolist()))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
