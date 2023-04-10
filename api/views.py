from django.shortcuts import render

from rest_framework import generics

from network.models import User, Following, Post
from .serializers import UserSerializer\
    #, FollowingSerializer, PostSerializer

# Create your views here.


class NetworkAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
