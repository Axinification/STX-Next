import requests

endpoint = "http://localhost:8000/books/"
response = requests.get(endpoint)
print(response)
