from django.urls import path
from .views import  json_data_view

urlpatterns = [
    path('api/json-file/', json_data_view, name='json-file'),
]