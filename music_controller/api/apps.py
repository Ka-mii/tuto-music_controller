# Rôle : Contient la configuration de l'application.
# Contenu : Définit une classe qui hérite de AppConfig. Cette classe est utilisée pour configurer certains aspects de l'application, comme son nom.

from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
