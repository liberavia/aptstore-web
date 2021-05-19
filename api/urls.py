from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('app/<int:appid>', views.details, name='api-details'),
]