from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Skill
from .serializers import SkillSerializer


class Register(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return Response({'message': 'User {} created successfully.'.format(username)})


class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)
