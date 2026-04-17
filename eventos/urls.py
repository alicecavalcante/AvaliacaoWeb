from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('novo/', views.novo, name='novo'),
]