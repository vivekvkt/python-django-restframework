"""FirstdjangoRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from updates.views import ( 
                        json_exmple_view,
                        JsonCBV,JsonCBV2, 
                        SerializeListView,
                        SerializeDetailView
                        )   
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('api/updates/', include('updates.api.urls')), #api/updates/ -->list  api/updates/1/ -->detail
    #path('api/auth/jwt/', obtain_jwt_token),
    path('api/auth/', include('accounts.api.urls')),
    path('api/status/',  include('status.api.urls')),
    path('api/updates/',  include('updates.api.urls')),
    



    # path('json/example', json_exmple_view),
    # path('json/cbv', JsonCBV.as_view()),
    # path('json/cbv2', JsonCBV2.as_view()),
    # path('json/serialize/list', SerializeListView.as_view()),
    # path('json/serialize/detail', SerializeDetailView.as_view()),
]
