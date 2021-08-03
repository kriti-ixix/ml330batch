import json
import requests

url = 'http://127.0.0.1:5000/'
data = {'hi':'hello'}
data_json = json.dumps(data)
headers = {'Content-Type':'application/json'}
requests.post(url, data=data_json, headers=headers)