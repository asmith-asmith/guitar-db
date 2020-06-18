from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('guitars/', views.guitar_index, name="index"),
    path('guitars/<int:guitar_id>/', views.guitar_details, name="detail"),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitar_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitar_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitar_delete'),
    path('guitars/<int:guitar_id>/add_variations/', views.add_variations, name='add_variations'),
]