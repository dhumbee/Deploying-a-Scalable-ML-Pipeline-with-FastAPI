import pytest
import numpy as np
from fastapi.testclient import TestClient
import json
from main import app
from sklearn.metrics import accuracy_score
from ml.model import train_model, inference
from train_model import X_train, y_train

client = TestClient(app)

# TODO: implement the first test. Change the function name and input as needed
def test_api_get():
    """
    # test the connection to the api
    """
    r = client.get("/")
    print(r.json())
    assert r.status_code == 200


# TODO: implement the second test. Change the function name and input as needed
def test_model_type():
    """
    # test that the train_model returns a Random Forest Classifier
    """
    model = train_model(X_train,y_train)  
    expected_algorithm = 'RandomForestClassifier' 
    assert type(model).__name__ == expected_algorithm, f"Expected {expected_algorithm}, {type(model).__name__} actual"


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    # test inference - confirm length is the same as the x_train - and the data quality
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert len(preds) == len(X_train) 
    assert np.all((preds==0)|(preds == 1)) == True
