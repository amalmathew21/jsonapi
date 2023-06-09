from django.http import JsonResponse
import json
from .serializers import MyModelSerializer
from .models import MyModel
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

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
        serializer = MyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved successfully.'})
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        if pk is not None:
            my_model = get_object_or_404(MyModel, pk=pk)
            data = json.loads(request.body)
            serializer = MyModelSerializer(my_model, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Data updated successfully.'})
            else:
                return JsonResponse(serializer.errors, status=400)
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


def image_data_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            image_model = get_object_or_404(ImageModel, pk=pk)
            serializer = ImageSerializer(image_model)
            return JsonResponse(serializer.data)
        else:
            image_models = ImageModel.objects.all()
            serializer = ImageSerializer(image_models, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        image = request.FILES.get('image')

        if not image:
            return JsonResponse({'message': 'No image provided.'}, status=400)

        image_data = {'json_data': data, 'image': image}
        serializer = ImageSerializer(data=image_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved successfully.'})
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        if pk is not None:
            image_model = get_object_or_404(ImageModel, pk=pk)
            data = json.loads(request.POST.get('data'))
            image = request.FILES.get('image')

            if not image:
                return JsonResponse({'message': 'No image provided.'}, status=400)

            image_data = {'json_data': data, 'image': image}
            serializer = ImageSerializer(image_model, data=image_data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Data updated successfully.'})
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    elif request.method == 'DELETE':
        if pk is not None:
            image_model = get_object_or_404(ImageModel, pk=pk)
            image_model.delete()
            return JsonResponse({'message': 'Data deleted successfully.'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request method.'})