# serializers.py --This file will serialize all the data of this app
import inspect
from rest_framework import serializers #Import the Serializers
from .models import Dj,DjMixTape #Import all the models in the APP

#DJ Create Serializer
class CreateDjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dj
        fields=('dj_name','dj_email','dj_website','dj_image')
        extra_kwargs = {'dj_website': {'required': False},'dj_image': {'required': False}}
        dj_email=serializers.EmailField()
        dj_name = serializers.CharField(max_length=100)
        dj_website=serializers.URLField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#DJ List Serializer
class ListDjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dj
        fields=('dj_id','dj_name','dj_email','dj_website','dj_image')
