from rest_framework import serializers
from ..bread.models import Bread

class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = ("id", "name", "description", "bread_type")