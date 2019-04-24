from django.urls import path
from web.endpoint import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'upload/', views.upload, name='upload'),
    path(r'star/', views.star, name='star'),
]
