import requests
import json

URL = 'http://127.0.0.1:8000/studcreate/'

d={'name':'jairuddin','roll':105,'city':'Mumbai'}
json_data=json.dumps(d)
r = requests.post(url = URL, data=json_data)

data = r.json()

print(data)