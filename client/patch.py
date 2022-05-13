import requests

endpoint = "http://localhost:8000/books/5"
response = requests.get(endpoint)
response = requests.patch(endpoint, json={
                                         "title": "Teścior666",
                                         "authors": "[Axins]",
                                         "published_year": "2022"})
response = requests.get(endpoint)
print(response.json())
