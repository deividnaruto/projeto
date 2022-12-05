from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name = 'homepage'),
    path('loguin/',views.loguin, name= 'loguin'), 
    path('cadastrar/',views.cadastro, name= 'cadastro'),
    path('videos/',views.videos, name= 'videos'), 
    path('logout/',views.logout, name= 'logout'), 
]
