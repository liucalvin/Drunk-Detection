from django.contrib.auth.models import User, Group
from rest_framework import viewsets
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
