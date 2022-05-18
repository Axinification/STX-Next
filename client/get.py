import requests

endpoint = "https://stxnext-app.herokuapp.com/post/"
response = requests.get(endpoint)

print(response.json())
