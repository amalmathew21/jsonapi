from django.http import JsonResponse
import json
from .serializers import MyModelSerializer
from .models import MyModel
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def json_data_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Assuming you receive the JSON data in the request body
        my_model = MyModel(json_file=data)
        my_model.save()
        return JsonResponse({'message': 'Data saved successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})
