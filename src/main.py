import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def analyze_stars(dataset_path):
    # Load dataset
    data = pd.read_csv(dataset_path)

    # Plot HR Diagram
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Temperature (K)'], data['Absolute magnitude(Mv)'], c=data['Star type'])
    plt.xlabel('Temperature (K)')
    plt.ylabel('Absolute Magnitude')
    plt.title('HR Diagram')
    plt.colorbar(label='Star Type')
    plt.savefig('hr_diagram.png')
    plt.show()

    # Train a simple classification model
    X = data[['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)']]
    y = data['Star type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

# Usage example:
if __name__ == "__main__":
    dataset_path = '../data/stars_dataset.csv'
    analyze_stars(dataset_path)
