
from django.urls import path
from .views import ( 
                      UpdateModelDetailApiView,
                      UpdateModelListApiView
                        )   
urlpatterns = [
    
    path('', UpdateModelListApiView.as_view()),  #api/updates  -- list/create
    #path(r'^(?P<id>\d+)/$', UpdateModelDetailApiView.as_view()),
    #path(r'^(?P<int:id>\d+)/$', UpdateModelDetailApiView.as_view()),
    path('<int:id>/', UpdateModelDetailApiView.as_view()),
   
    
]