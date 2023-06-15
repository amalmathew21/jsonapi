from django.http import JsonResponse
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


# @csrf_exempt
# def image_data_view(request, pk=None):
#     if request.method == 'GET':
#         if pk is not None:
#             image = get_object_or_404(Image, pk=pk)
#             serializer = ImageSerializer(image)
#             return JsonResponse(serializer.data)
#         else:
#             images = Image.objects.all()
#             serializer = ImageSerializer(images, many=True)
#             return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         image = request.FILES.get('image')
#
#         if not image:
#             return JsonResponse({'message': 'No image provided.'}, status=400)
#
#         image_data = {'image': image}
#         serializer = ImageSerializer(image=image_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Data saved successfully.'})
#         else:
#             return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'PUT':
#         if pk is not None:
#             image = get_object_or_404(Image, pk=pk)
#             new_image = request.FILES.get('image')
#
#             if not new_image:
#                 return JsonResponse({'message': 'No image provided.'}, status=400)
#
#             image.image = new_image
#             image.save()
#
#             return JsonResponse({'message': 'Data updated successfully.'})
#         else:
#             return JsonResponse({'message': 'Invalid request.'}, status=400)
#
#     elif request.method == 'DELETE':
#         if pk is not None:
#             image = get_object_or_404(Image, pk=pk)
#             image.delete()
#             return JsonResponse({'message': 'Data deleted successfully.'})
#         else:
#             return JsonResponse({'message': 'Invalid request.'}, status=400)
#
#     else:
#         return JsonResponse({'message': 'Invalid request method.'})

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
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=400)

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
            serializer.save()
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
            serializer.save()
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
