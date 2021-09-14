# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import path
from .views import ArchivesApi,LiveLinkApi,ListLiveLinkDetailApi,ArchiveDetailApi

#Add Our API URLS
urlpatterns = [
    path('archives/', ArchivesApi.as_view(),name="Archives"),
    path('archives/<int:id>/', ArchiveDetailApi.as_view(),name="Archives Detail"),
    path('livelinks/', LiveLinkApi.as_view(),name="Live Links"),
    path('livelinks/<int:id>/', ListLiveLinkDetailApi.as_view(),name="Live Links Detail"),
    
    
]
