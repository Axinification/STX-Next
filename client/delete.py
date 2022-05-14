import requests

endpoint = "http://localhost:8000/books/1"
response = requests.delete(endpoint)
print(response)
