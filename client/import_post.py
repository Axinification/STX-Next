import requests

endpoint = "https://stxnext-app.herokuapp.com/import/"
# endpoint = "http://localhost:8000/import/"

response = requests.post(endpoint, json={"author": "chmielewska"})

print(response.json())
