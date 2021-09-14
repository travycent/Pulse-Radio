# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import path
from .views import CreateDjApi,ListDjApi,ListDjDetailApi

#Add Our API URLS
urlpatterns = [
    path('djs/create', CreateDjApi.as_view(),name="create_dj"),
    path('djs/',ListDjApi.as_view(),name="djs"),   
    path('djs/<int:id>/',ListDjDetailApi.as_view(),name="dj_detail"), 
]