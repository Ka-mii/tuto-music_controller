# Rôle : Définit les routes (ou URL) de l'application et mappe ces URL à des vues spécifiques.
# Contenu :
# - URL Patterns : Utilise urlpatterns pour mapper les URL aux vues.
# - Inclut les routes des applications : Utilise include pour inclure les routes des applications.

"""
URL configuration for music_controller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # si domain.com/admin, ça va rediriger vers admin.site.urls qui va gérer l'affichage de la page
    path('api/', include('api.urls')), # redirige tous les urls '' vers le module urls de api
    path('', include('frontend.urls'))
]
