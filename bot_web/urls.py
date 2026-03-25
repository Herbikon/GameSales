from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('api/message/', views.messages, name='messages'),

]
