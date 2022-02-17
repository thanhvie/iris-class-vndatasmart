import numpy as np
import joblib

iris_classes = ['Setosa', 'Versicolor', 'Virginica']

filename = 'model/iris_model.pkl'
multi_model = joblib.load(filename)


# Function for classification based on inputs
def classify(a, b, c, d):
    client_input = np.array([[a, b, c, d]])   # Convert to numpy array
    iris_pred = multi_model.predict(client_input)[0]   # Retrieve from dictionary
    prediction = 'Predicted class is ' + iris_classes[iris_pred]
    return prediction   # Return the prediction
