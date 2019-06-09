
from django.urls import path

from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    )

urlpatterns = [
    

     path(r'^$', StatusAPIView.as_view(), name='list'),
     path(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
    
]