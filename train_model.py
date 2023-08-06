from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_and_save_model():
    # Load dataset
    iris = load_iris()
    X = iris['data']
    y = iris['target']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    # Print accuracy
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f'Accuracy: {accuracy}')

    # Save model
    joblib.dump(model, 'model.joblib')

if __name__ == '__main__':
    train_and_save_model()
