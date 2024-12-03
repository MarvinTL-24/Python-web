from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
]

