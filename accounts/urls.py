from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('register/', views.RegisterUser.as_view(), name='register'),
]