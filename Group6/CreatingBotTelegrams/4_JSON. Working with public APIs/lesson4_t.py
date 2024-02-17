import requests

response = requests.get('https://cataas.com/cat?json=true').json()
print(response)