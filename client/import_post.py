import requests

endpoint = "https://stxnext-app.herokuapp.com/import/"

response = requests.post(endpoint, json={"author": "nazwisko"})

print(response.json())
