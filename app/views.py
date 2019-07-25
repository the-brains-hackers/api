from django.shortcuts import render
from rest_framework import generics
from .models import UserInfo
from .serializers import UserInfoSerializer

# Create your views here.


class UserInfoList(generics.ListCreateAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
