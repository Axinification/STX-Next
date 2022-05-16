import requests

endpoint = "http://localhost:8000/import/"

response = requests.post(endpoint, json={"author": "Tolkien"})

print(response.json())
