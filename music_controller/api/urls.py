from django.urls import path
from .views import main

urlpatterns = [
    path('', main) # si url est vide, ça va appeler la fonction main qui va revoyer une réponse HTTP
]
