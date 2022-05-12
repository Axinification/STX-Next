import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
endpoint = "http://localhost:8000/api/books"

response = requests.get(endpoint)

print(response)
