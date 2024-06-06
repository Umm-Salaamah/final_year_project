from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    
    # path("login", views.login_view, name="login"),
    path("index", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path('scan_results/', views.scan_results, name='scan_results'),
    #path('previous_scans/', views.previous_scans, name='previous_scans'),
    
]
