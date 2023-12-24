# StarPlot Project

This project aims to analyze star data using Python.

## Project Structure

- `src/`: Source directory.
  - `star_type_classification/`: Package containing the star analysis scripts.
    - `models/`: Directory containing classification and visualization modules.
      - `__init__.py`: Initialization file for the models directory.
      - `classification.py`: Module for star classification.
      - `visualization.py`: Module for visualizing star data.
    - `__init__.py`: Initialization file for the `star_type_classification` package.
    - `train.py`: Script for training the star classification model.

- `data/`: Directory containing dataset files.
  - `stars_dataset.csv`: CSV file containing star data.

## How to Use

1. **Star Classification**:
    - The `src/star_type_classification/models/classification.py` module provides functions for training classification models based on star data.

2. **Data Visualization**:
    - Utilize the `src/star_type_classification/models/visualization.py` module to create visualizations, such as HR diagrams, from star data.

3. **Training the Model**:
    - To train the star classification model, execute `python3 train.py ../data/stars_dataset.csv` from within the `/src/star_type_classification` directory.

    Example:
    ```bash
    python3 train.py ../data/stars_dataset.csv
    ```
    This command will run the script for training the model using the provided dataset.

4. **Model Performance**:
    - After training, the model achieves an accuracy of 97.92% on the test dataset.

## Dependencies

- Python 3.x
- Required Python packages (specified in `requirements.txt` or `Pipfile` if using Pipenv).

## Getting Started

1. Clone the repository.
2. Install dependencies (`pip install -r requirements.txt` or `pipenv install`).
3. Navigate to the `/src/star_type_classification` directory.
4. Train the model using ` python3 train.py ../data/stars_dataset.csv`.
