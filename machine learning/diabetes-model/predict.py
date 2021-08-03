#Importing the libraries
import json
import requests

#User input
bmi = input("Enter BMI: ")
age = input("Enter age: ")
glucose = input("Enter glucose: ")

#Sending the request
url = "http://127.0.0.1:5000/predict"
data = {'BMI':bmi, 'Age':age, 'Glucose':glucose}
dataJSON = json.dumps(data)
headers = {'Content-type': 'application/json'}

#Sending the request and getting the response
output = requests.post(url = url, data = dataJSON, headers = headers)
outputDict = json.loads(output.text)

#Printing the prediction
prediction = outputDict['prediction'] 
print("Diabetic" if prediction == 1 else "Not Diabetic")