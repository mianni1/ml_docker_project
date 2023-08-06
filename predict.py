import numpy as np
import joblib

def load_and_predict():
    # Load model
    model = joblib.load('model.joblib')

    # Predict the class of a new sample
    # Random sample for demonstration purposes
    sample = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)
    prediction = model.predict(sample)

    print(f'Prediction for the sample is: {prediction}')

if __name__ == '__main__':
    load_and_predict()
