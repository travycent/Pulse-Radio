from django.shortcuts import render

from rest_framework import viewsets
from .serializers import LiveLinkSerializer,ArchivesSerializer
from .models import Dj,DjMixTape,LiveLink,Archives #import all models

#Get all the Data of the Live Links
class LiveLinkViewSet(viewsets.ModelViewSet):
    queryset = LiveLink.objects.all().order_by('created_on')
    serializer_class = LiveLinkSerializer
#Get all the Data of the Archives
class AchivesViewSet(viewsets.ModelViewSet):
    queryset = Archives.objects.all().order_by('created_on')
    serializer_class = ArchivesSerializer
