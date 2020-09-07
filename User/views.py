from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here

from User.Service import UserService


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserList(request):
    return Response(UserService.getAll())


@api_view(['POST'])
def UserList(request):
    return Response(UserService.postUser(request))


class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, ID):
        return Response(UserService.getUserByID(request, ID))
