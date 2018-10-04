from rest_framework import serializers
from .models import Namelist

class NamelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Namelist
        fields = '__all__'