import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/updates/"


def  get_list(id = None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id":id})
    res = requests.get(BASE_URL + END_POINT, data = data)
    print(res.status_code)
    status_code= res.status_code
    if status_code !=200:
        print('probably  not good sign')
    data = res.json()
    # for obj in data:
    #     print(obj['id'])
    #     if obj['id']==1:
    #         res1 = requests.get(BASE_URL + END_POINT + str(obj['id']))
    #         print(res1.json())
    return data


def create_update():
    new_data ={
        "user":1,
        "content":"Another new cool content",  
    }
    r = requests.post(BASE_URL + END_POINT,  data=json.dumps(data=new_data))
    if r.status_code ==  requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text
    

create_update()





def do_obj_update():
    new_data ={
        "id":12,
        #"id":1
        "content":"Another new cool content",  
    }
    r = requests.put(BASE_URL + END_POINT , data=json.dumps(data=new_data))

    # new_data ={
    #     "id":1,
    #     "content":"Another new cool content",  
    # }
    # r = requests.delete(BASE_URL + END_POINT , data=new_data)
    if r.status_code ==  requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text

do_obj_update()





def do_obj_delete():
    new_data ={
        "id":1
        #"content":"Another new cool content",  
    }
    r = requests.delete(BASE_URL + END_POINT, data = json.dumps(new_data) )

    # new_data ={
    #     "id":1,
    #     "content":"Another new cool content",  
    # }
    # r = requests.delete(BASE_URL + END_POINT , data=new_data)
    if r.status_code ==  requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text

do_obj_delete()
    