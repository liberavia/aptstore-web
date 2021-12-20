from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('teaser/', views.teaser, name='api-teaser'),
    path('app/<int:appid>', views.details, name='api-details'),
]