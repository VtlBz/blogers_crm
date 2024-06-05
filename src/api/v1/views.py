from django.http import JsonResponse
from rest_framework import status


def healthcheck_status(request):
    data = {"status": "healthy"}
    return JsonResponse(data, status=status.HTTP_200_OK)
