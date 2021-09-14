"""mtnpulse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# include routes for Simple JWT’s TokenObtainPairView and TokenRefreshView views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    #Add APP URLS
    path('api/', include('mtnpulseapp.urls')),
    path('api/', include('mixtapes.urls')),
    #Used to get the API Token Pair. The token and Refresh Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #Used to Refresh the API Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Used to check if the token is still valid
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #Displays the Django Admin if it has not been specified in the URLS..Ensure it is the last path
    path('', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#A function to change the default Text in the DJango Admin Portal
def change_admin_default_settings():
    admin.site.site_header = 'MTN Pulse Portal'# default: "Django Administration"
    admin.site.index_title = 'Features area'   # default: "Site administration"
    admin.site.site_title = 'MTN Pulse Portal' # default: "Django site admin"
change_admin_default_settings()

