from django.shortcuts import render
from sharptest import serializers
from rest_framework.views import APIView
from rest_framework import status
from sharptest.models import BaseModel,Brand,ServiceCategory,Package,Product,Review,Store
from sharptest.serializers import BaseModelSerializer,BrandSerializer,ServiceSerializer,PackageSerializer,ProductSerializer,ReviewSerializer,StoreSerializer

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


    def delete(self,request,id):
        try:
            brand=Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response("not found",status=status.HTTP_404_NOT_FOUND)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServicecatogaryCrud(APIView):

    def get(self,request):
        service=ServiceCategory.objects.all()
        serializer=ServiceSerializer(service,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

class PackageCrud(APIView):
    # def get(self,request):
    #     package=Package.objects.all()
    #
    #     serializer=PackageSerializer(package,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    # def get(self, request):
    #     search = request.query_params.get("search")
    #
    #     if search:
    #         package = Package.objects.filter(name__icontains = search)
    #     else:
    #         package =Package.objects.all()
    #         print("Hiiiii")
    #
    #     serializer = PackageSerializer(package, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self,request):
        search = request.query_params.get("search")
        brand_id = request.query_params.get("brand_id")

        package = Package.objects.all()

        if search:
            package = package.filter(name__icontains = search)
        if brand_id:
            package =package.filter(brand_id = brand_id)

        serializers = PackageSerializer(package,many = True)
        return Response(serializers.data,status = status.HTTP_200_OK)

    def post(self,request):
        serializer=PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,id):
        try:
            package=Package.objects.get(id=id)
        except Package.DoesNotExist:
            return Response("not exist",status=status.HTTP_404_NOT_FOUND)
        serializer=PackageSerializer(package,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ProductCrud(APIView):

    def get(self,request):
        product=Product.objects.all()
        serializer=PackageSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response("status not found",status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ReviewCrud(APIView):

    def get(self,request):
        review=Review.objects.all()
        serializer=ReviewSerializer(review,many=True)
        return Response(serializer.data)


class StoreCrud(APIView):

    def get(self,request):
        store=Store.objects.all()
        serialiazr=StoreSerializer(store,many=True)
        return Response(serialiazr.data)


    def post(self,request):
        serializer=StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            store=Store.objects.get(id=id)
        except Store.DoesNotExist:
            return Response("not found",status=status.HTTP_400_BAD_REQUEST)
        serializer=StoreSerializer(store,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,id):
        try:
            store=Store.objects.get(id=id)
        except Store.DoesNotExist:
            return Response('not found',status=status.HTTP_400_BAD_REQUEST)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





