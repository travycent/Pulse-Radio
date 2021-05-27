# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'livelinks', views.LiveLinkViewSet)
router.register(r'archives', views.AchivesViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^login', UserLoginView.as_view()),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    
]