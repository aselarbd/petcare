from .Serializer import PetCareUserSerializer
from .models import PetCareUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserService:

    @staticmethod
    def getAll():
        users = PetCareUser.objects.all()
        serializer = PetCareUserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        try:
            serializer = PetCareUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                msg = {"message": "User created successfully.", "email": serializer.data["email"], "Access-token": ""}
                return msg
            return serializer.errors
        except:
            msg = {"error": " Please provide valid details to register with the system (email, password, first_name, "
                            "last_name, contactNo, petName)"}
            return msg

    @staticmethod
    def getUserByID(request, ID):
        try:
            user = PetCareUser.objects.get(pk=ID)
        except PetCareUser.DoesNotExist:
            pass
        serializer = PetCareUserSerializer(user)
        return serializer.data
