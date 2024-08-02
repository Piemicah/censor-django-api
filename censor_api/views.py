# from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from .serializers import PersonSerializer, UserSerializer
from censor.models import Persons
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView


class PersonListCreate(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Persons.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return super().perform_create(serializer)


class PersonRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Persons.objects.all()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


tokens = {"token": "", "refresh": "", "user": ""}


class SaveApi(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(tokens)

    def post(self, request):
        token = request.data["token"]
        refresh = request.data["refresh"]
        user = request.data["user"]
        tokens["token"] = token
        tokens["refresh"] = refresh
        tokens["user"] = user
        return Response({"status": "success"})


class Logout(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        tokens["token"] = ""
        tokens["refresh"] = ""
        tokens["user"] = ""
        return Response({"status": "success"})
