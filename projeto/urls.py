from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Mantém o painel administrativo
    path('', views.home, name='home.html')  # Define a rota raiz como página inicial
]
