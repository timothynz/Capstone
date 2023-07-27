#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
pipeline = joblib.load('capstone_pipe.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = pipeline.predict([data])
    return jsonify({'prediction': prediction.tolist()})

