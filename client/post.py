import requests

endpoint = "https://stxnext-app.herokuapp.com/books/"

response = requests.post(endpoint, json={
                                         "title": "Tibijska przygoda",
                                         "authors": ["Axins"],
                                         "published_year": 2018,
                                         "thumbnail": """http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1
&zoom=1&source=gbs_api"""
})

print(response.json())
