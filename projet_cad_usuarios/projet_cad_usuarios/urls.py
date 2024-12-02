from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('responder_enquete/', views.responder_enquete, name='responder_enquete'),
]
