from django.urls import path
from .views import register_view

app_name = 'doctor'

urlpatterns = [
    path('register/', register_view, name='register')
]
