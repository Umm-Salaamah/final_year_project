from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scan_results/', views.scan_results, name='scan_results'),
    
]
