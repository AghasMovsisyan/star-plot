from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_classification_model(data):
    X = data[['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)']]
    y = data['Star type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define hyperparameters for grid search
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [None, 5, 10, 15]
    }

    # Create a RandomForestClassifier
    clf = RandomForestClassifier(random_state=42)

    # Perform GridSearchCV
    grid_search = GridSearchCV(clf, param_grid, cv=5)
    grid_search.fit(X_train, y_train)

    # Get the best estimator
    best_clf = grid_search.best_estimator_

    # Train with the best estimator
    best_clf.fit(X_train, y_train)

    # Predict on test set
    y_pred = best_clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
