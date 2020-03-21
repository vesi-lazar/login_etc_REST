from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from .serializers import UserCreateSerializer
# Create your views here.

class RegisterUser(views.APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)