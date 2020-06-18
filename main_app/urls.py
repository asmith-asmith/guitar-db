from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('guitars/', views.guitar_index, name="index"),
    path('guitars/<int:guitar_id>/', views.guitar_details, name="detail"),
]