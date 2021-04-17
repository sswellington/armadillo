import requests
import json

url = 'https://api.escavador.com/api/v1/request-token'

payload = {
     'username': 'meuemail@email.com',  
    'password': 'minha_senha'  
}

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json'
}

response = requests.request('POST', url, headers=headers, json=payload)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4))