from joblib import load
from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
import json
model = load('.joblib')

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("home.html")


@app.route('/predict', methods = ['POST'])
def predict():
    #request of all inputs
    features = [x for x in request.form.values()]
    
    #data preparing
    features_array = np.array(features)
    pandas_features = pd.DataFrame([features_array])
    print(features)
    
    #predict
    result = linregre.predict(pandas_features)
    print(result)
    prediction = float(result[0])
    return render_template("home.html", result = "prediction: {}".format(prediction))

@app.route('/model_health/<model_id>', methods = ['GET'])
def model_health(model_id):
    with open('model_metrics_version_{0}.json'.format(model_id)) as f:
        model_metrics = json.load(f)    
        return model_metrics

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80)
