from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()) # si url est vide, ça va appeler la fonction main qui va revoyer une réponse HTTP
]
