import sys
sys.path.append('../')  # Add the parent directory to the Python path

from models.classification import train_classification_model
from models.visualization import plot_hr_diagram
import pandas as pd

def analyze_stars(dataset_path):
    # Load dataset
    data = pd.read_csv(dataset_path)

    # Plot HR Diagram
    plot_hr_diagram(data)

    # Train a simple classification model
    train_classification_model(data)

# Usage example:
if __name__ == "__main__":
    dataset_path = '../data/stars_dataset.csv'
    analyze_stars(dataset_path)
