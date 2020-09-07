from .Serializer import VetBaseSerializer, AvailabilitySerializer, ClinicBaseSerializer, TakenSlotsSerializer
from .models import Vet, Availability, ClinicBase, TakenSlots


# Clinic table service

class ClinicBaseService:

    @staticmethod
    def getAll():
        clinic = ClinicBase.objects.all()
        serializer = ClinicBaseSerializer(clinic, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        serializer = ClinicBaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    @staticmethod
    def getUserByID(request, ID):
        try:
            clinic = ClinicBase.objects.get(pk=ID)
        except ClinicBase.DoesNotExist:
            pass
        serializer = ClinicBaseSerializer(clinic)
        return serializer.data


# Vet table service

class VetService:

    @staticmethod
    def getAll():
        vet = Vet.objects.all()
        serializer = VetBaseSerializer(vet, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        serializer = VetBaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    @staticmethod
    def getUserByID(request, ID):
        try:
            vet = Vet.objects.get(pk=ID)
        except Vet.DoesNotExist:
            pass
        serializer = VetBaseSerializer(vet)
        return serializer.data


# Availability table service

class AvailabilityService:

    @staticmethod
    def getAll():
        availability = Availability.objects.all()
        serializer = AvailabilitySerializer(availability, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        serializer = AvailabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    @staticmethod
    def getUserByID(request, ID):
        try:
            availability = Availability.objects.get(pk=ID)
        except Availability.DoesNotExist:
            pass
        serializer = AvailabilitySerializer(availability)
        return serializer.data


# Taken table service

class TakenSlotsService:

    @staticmethod
    def getAll():
        takenSlots = TakenSlots.objects.all()
        serializer = TakenSlotsSerializer(takenSlots, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        serializer = TakenSlotsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    @staticmethod
    def getUserByID(request, ID):
        try:
            takenSlots = TakenSlots.objects.get(pk=ID)
        except TakenSlots.DoesNotExist:
            pass
        serializer = TakenSlotsSerializer(takenSlots)
        return serializer.data
