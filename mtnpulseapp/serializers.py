# serializers.py

from rest_framework import serializers #import the serializer

from .models import LiveLink,Archives #import all models
#Live Links Serializers for Create, Get,Delete
class LiveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveLink

        fields = ('live_link_id', 'live_link_title','live_link_url','live_link_show_name','live_link_host','live_link_tot_likes','live_link_tot_views','created_on')
        extra_kwargs = {'live_link_tot_views': {'required': False},'live_link_tot_likes': {'required': False},'live_link_host': {'required': False},'live_link_show_name': {'required': False}}
        live_link_tot_likes=serializers.IntegerField()
        live_link_tot_views=serializers.IntegerField()
        live_link_title = serializers.CharField(max_length=100)
        live_link_show_name = serializers.CharField(max_length=100)
        live_link_host = serializers.CharField(max_length=100)
        live_link_url=serializers.URLField(max_length=100)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#Live Links Serializers for Update and get detail
class UpdateLiveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveLink
        fields = ('live_link_id', 'live_link_title','live_link_url','live_link_show_name','live_link_host','live_link_tot_likes','live_link_tot_views')
        extra_kwargs = {'live_link_url': {'required': False},'live_link_title': {'required': False},'live_link_tot_views': {'required': False},'live_link_tot_likes': {'required': False},'live_link_host': {'required': False},'live_link_show_name': {'required': False}}
        live_link_tot_likes=serializers.IntegerField()
        live_link_tot_views=serializers.IntegerField()
        live_link_title = serializers.CharField(max_length=100)
        live_link_show_name = serializers.CharField(max_length=100)
        live_link_host = serializers.CharField(max_length=100)
        live_link_url=serializers.URLField(max_length=100)
#Archives Serializers for Create, Get,Delete
class ArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archives
        fields = ('archive_id', 'archive_title','archive_url','archive_description','archive_presenter','archive_tot_likes','archive_tot_views','created_on')
        extra_kwargs = {'archive_tot_views': {'required': False},'archive_tot_likes': {'required': False},'archive_description': {'required': False},'archive_presenter': {'required': False}}
        archive_tot_views=serializers.IntegerField()
        archive_tot_likes=serializers.IntegerField()
        archive_title = serializers.CharField(max_length=100)
        archive_presenter = serializers.CharField(max_length=100)
        archive_url=serializers.FileField()
    def create(self,instance, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#Archives Serializers for Create, Get,Delete
class UpdateArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archives
        fields = ('archive_id', 'archive_title','archive_url','archive_description','archive_presenter','archive_tot_likes','archive_tot_views')
        extra_kwargs = {'archive_url': {'required': False},'archive_title': {'required': False},'archive_tot_views': {'required': False},'archive_tot_likes': {'required': False},'archive_description': {'required': False},'archive_presenter': {'required': False}}
        archive_tot_views=serializers.IntegerField()
        archive_tot_likes=serializers.IntegerField()
        archive_title = serializers.CharField(max_length=100)
        archive_presenter = serializers.CharField(max_length=100)
        archive_url=serializers.FileField()
    
