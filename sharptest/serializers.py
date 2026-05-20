from rest_framework import serializers

from sharptest.models import BaseModel,Brand,ServiceCategory,Package,Product,Review,Store

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= BaseModel
        fields= "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields= "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceCategory
        fields="__all__"


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Store
        fields="__all__"
