import requests

endpoint = "https://stxnext-app.herokuapp.com/books/1"
response = requests.delete(endpoint)
print(response)
