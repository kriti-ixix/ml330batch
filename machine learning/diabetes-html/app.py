#Importing the libraries
from flask import Flask, request, render_template
import requests
import numpy as np
import pickle


#Setting up the API
app = Flask(__name__)
loadedModel = pickle.load(open('diabetes.sav', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')    


@app.route('/diagnosis', methods=['POST'])
def diagnose():
    
    bmi = int(request.form['bmi'])
    age = int(request.form['age'])
    glucose = int(request.form['glucose'])

    prediction = loadedModel.predict([[glucose,bmi,age]])[0]
    probability = loadedModel.predict_proba([[glucose,bmi,age]])

    probability = str(round(np.amax(probability)*100, 2))

    return render_template('index.html', prediction_output=prediction, probability_output=probability)


if __name__ == '__main__':
    app.run(debug=True)