import pandas as pd
import matplotlib.pyplot as plt
from models.classification_model import train_classification_model

def plot_hr_diagram(data):
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Temperature (K)'], data['Absolute magnitude(Mv)'], c=data['Star type'])
    plt.xlabel('Temperature (K)')
    plt.ylabel('Absolute Magnitude')
    plt.title('HR Diagram')
    plt.colorbar(label='Star Type')
    plt.savefig('hr_diagram.png')
    plt.show()

def main():
    # Load dataset
    data = pd.read_csv('data/stars_dataset.csv')

    # Plot HR Diagram
    plot_hr_diagram(data)

    # Train classification models
    clf, accuracy = train_classification_model(data)
    print(f'Accuracy: {accuracy}')

if __name__ == "__main__":
    main()
