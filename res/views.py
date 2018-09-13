from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        print(self.request.user)
        print(request.data)
        """
        Return a list of all users.
        """
        return Response({"message": "Hello, world!"})