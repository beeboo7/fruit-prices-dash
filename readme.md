# Fruit Prices Dashboard

An interactive web dashboard built with Python and Dash. Pick one or more fruits from a dropdown and the chart updates to show their prices.

## Features

- Multi-select dropdown to choose which fruits to display
- Chart that updates instantly when the selection changes (via a Dash callback)
- Runs locally in the browser, with no database or external data needed

## Tech Stack

- Python
- Dash (charts are rendered with Plotly under the hood)

## Getting Started

### Requirements

- Python 3.8 or newer

### Installation

```bash
git clone https://github.com/beeboo7/fruit-prices-dashboard.git
cd fruit-prices-dashboard
pip install -r requirements.txt
```

### Run the app

```bash
python fruitprices.py
```

Then open [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser. Press `Ctrl + C` in the terminal to stop it.

## Project Structure

```
fruit-prices-dashboard/
├── fruitprices.py     # Dash app: layout and callback
├── requirements.txt   # Dependencies
└── README.md
```

## How It Works

- The fruit names and prices are stored in a Python dictionary.
- The layout has a heading, a graph and a multi-select dropdown (Apples is selected by default).
- A callback listens to the dropdown, looks up the price of each selected fruit and returns a new chart figure.

## Possible Improvements

- Use a bar chart, which suits comparing categories better than a line
- Load prices from a CSV file or API instead of hardcoding them
- Add more fruits, price history over time, or a date filter
- Add a "select all" option and styling to the layout

## Author

Aimee Teppo
