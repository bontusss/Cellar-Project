from rest_framework import serializers
from . import models

class GovernorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Governor
        fields = '__all__'