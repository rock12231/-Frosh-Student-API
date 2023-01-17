from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from API.serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
class UserList(APIView):

    def get(self, request, format=None):
        userHist = User.objects.all()
        serializer = UserSerializer(userHist, many=True)
        return Response(serializer.data)
