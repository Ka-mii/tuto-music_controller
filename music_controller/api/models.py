# Rôle : Utilisé pour définir les modèles de l'application. Un modèle représente une table dans la base de données.
# Contenu : Contient des classes qui définissent la structure des données, les champs et les comportements des modèles.

from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count == 0: # all Room object
            break
    return code

# Create your models here.
class Room(models.Model): # C'est un modèle
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False) # permission guest peut ou pas pause la musique, peut pas être null
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)