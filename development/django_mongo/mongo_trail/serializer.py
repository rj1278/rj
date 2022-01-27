from django.db.models import fields
from rest_framework import serializers
from . import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Members
        fields='__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Assets
        fields='__all__'
class MemberAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Member_Assets
        fields='__all__'
