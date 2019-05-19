import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from FirstdjangoRest.mixins import JsonResponseMixin
from . models import Update

def json_exmple_view(request):
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
            "count":103,
            "content":"some tough welcome"
        }
        return JsonResponse(data)



class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":200,
            "content":"some new content"
        }
        return self.render_to_json_response(data)


# python manage.py dumpdata --format json --indent 4
#python manage.py dumpdata updates.Update --format json --indent 4
class SerializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        #json_data = data
        #data =  serialize("json", [obj,], fields=('user', 'content'))
        # data = {
        #     "count":obj.user.username,   
        #     "content":obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data,  content_type='aplication/json')



class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        #data =  serialize("json", qs, fields=('user', 'content'))
        #data =  serialize("json", qs)
        #json_data = data
        json_data = Update.objects.all().serialize()   
        
        # data = {
        #     "count":obj.user.username,
        #     "content":obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data,  content_type='aplication/json')

