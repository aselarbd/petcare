from .Serializer import AppointmentSerializer
from .models import Appointment
from Clinic.models import TakenSlots
from User.models import PetCareUser


class AppointmentService:


    @staticmethod
    def postUser(request):
        data = request.data

        userID = data["userID"]
        try:
            user = PetCareUser.objects.get(pk=userID)

            vetID = data["vetID"],
            clinicID = data["clinicID"]
            availabilityID = data["availabilityID"]

            try:
                slot = TakenSlots.objects.filter(vetID=vetID, clinicID=clinicID, availabilityID=availabilityID)
                msg ={"error": "Already Appointment with this combination"}
                serializer = AppointmentSerializer(data=msg)
                if serializer.is_valid():
                    return serializer.data
                return serializer.errors

            except:
                serializer = AppointmentSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return serializer.data
                return serializer.errors

        except PetCareUser.DoesNotExist:
            msg = {"error": " Please resister with the system"}
            serializer = AppointmentSerializer(data=msg)
            if serializer.is_valid():
                return serializer.data
            return serializer.errors




    @staticmethod
    def getUserByID(request, ID):
        try:
            appointment = Appointment.objects.filter(userID=ID)
        except Appointment.DoesNotExist:
            pass
        serializer = AppointmentSerializer(appointment)
        return serializer.data
