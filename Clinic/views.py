from rest_framework.views import APIView
from rest_framework.response import Response

from Clinic.Service import ClinicBaseService, AvailabilityService, TakenSlotsService, VetService


class ClinicList(APIView):

    def get(self, request):
        return Response(ClinicBaseService.getAll())

    def post(self, request):
        return Response(ClinicBaseService.postUser(request))


class ClinicDetails(APIView):

    def get(self, request, ID):
        return Response(ClinicBaseService.getUserByID(request, ID))


class VetList(APIView):

    def get(self, request):
        return Response(VetService.getAll())

    def post(self, request):
        return Response(VetService.postUser(request))


class VetDetails(APIView):

    def get(self, request, ID):
        return Response(VetService.getUserByID(request, ID))


class AvailabilityList(APIView):

    def get(self, request):
        return Response(AvailabilityService.getAll())

    def post(self, request):
        return Response(AvailabilityService.postUser(request))


class AvailabilityDetails(APIView):

    def get(self, request, ID):
        return Response(AvailabilityService.getUserByID(request, ID))
