from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication# TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
from rest_framework import status
from authentication.models import Token
from authentication.auth import TokenAuthentication

class TokenViewSet(APIView):
    """
    View to create multiple Tokens for a user.
    """
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        """
        Creates and returns a new token every time it is called by a user.
        """
        if request.data['name']:
            name = request.data['name']
            token = Token.objects.create(user=request.user, name=name)
            content = {
                'name': name,
                'token': token.key,
            }
            return Response(content)
        else:
            return Response({"error": "Missing key 'name'."}, status=status.HTTP_400_BAD_REQUEST)

# class TokenViewSet(APIView):
#     """
#     View to Create new standard Django Tokens.
#     """
#     authentication_classes = (BasicAuthentication, )
#     permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         """
#         Creates a new token and returns it to the user.
#         """
#         token = Token.objects.create(user=request.user)
#         return Response({"token": token.key})

@api_view()
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def test_auth(request):
    """Tests authentication worked successfuly."""
    return Response({"message": "You successfuly authenticated!"})
