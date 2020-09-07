from rest_framework import serializers
from .models import ClinicBase, Vet, Availability, TakenSlots


class ClinicBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicBase
        fields = ['clinicID', 'clinicName', '_created_at']


class VetBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = ['vetID', 'vetName', '_created_at']


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['availabilityID', 'dateAndTime', '_created_at']


class TakenSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenSlots
        fields = ['takenID', 'vetID', 'clinicID', 'availabilityID', '_created_at']
