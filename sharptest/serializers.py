from rest_framework import serializers
import re

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

    def validate_name(self, value):
        pattern = r'^[A-Z][a-zA-Z]*( [A-Z][a-zA-Z]*)*$'

        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Each word must start with a capital letter and contain only letters."
            )

        return value


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
