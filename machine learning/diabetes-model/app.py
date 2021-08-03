#Importing the libraries
import pickle
from flask import Flask, request, json, jsonify
import numpy as np

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('diabetes.sav', 'rb'))

#User defined functions
@app.route('/predict', methods=['POST'])
def predict():
    userInput  = request.json
    bmi = userInput['BMI']
    age = userInput['Age']
    glucose = userInput['Glucose']

    prediction = loadedModel.predict([[glucose, bmi, age]])[0]

    userOutput = {'prediction': int(prediction)}
    return jsonify(userOutput)

#Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)