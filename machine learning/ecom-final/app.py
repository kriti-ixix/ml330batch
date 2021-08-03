#Importing the libraries
import pickle
from flask import Flask, request, json, jsonify
import numpy as np 


#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('ecommerce model.pkl', 'rb'))


#User defined functions
@app.route('/predict', methods=['POST'])
def prediction():
	print("Prediction function is called")


#Main function
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)