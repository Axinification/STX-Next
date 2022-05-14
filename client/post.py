import requests

endpoint = "http://localhost:8000/books/"

response = requests.post(endpoint, json={
                                         "title": "Tibijskie opowieści",
                                         "authors": ["Axins"],
                                         "published_year": "2022"})

print(response.json())
