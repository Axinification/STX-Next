import requests

endpoint = "http://localhost:8000/api/import"
query = "?q=inauthor=tolkien"
response = requests.post(endpoint)
print(response.json())
