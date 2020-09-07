from .Serializer import UserSerializer
from .models import User


class UserService:

    @staticmethod
    def getAll():
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def postUser(request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    @staticmethod
    def getUserByID(request, ID):
        try:
            user = User.objects.get(pk=ID)
        except User.DoesNotExist:
            pass
        serializer = UserSerializer(user)
        return serializer.data
