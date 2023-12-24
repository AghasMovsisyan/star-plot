import sys
import argparse
import pandas as pd

# Add the parent directory to the Python path
sys.path.append('../')

# Import functions from modules
from src.star_type_classification.models.classification import train_classification_model
from src.star_type_classification.models.visualization import plot_hr_diagram

def analyze_stars(dataset_path):
    # Load dataset
    data = pd.read_csv(dataset_path)

    # Plot HR Diagram
    plot_hr_diagram(data)

    # Train a simple classification model
    train_classification_model(data)

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Analyze star data')

    # Add an argument for the dataset path
    parser.add_argument('dataset_path', type=str, help='Path to the stars dataset CSV file')

    # Parse the arguments
    args = parser.parse_args()

    # Run the analysis using the provided dataset path
    analyze_stars(args.dataset_path)
