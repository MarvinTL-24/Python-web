from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Configura a URL para a página inicial
]
