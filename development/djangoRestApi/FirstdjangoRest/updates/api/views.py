import json

from django.views.generic import View
from django.http import HttpResponse
from  .mixins import CSRFExemptMixin
from FirstdjangoRest.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel

from .utils import is_json


class UpdateModelDetailApiView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True

    def get_object(self, id = None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        qs = UpdateModel.objects.filter(id=id)
        if qs.count == 1:
            return qs.first()
        return None
    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)
        
    
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message":"not allowed"})
        return self.render_to_response(json_data, status=403)
       # return HttpResponse({}, content_type = 'application/json')


    def put(self, request, id,*args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=404)
        new_data = {}
        data = json.laods(obj.serialize())
        pased_data = json.loads(request.body)
        for key , value  in pased_data.items():
            data[key]  = value
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            #obj_data = obj.serialize()
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data,status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        json_data = json.dumps({"message":"something"})
        return self.render_to_response(json_data)
        #return HttpResponse({}, content_type = 'application/json')

    
    def delete(self, request,id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=404)
        deleted_ = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({"message":"sussessfully deleted"})
            return self.render_to_response(json_data , status = 200)
            #return HttpResponse({}, content_type = 'application/json')
        error_data = json.dumps({"message":"could not delete item"})
        return self.render_to_response(error_data, status=400)

class UpdateModelListApiView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True


    # def render_to_response(data, status=200):
    #     return HttpResponse(data, content_type='application/json', status=status)
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset= qs
        return qs
    def get_object(self, id = None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None

        if id is None:
            return None
        qs = self.get_queryset.filter(id=id)
        if qs.count == 1:
            return qs.first()
        return None
        

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"message":"not found update"})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:

            qs = self.get_queryset()
            #qs = UpdateModel.objects.all()
            json_data = qs.serialize()
            return self.render_to_response(json_data)


    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data,status=203)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {"message":"Not Allowed"}
        return self.render_to_response(data,status=400)
    
    # def delete(self, request, *args, **kwargs):
       
    #     data = json.dumps({"message":"U cant delete"})
    #     status_code = 403  #not allowd
    #     return self.render_to_response(data, status=403)

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=400)
        pased_data = json.loads(request.body)
        passd_id= pased_data.get('id', None)
        if not passd_id:
            error_data = json.dumps({"id":"requare field"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passd_id)
        if obj is None:
            error_data = json.dumps({"message":"object not found"})
            return self.render_to_response(error_data, status=404)
        new_data = {}
        data = json.laods(obj.serialize())
        
        for key , value  in pased_data.items():
            data[key]  = value
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            #obj_data = obj.serialize()
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data,status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        json_data = json.dumps({"message":"something"})
        return self.render_to_response(json_data)
        #return HttpResponse({}, content_type = 'application/json')

    
    def delete(self, request, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"not found update"})
            return self.render_to_response(error_data, status=400)
        pased_data = json.loads(request.body)
        passd_id= pased_data.get('id', None)
        if not passd_id:
            error_data = json.dumps({"id":"requare field"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passd_id)
        if obj is None:
            error_data = json.dumps({"message":"object not found"})
            return self.render_to_response(error_data, status=404)
        # obj = self.get_object(id=id)
        # if obj is None:
        #     error_data = json.dumps({"message":"not found update"})
        #     return self.render_to_response(error_data, status=404)
        deleted_ = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({"message":"sussessfully deleted"})
            return self.render_to_response(json_data , status = 200)
            #return HttpResponse({}, content_type = 'application/json')
        error_data = json.dumps({"message":"could not delete item"})
        return self.render_to_response(error_data, status=400)


    


   

    