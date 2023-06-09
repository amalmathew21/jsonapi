from django.urls import path
from .views import json_data_view,image_data_view,data_view

urlpatterns = [
    path('api/json-file/<int:pk>/', json_data_view, name='json-file'),
    path('api/json-file/', json_data_view,name='viewdata'),
    path('api/image/', image_data_view, name='image-data-view'),
    path('api/image/<int:pk>/', image_data_view, name='image-data-detail'),
    path('api/data/',data_view,name='jsondataview'),
    path('api/data/<int:pk>/',data_view,name='dataview')

]