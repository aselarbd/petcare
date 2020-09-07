from rest_framework import serializers
from .models import PetCareUser


class PetCareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetCareUser
        fields = ['email']
