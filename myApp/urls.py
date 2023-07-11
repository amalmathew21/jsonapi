from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

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
    path('api/ordoreports/', OrdoreportAPIView.as_view(), name='audioreports'),
    path('api/ordoreports/<int:pk>/', OrdoreportAPIView.as_view(), name='audioreports'),
    #path('api/opportunity/<int:opportunity_id>/photo/',views.opportunity_photo_view, name='opportunity_photo'),

    path('api/mymodules/',MymodelData.as_view(),name="mymodules"),
    path('api/leadsdata/',LeadsData.as_view(),name="leaddata"),
    path('api/accountsdata/',AccountsData.as_view(),name="accountsdata"),
    path('api/opportunitiesdata/',OpportunitiesData.as_view(),name="opportunitiesdata"),
    path('api/tasksdata/',TasksData.as_view(),name="tasksdata"),
    path('api/reportsdata/',ReportsData.as_view(),name="reportsdata"),
    path('api/notesdata/',NotesData.as_view(),name="notesdata"),
    path('api/ordoreportsdata/',OrdoReportData.as_view(),name="ordoreportsdata"),

    path('ordoreports/', OrdoreportListCreateView.as_view(), name='ordoreport-list-create'),
    path('reportview/<int:pk>/',views.your_view,name='reportlist'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)