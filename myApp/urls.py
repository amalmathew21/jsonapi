from django.urls import path
from .views import *

urlpatterns = [
    path('api/json-file/<int:pk>/', json_data_view, name='json-file'),
    path('api/json-file/', json_data_view,name='viewdata'),
    path('api/dropdown/', dropdown_dataview, name='dropdown-data-view'),
    path('api/dropdown/<int:pk>/', dropdown_dataview, name='dropdown-data-detail'),
    path('api/data/',data_view,name='jsondataview'),
    path('api/data/<int:pk>/',data_view,name='dataview'),
    path('api/leads/', LeadAPIView.as_view(), name='leads'),
    path('api/leads/<int:pk>/', LeadAPIView.as_view(), name='leadsdetails'),
    path('api/accounts/', AccountAPIView.as_view(), name='accounts'),
    path('api/accounts/<int:pk>/', AccountAPIView.as_view(), name='accountsdetails'),
    path('api/opportunities/', OpportunityAPIView.as_view(), name='opportunities'),
    path('api/opportunities/<int:pk>/', OpportunityAPIView.as_view(), name='opportunitiesdetails'),
    path('api/tasks/', TaskAPIView.as_view(), name='tasks'),
    path('api/tasks/<int:pk>/', TaskAPIView.as_view(), name='tasksdetails'),
    path('api/reports/', ReportAPIView.as_view(), name='reports'),
    path('api/reports/<int:pk>/', ReportAPIView.as_view(), name='reportsdetails'),
    path('api/notes/', NoteAPIView.as_view(), name='notes'),
    path('api/notes/<int:pk>/', NoteAPIView.as_view(), name='notes'),
]