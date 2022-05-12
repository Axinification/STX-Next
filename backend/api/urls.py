from django.urls import path

from .views import books, imports

urlpatterns = [
    path('books/', books),
    path('import/', imports)
]
