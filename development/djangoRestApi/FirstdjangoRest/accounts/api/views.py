from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .utils import jwt_response_payload_handler
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User  = get_user_model()
class AuthAPIView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({'detail':'You are already'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username= username, password=password)
        qs  = User.objects.filter(
                Q(username_iexact=username) | 
                Q(email_iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.filter()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_response_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(request, user, request= request)
                return Response(response)
        return Response({"detail":"invalid creditials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.object.all()
    serializer_classes = UserRegisterSerializer
    permissions_classes = [permissions.AllowAny]
    
# class RegisterAPIView(APIView):
#     authentication_classes = []
#     permission_classes = [permissions.AllowAny]
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return Response({'detail':'You are already Register and authnticated'}, status=400)
#         data = request.data
#         username        = data.get('username')
#         email           = data.get('email')
#         password        = data.get('password')
#         password2       = data.get('password2')
#         qs  = User.objects.filter(
#                 Q(username_iexact=username) | 
#                 Q(email_iexact=username)
#             )
#         if password != password2:
#             return Response({"password":"password must be match"}, status=401)
#         if qs.exists():
#             return Response({"detail":"this user already exist"}, status=401)
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_response_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(request, user, request= request)
#             return Response(response, status=201)
#         return Response({"detail":"invalid request"}, status=400)



        # if qs.count() == 1:
        #     user_obj = qs.filter()
        #     if user_obj.check_password(password):
        #         user = user_obj
        #         payload = jwt_response_payload_handler(user)
        #         token = jwt_encode_handler(payload)
        #         response = jwt_response_payload_handler(request, user, request= request)
        #         return Response(response)
        # return Response({"detail":"invalid creditials"}, status=401)