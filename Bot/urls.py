from django.urls import path
from . import views , controller

urlpatterns = [
    path('', views.index),
    path('CO', controller.index),
]
