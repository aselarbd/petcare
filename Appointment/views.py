from rest_framework.views import APIView
from rest_framework.response import Response

from Appointment.Service import AppointmentService


class AppointmentList(APIView):

    def post(self, request):
        return Response(AppointmentService.postUser(request))


class AppointmentDetails(APIView):

    def get(self, request, ID):
        return Response(AppointmentService.getUserByID(request, ID))

