# serializers.py

from rest_framework import serializers #import the serializer

from .models import Dj,DjMixTape,LiveLink,Archives #import all models




class LiveLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LiveLink
        fields = ('live_link_id', 'live_link_title','live_link_url','created_on')
#Archives Serializer
class ArchivesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archives
        fields = ('archive_id', 'archive_title','archive_url','created_on')
