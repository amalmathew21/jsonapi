from django.http import JsonResponse
import json
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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
def image_data_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            image = get_object_or_404(Image, pk=pk)
            serializer = ImageSerializer(image)
            return JsonResponse(serializer.data)
        else:
            images = Image.objects.all()
            serializer = ImageSerializer(images, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        image = request.FILES.get('image')

        if not image:
            return JsonResponse({'message': 'No image provided.'}, status=400)

        image_data = {'image': image}
        serializer = ImageSerializer(image=image_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved successfully.'})
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        if pk is not None:
            image = get_object_or_404(Image, pk=pk)
            new_image = request.FILES.get('image')

            if not new_image:
                return JsonResponse({'message': 'No image provided.'}, status=400)

            image.image = new_image
            image.save()

            return JsonResponse({'message': 'Data updated successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    elif request.method == 'DELETE':
        if pk is not None:
            image = get_object_or_404(Image, pk=pk)
            image.delete()
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


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def lead_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            lead = Leads.objects.get(pk=pk)
            serializer = LeadsSerializer(lead)
            return Response(serializer.data)
        else:
            leads = Leads.objects.all()
            serializer = LeadsSerializer(leads, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data  # Assuming you are sending the JSON data in the request body
        serializer = LeadsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        lead = Leads.objects.get(pk=pk)
        data = request.data
        serializer = LeadsSerializer(lead, data=data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lead = Leads.objects.get(pk=pk)
        lead.delete()
        return Response({'message': 'Data deleted successfully.'})

    else:
        return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


