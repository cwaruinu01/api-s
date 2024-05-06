from django.shortcuts import render, redirect
from django.template import loader
from django.http import JsonResponse, HttpResponse
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def application_list(request, format=None):
    if request.method == 'GET':
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)


def mpesa(request):
    template = loader.get_template('mpesa.html')
    return HttpResponse(template)
