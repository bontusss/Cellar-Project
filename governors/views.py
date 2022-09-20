from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from governors.models import Governor
from governors.serializers import GovernorSerializer

# Create your views here.
class GovernorList(ListAPIView):
    '''This produces a list of all governors in  the database'''
    queryset = Governor.objects.all()
    serializer_class = GovernorSerializer


class GovernorDetail(RetrieveAPIView):
    queryset = Governor.objects.all()
    serializer_class = GovernorSerializer