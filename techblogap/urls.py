from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home),
    path('author/', views.author),
    path('category01/', views.category01),
    path('category02/', views.category02),
    path('category03/', views.category03),
    path('contact/', views.contact),
    path('single/', views.single),
    
]