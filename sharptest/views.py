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


    def post(self,request):
        serializer=BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            brand=Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response("not Found",status=status.HTTP_404_NOT_FOUND)
        serializer=BrandSerializer(brand,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)