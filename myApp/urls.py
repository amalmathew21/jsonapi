from django.urls import path
from .views import json_data_view,image_data_view

urlpatterns = [
    path('api/json-file/<int:pk>/', json_data_view, name='json-file'),
    path('data', json_data_view,name='viewdata'),
    path('api/image/', image_data_view, name='image-data-view'),
    path('image/<int:pk>/', image_data_view, name='image-data-detail'),
]