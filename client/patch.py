import requests

endpoint = "http://localhost:8000/books/1"
response = requests.get(endpoint)
response = requests.patch(endpoint, json={
                                         "title": "Teścior",
                                         "authors": ["Axins"],
                                         "published_year": 2022})
response = requests.get(endpoint)
print(response.json())
