from django.http import JsonResponse, Http404
import json
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.http import HttpResponse


@csrf_exempt
def json_data_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            my_model = get_object_or_404(MyModel, pk=pk)
            serializer = MyModelSerializer(my_model)
            return JsonResponse(serializer.data)
        else:
            my_models = MyModel.objects.all()
            serializer = MyModelSerializer(my_models, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)  # Assuming you receive the JSON data in the request body
        my_model = MyModel(json_file=data)
        my_model.save()
        return JsonResponse({'message': 'Data saved successfully.'})

    elif request.method in ['PATCH', 'PUT']:
        if pk is not None:
            my_model = get_object_or_404(MyModel, pk=pk)
            data = json.loads(request.body)
            my_model.json_file = data
            my_model.save()
            return JsonResponse({'message': 'Data updated successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    elif request.method == 'DELETE':
        if pk is not None:
            my_model = get_object_or_404(MyModel, pk=pk)
            my_model.delete()
            return JsonResponse({'message': 'Data deleted successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request method.'})



@csrf_exempt
def data_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            my_model = get_object_or_404(DataModel, pk=pk)
            serializer = DataModelSerializer(my_model)
            return JsonResponse(serializer.data)
        else:
            my_models = DataModel.objects.all()
            serializer = DataModelSerializer(my_models, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)  # Assuming you receive the JSON data in the request body
        my_model = DataModel(json_data=data)
        my_model.save()
        return JsonResponse({'message': 'Data saved successfully.'})

    elif request.method in ['PATCH', 'PUT']:
        if pk is not None:
            my_model = get_object_or_404(DataModel, pk=pk)
            data = json.loads(request.body)
            my_model.json_data = data
            my_model.save()
            return JsonResponse({'message': 'Data updated successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    elif request.method == 'DELETE':
        if pk is not None:
            my_model = get_object_or_404(DataModel, pk=pk)
            my_model.delete()
            return JsonResponse({'message': 'Data deleted successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request method.'})


@csrf_exempt
def dropdown_dataview(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            my_model = get_object_or_404(DropdownModel, pk=pk)
            serializer = DropdownSerializer(my_model)
            return JsonResponse(serializer.data)
        else:
            my_models = DropdownModel.objects.all()
            serializer = DropdownSerializer(my_models, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)  # Assuming you receive the JSON data in the request body
        my_model = DropdownModel(json_data=data)
        my_model.save()
        return JsonResponse({'message': 'Data saved successfully.'})

    elif request.method in ['PATCH', 'PUT']:
        if pk is not None:
            my_model = get_object_or_404(DropdownModel, pk=pk)
            data = json.loads(request.body)
            my_model.json_data = data
            my_model.save()
            return JsonResponse({'message': 'Data updated successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    elif request.method == 'DELETE':
        if pk is not None:
            my_model = get_object_or_404(DropdownModel, pk=pk)
            my_model.delete()
            return JsonResponse({'message': 'Data deleted successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request method.'})


class LeadAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        lead = self.get_object(pk)
        serializer = LeadsSerializer(lead)
        return Response(serializer.data)

    def put(self, request, pk):
        lead = self.get_object(pk)
        serializer = LeadsSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        lead = self.get_object(pk)
        serializer = LeadsSerializer(lead, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        lead = self.get_object(pk)
        lead.delete()
        return Response({'message': 'Data deleted successfully.'})


class AccountAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Accounts.objects.get(pk=pk)
        except Accounts.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountsSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountsSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountsSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        account = self.get_object(pk)
        account.delete()
        return Response({'message': 'Data deleted successfully.'})


class OpportunityAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = OpportunitySerializer(data=request.data)
        if serializer.is_valid():
            opportunity = serializer.save()

            profile_photo = request.FILES.get('profilePhoto')
            if profile_photo:
                image_format = imghdr.what(None, h=profile_photo.read())
                file_extension = image_format if image_format else 'jpg'
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                file_name = f'opportunity_photos/{opportunity.opportunityId}_{random_string}.{file_extension}'
                opportunity.profilePhoto.save(file_name, profile_photo, save=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Opportunities.objects.get(pk=pk)
        except Opportunities.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        opportunity = self.get_object(pk)
        serializer = OpportunitySerializer(opportunity)
        return Response(serializer.data)


    def put(self, request, pk):
        opportunity = self.get_object(pk)
        serializer = OpportunitySerializer(opportunity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)


    def patch(self, request, pk):
        opportunity = self.get_object(pk)
        serializer = OpportunitySerializer(opportunity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)


    def delete(self, request, pk):
        opportunity = self.get_object(pk)
        opportunity.delete()
        return Response({'message': 'Data deleted successfully.'})


class TaskAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
           
            profile_pic = request.FILES.get('profilePic')
            serializer.save(profilePic=profile_pic)  # Pass the file to the serializer
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = TasksSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({'message': 'Data deleted successfully.'})


class ReportAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        report = self.get_object(pk)
        report.delete()
        return Response({'message': 'Data deleted successfully.'})


class NoteAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():

            profile_photo = request.FILES.get('profilePhoto')
            serializer.save(profilePhoto=profile_photo)  # Pass the file to the serializer
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        notes = self.get_object(pk)
        serializer = NotesSerializer(notes)
        return Response(serializer.data)

    def put(self, request, pk):
        notes = self.get_object(pk)
        serializer = NotesSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        notes = self.get_object(pk)
        serializer = NotesSerializer(notes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        notes = self.get_object(pk)
        notes.delete()
        return Response({'message': 'Data deleted successfully.'})


class OrdoreportAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = OrdoReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Ordo_Report.objects.get(pk=pk)
        except Ordo_Report.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = OrdoReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        serializer = OrdoReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        report = self.get_object(pk)
        serializer = OrdoReportSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        report = self.get_object(pk)
        report.delete()
        return Response({'message': 'Data deleted successfully.'})


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Opportunities


# def opportunity_photo_view(request, opportunity_id):
#
#     opportunity = get_object_or_404(Opportunities, opportunityId=opportunity_id)
#
#
#     profile_photo = opportunity.profilePhoto
#
#
#     if profile_photo and profile_photo.storage.exists(profile_photo.name):
#
#         with profile_photo.storage.open(profile_photo.name, 'rb') as file:
#             # Set the appropriate response headers
#             response = HttpResponse(file.read(), content_type='image/jpeg')
#
#
#             return response
#     else:
#
#         return HttpResponse("Profile photo not found.", status=404)


class MymodelData(APIView):
    def get(self, request):
        mymodel = MyModel.objects.all()
        serializer = MyModelSerializer(mymodel, many=True)
        return Response(serializer.data)

class LeadsData(APIView):
    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadsSerializer(leads, many=True)
        return Response(serializer.data)


class AccountsData(APIView):
    def get(self, request):
        accounts = Accounts.objects.all()
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)


class OpportunitiesData(APIView):
    def get(self, request):
        opportunity = Opportunities.objects.all()
        serializer = OpportunitySerializer(opportunity, many=True)
        return Response(serializer.data)


class TasksData(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)


class ReportsData(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportsSerializer(reports, many=True)
        return Response(serializer.data)


class NotesData(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)


class OrdoReportData(APIView):
    def get(self, request):
        reports = Ordo_Report.objects.all()
        serializer = OrdoReportSerializer(reports, many=True)
        return Response(serializer.data)

from rest_framework import generics
class OrdoreportListCreateView(generics.ListCreateAPIView):
    queryset = Ordo_Report.objects.all()
    serializer_class = OrdoReportSerializer

    def get(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)


from django.http import JsonResponse
from django.apps import apps

def your_view(request,pk):
    ordoreport = Ordo_Report.objects.get(id=pk)
    primary_module_model = apps.get_model(app_label='myApp', model_name=ordoreport.primaryModule)
    primary_module_instances = primary_module_model.objects.all()

    field_values = {}
    for field_data in ordoreport.fields:
        field_name = field_data["fieldName"]
        if hasattr(primary_module_model, field_name):
            field_values[field_name] = [getattr(instance, field_name) for instance in primary_module_instances]

    response_data = {
        # "id": ordoreport.id,
        # "assignedTo": ordoreport.assignedTo,
        # "chartType": ordoreport.chartType,
        # "description": ordoreport.description,
        # "fields": ordoreport.fields,
        # "groupByField": ordoreport.groupByField,
        # "groupByLabel": ordoreport.groupByLabel,
        # "name": ordoreport.name,
        # "primaryModule": ordoreport.primaryModule,
        # "summaryField": ordoreport.summaryField,
        # "summaryLabel": ordoreport.summaryLabel,
        # "sortBy": ordoreport.sortBy,
        "field_values": field_values
    }

    return JsonResponse(response_data)



class CreateUserList(generics.ListCreateAPIView):
    queryset = createUser.objects.all()
    serializer_class = CreateUserSerializer

class CreateUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = createUser.objects.all()
    serializer_class = CreateUserSerializer

class CreateUserView(generics.ListCreateAPIView):
    queryset = createUser.objects.all()
    serializer_class = CreateUserSerializer

    def get(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)
