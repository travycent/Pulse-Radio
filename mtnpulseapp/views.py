from django.shortcuts import render

from rest_framework import viewsets
from .serializers import LiveLinkSerializer,UpdateLiveLinkSerializer,ArchivesSerializer,UpdateArchivesSerializer
from .models import LiveLink,Archives #import all models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#Get all the Data of the Live Links
class LiveLinkViewSet(viewsets.ModelViewSet):
    queryset = LiveLink.objects.all().order_by('created_on')
    serializer_class = LiveLinkSerializer

#Class to Manage Live Links
class LiveLinkApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        live=LiveLinkSerializer(data=request.data)
        if live.is_valid():
            new_live=live.save()
            if new_live:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'Live Link Created successfully',
                }
                return Response(response,status=status_code)
        return Response(live.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = LiveLink.objects.all().order_by('created_on')
        serializer_class = LiveLinkSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific Live Link
class ListLiveLinkDetailApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = LiveLink.objects.filter(live_link_id=id)
            serializer_class = UpdateLiveLinkSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = LiveLink.objects.filter(live_link_id=id).first()
        serializer_class = UpdateLiveLinkSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
#Class to Manage Archives
class ArchivesApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        archive=ArchivesSerializer(data=request.data)
        if archive.is_valid():
            new_archive=archive.save()
            if new_archive:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'Archive Created successfully',
                }
                return Response(response,status=status_code)
        return Response(archive.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = Archives.objects.all().order_by('created_on')
        serializer_class = ArchivesSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific Archive
class ArchiveDetailApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = Archives.objects.filter(archive_id=id)
            serializer_class = UpdateArchivesSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = Archives.objects.filter(archive_id=id).first()
        serializer_class = UpdateArchivesSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
