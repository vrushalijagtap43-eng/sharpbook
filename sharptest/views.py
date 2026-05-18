from django.shortcuts import render
from sharptest import serializers
from rest_framework.views import APIView
from rest_framework import status
from sharptest.models import BaseModel,Brand
from sharptest.serializers import BaseModelSerializer,BrandSerializer

from  rest_framework.response import Response
# Create your views here.

class SharpBookCrud(APIView):

    def get(self,request):
        brand=Brand.objects.all()
        serializer=BrandSerializer(brand,many= True)
        return Response(serializer.data,status=status.HTTP_200_OK)
