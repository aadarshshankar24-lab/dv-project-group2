# Global Trends in Internet Usage and Economic Development

**Group 2** — Aadarsh Shankar, Divy Jhanjhari  
**Course:** Data Visualization |

---
## How to Run
Open Terminal on your Mac and follow these steps one by one.

### 1. Navigate into the project folder
```
cd path/to/project
```
### 2.Create a virtual environment

This keeps the project dependencies separate from your system Python.

```
python3 -m venv venv
source venv/bin/activate

venv also contains the installed python libraries used
```
### 3. Install dependencies
```
pip3 install -r requirements.txt
```

### 4. Start the Flask server

```
python3 app.py
```

You should see something like this in your terminal:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### 5. Open in your browser

```
open the link from terminal in browser
```
The dataset loads automatically from the `data/` folder.

---

## Project Structure

```
under my own folder locally and then/project/
├── app.py                      # Flask backend — serves pages and data API
├── requirements.txt            # Python dependencies
├── data/
│   └── internet_gdp_data.csv   # Dataset: 50 countries × 24 years = 1200 rows
├── templates/
│   └── index.html              # Main interactive visualization (Plotly.js)
└── README.md
```

---

## How to Read the Visualization

### Stats Bar (top)
Shows live summary statistics for the selected year — average internet usage, average GDP per capita, and the country with the highest internet penetration.

### Controls
- **Year Slider** — drag left/right to animate the scatter plot across years (2000–2023)
- **Income Group Filter** — narrows the scatter plot to a specific income tier
- **Region Filter** — highlights a specific region in the line chart

---

## Visualization Idioms

### 1. Scatter Plot — GDP per Capita vs Internet Usage
- **X-axis (log scale):** GDP per capita in USD. Log scale is used because GDP spans from ~$500 to ~$85,000.
- **Y-axis:** Internet users as a percentage of the population.
- **Bubble size:** Proportional to GDP per capita — bigger bubbles = wealthier countries.
- **Bubble color:** Each color represents a geographic region (see legend).
- **Interactivity:** Year slider animates the plot. Income filter narrows countries shown. Hover over any bubble to see country name, exact GDP, and internet %.
- **What to look for:** The positive upward trend — richer countries cluster top-right. Over time, all countries shift upward (more internet), but the gap between rich and poor persists.

### 2. Line Chart — Internet Growth Over Time
- **X-axis:** Years from 2000 to 2023.
- **Y-axis:** Average internet usage (%) per region.
- **Each line:** One geographic region. Lines are smoothed for readability.
- **Interactivity:** Use the region filter to isolate a specific region. Hover for exact values.
- **What to look for:** All regions grow, but at very different rates. Europe and North America started high and plateaued. Sub-Saharan Africa started near zero and is still catching up.

### 3. Bar Chart — Regional Internet Comparison (2023)
- **X-axis:** Average internet usage percentage for 2023.
- **Y-axis:** World regions, sorted highest to lowest.
- **Color:** Each bar matches its region color from the scatter plot.
- **Interactivity:** Hover bars for exact values.
- **What to look for:** The gap between regions is stark — North America and Europe near 95%, Sub-Saharan Africa around 35%.

---

## Dataset

| Column | Type | Description |
|---|---|---|
| Country Name | Categorical | Name of the country |
| Country Code | Categorical | ISO 3-letter code |
| Year | Ordered (2000–2023) | Year of measurement |
| GDP per Capita | Quantitative (USD) | Economic output per person |
| Internet Users | Quantitative (%) | % of population using internet |
| Income Group | Ordered Categorical | World Bank classification |
| Region | Categorical | Geographic region |

**Source:** World Bank Open Data — https://data.worldbank.org  
**Coverage:** 50 countries, 2000–2023 (1,200 rows)

---
Our live URL(We used render) - https://dv-project-group2.onrender.com
---
