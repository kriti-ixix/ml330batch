#Importing the libraries
import pickle
import numpy as np
from flask import Flask, request, json, jsonify  


#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('diabetes.sav', 'rb'))


#User defined functions
@app.route('/', methods=['POST'])
def predict():
    #Getting the input from the request
    userInput = request.json
    inputList = [userInput['glucose'], userInput['bmi'], userInput['age']]

    #Making predictions
    prediction = loadedModel.predict([inputList])
    confidence = loadedModel.predict_proba([inputList])

    #Returning the predictions
    response = {}
    response['prediction'] = int(prediction[0])
    #response['confidence'] = str(round(np.amax(confidence[0]) * 100, 2))
    
    return jsonify(response)

#Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
