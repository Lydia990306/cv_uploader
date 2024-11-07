from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload-cv/', views.upload_cv, name='upload_cv'),
    path('admin-view/', views.admin_view, name='admin_view'),  # For the admin to view all CVs
]
