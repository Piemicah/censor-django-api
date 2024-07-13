# from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from .serializers import PersonSerializer, UserSerializer
from censor.models import Persons


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
