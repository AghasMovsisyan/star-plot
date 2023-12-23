# StarPlot Project

This project aims to analyze star data using Python.

## Project Structure

- `models/`: Directory containing modules for star classification and visualization.
  - `__init__.py`: Initialization file indicating this directory is a package.
  - `classification.py`: Module for star classification.
  - `visualization.py`: Module for visualizing star data.

- `src/`: Source directory.
  - `__init__.py`: Initialization file for the source directory.
  - `main.py`: Main script for analyzing star data.

- `data/`: Directory containing dataset files.
  - `stars_dataset.csv`: CSV file containing star data.

## How to Use

1. **Star Classification**:
    - The `models/classification.py` module provides functions for training classification models based on star data.

2. **Data Visualization**:
    - Utilize the `models/visualization.py` module to create visualizations, such as HR diagrams, from star data.

3. **Running the Analysis**:
    - To run the star analysis, execute `python3 main.py` from within the `/src` directory.

## Dependencies

- Python 3.x
- Required Python packages (specified in `requirements.txt` or `Pipfile` if using Pipenv).

## Getting Started

1. Clone the repository.
2. Install dependencies (`pip install -r requirements.txt` or `pipenv install`).
3. Navigate to the `/src` directory.
4. Execute the analysis using `python3 main.py`.

