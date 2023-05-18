from django.http import JsonResponse
import json
from .serializers import MyModelSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def json_data_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Assuming you receive the JSON data in the request body
        serializer = MyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved successfully.'})
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method.'})