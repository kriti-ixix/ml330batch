#Importing the libraries
import json 
import requests

#Getting the input from the user
bmi = input("Enter BMI: ")
age = input("Enter age: ")
glucose = input("Enter glucose: ")

#Creating the request for the API
#1. URL     2. Data     3. Header
url = "http://127.0.0.1:5000/"
data = {"bmi":bmi, "age":age, "glucose":glucose}
dataJSON = json.dumps(data)
headers = {"Content-type":"application/json"}

#Sending the request
response = requests.post(url=url, data=dataJSON, headers=headers)
output = json.loads(response.text)

prediction = output['prediction']
print("Diabetic" if prediction == 1 else "Not Diabetic")