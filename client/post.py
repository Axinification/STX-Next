import requests

endpoint = "http://localhost:8000/books/"

response = requests.post(endpoint, json={
                                         "title": "Tibijska przygoda",
                                         "authors": ["Axins"],
                                         "published_year": 2020,
                                         "thumbnail": """http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1
&zoom=1&source=gbs_api"""
})

print(response.json())
