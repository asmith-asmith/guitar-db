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
    #one to many no need to associate
    path('guitars/<int:guitar_id>/add_variations/', views.add_variations, name='add_variations'),
    # many to many must write code to associate + unassociate
    path('guitar/<int:guitar_id>/assoc_guitarist/<int:guitarist_id>/', views.assoc_guitarist, name='assoc_guitarist'),
    path('guitar/<int:guitar_id>/unassoc_guitarist/<int:guitarist_id>/', views.unassoc_guitarist, name='unassoc_guitarist'),
    path('guitarists/create/', views.GuitaristCreate.as_view(), name='guitarist_create'),
    path('guitarists/', views.GuitaristList.as_view(), name='guitarist_index'),
    path('guitarists/<int:pk>/', views.GuitaristDetail.as_view(), name='guitarist_detail'),
    path('giutarists/<int:pk>/delete/', views.GuitaristDelete.as_view(), name='guitarist_delete'),
    path('giutarists/<int:pk>/update/', views.GuitaristUpdate.as_view(), name='guitarist_update'),

]