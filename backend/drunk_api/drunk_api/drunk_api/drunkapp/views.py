import base64
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from drunk_api.drunkapp.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
import requests
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    return HttpResponse("Hello world!")


# class ResultsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows results to be viewed.
#     """
#     r = requests.get('https://randomuser.me/api/?results=40')
#     print(r)
#     # r_status = r.status_code
#     # # If it is a success
#     # if r_status == 200:
#     #     print(r)

class SubmitImage(APIView):
    """
    View to handle image request for drunkness detection
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request)
        return Response("request")

    def post(self, request):
        """
        to submit an image
        """
        if request and request.FILES:
            if "file" in request.FILES:
                file = request.FILES["file"]
                print(file.__dict__)
                with file.open("rb") as img_file:
                    encodedImage = base64.b64encode(img_file.read())
                    print(encodedImage)
                return Response(json.dumps({"successfully encoded to base64:": encodedImage}))
        else:
            return Response("Image required!", 400)


class Pong(APIView):
    def get(self, request):
        return Response(json.dumps("PONG"))
