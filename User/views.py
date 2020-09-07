from rest_framework.views import APIView
from rest_framework.response import Response

from User.Service import UserService


class UserList(APIView):

    def get(self, request):
        return Response(UserService.getAll())

    def post(self, request):
        return Response(UserService.postUser(request))


class UserDetails(APIView):

    def get(self, request, ID):
        return Response(UserService.getUserByID(request, ID))

