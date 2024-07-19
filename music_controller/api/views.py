# Rôle : Contient les vues de l'application. Une vue est une fonction ou une classe qui traite une requête HTTP et retourne une réponse HTTP. Contient tous les endpoints : endroit sur le site (après le /)
# Contenu : Définit des fonctions ou des classes qui déterminent la logique de traitement des requêtes et la génération des réponses.

from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# Cette fonction prend en argument un objet request (qui représente une requête HTTP) et renvoie une réponse HTTP contenant le texte "Hello".
# une reqûete HHTP : 
# - Ligne de requête : Contient le type de requête (méthode), l'URL de la ressource demandée, et la version du protocole HTTP. 
# GET /index.html HTTP/1.1
# - En-têtes de requête : Fournissent des informations supplémentaires sur la requête ou sur le client.
# Host: www.example.com
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive

# RoomView renvoie une réponse HTTP contenant une vue qui affiche toutes les instances du modèle Room sous forme de JSON sérialisé, incluant les champs spécifiés dans le RoomSerializer.
class RoomView(generics.ListAPIView): 
    queryset = Room.objects.all() # Définit la requête de base qui récupère toutes les instances du modèle Room depuis la base de données.
    serializer_class = RoomSerializer # Spécifie le sérialiseur RoomSerializer qui convertit les instances du modèle Room en données JSON.