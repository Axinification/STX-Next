import requests

endpoint = "https://stxnext-app.herokuapp.com/books/"
response = requests.get(endpoint)

print(response.json())
