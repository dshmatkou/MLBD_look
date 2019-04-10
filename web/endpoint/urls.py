from django.urls import path
from web.endpoint import views

urlpatterns = [
    path(r'endpoint/', views.endpoint, name='endpoint'),
]
