from rest_framework import serializers

from sharptest.models import BaseModel,Brand,ServiceCategory

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
