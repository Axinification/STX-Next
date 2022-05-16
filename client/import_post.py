import requests

endpoint = "http://localhost:8000/import/"

response = requests.post(endpoint, json={"author": "tolkien"})

print(response.json())
