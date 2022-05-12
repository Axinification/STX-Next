import json
from django.http import JsonResponse


def books(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse({"message": "JsonResponse"})


def imports(request, *args, **kwargs):
    pass
