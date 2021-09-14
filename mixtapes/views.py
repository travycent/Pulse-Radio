from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateDjSerializer,ListDjSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Dj #import all models

#Class to Create A DJ
class CreateDjApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        DJ=CreateDjSerializer(data=request.data)
        if DJ.is_valid():
            new_dj=DJ.save()
            if new_dj:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'DJ Created successfully',
                }
                return Response(response,status=status_code)
        return Response(DJ.errors,status=status.HTTP_400_BAD_REQUEST)

#Class List All DJS

class ListDjApi(APIView):
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request):
        queryset = Dj.objects.all().order_by('dj_id')
        serializer_class = ListDjSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific DJS
class ListDjDetailApi(APIView):
    permission_classes = (AllowAny,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        queryset = Dj.objects.filter(dj_id=id).order_by('dj_id')
        serializer_class = ListDjSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
    #Update the Data
    def patch(self,request,id):
        queryset = Dj.objects.filter(dj_id=id).first()
        serializer_class = ListDjSerializer(queryset, data=request.data)
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

        
