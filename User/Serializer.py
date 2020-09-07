from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userID', 'firstName', 'lastName', 'contactNo', 'petName', '_created_at']
