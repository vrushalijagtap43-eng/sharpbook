from rest_framework import serializers

from sharptest.models import BaseModel,Brand

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= BaseModel
        fields= "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields= "__all__"