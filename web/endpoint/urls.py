from django.urls import path
from web.endpoint import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(r'upload/', views.UploadView.as_view(), name='upload'),
    path(r'star/', views.StarView.as_view(), name='star'),
]
