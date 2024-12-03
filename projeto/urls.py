from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Mantém o painel administrativo
    path('', include('home.urls')),  # Define a página inicial para o app "home"
]
