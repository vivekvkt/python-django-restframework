import json
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from . models import Update

def update_model_detail_view(request):
    data = {
        "count":100,
        "content":"some tough welcome"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data,  content_type='aplication/json')
    #return JsonResponse(data)


class JsonCBV(View):
    def get(self, request,*args, **kwargs):

        data = {
            "count":100,
            "content":"some tough welcome"
        }
        return JsonResponse(data)

