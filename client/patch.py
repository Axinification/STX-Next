import requests

endpoint = "https://stxnext-app.herokuapp.com/books/1"
response = requests.get(endpoint)
response = requests.patch(endpoint, json={
                                         "title": "Teścior",
                                         "authors": ["Axins"],
                                         "published_year": 2022,
                                         "acquired": True})
response = requests.get(endpoint)
print(response.json())
