import datetime
from django.contrib.auth import get_user_model
from django.utils  import timezone
from rest_framework import  serializers

from rest_framework_jwt.settings import api_settings



jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta         = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User= get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password        = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2       = serializers.CharField(style={'input_type':'password'}, write_only=True)
    token           = serializers.SerializerMethodField(read_only=True)
    expires         = serializers.SerializerMethodField(read_only=True)
    token_response  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
             'email',
             'password',
             'password2',
             'token',
             'expires',
             'token_response'
        ]
        extra_kwrgs = {'password':{'write_only':True}}

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("plsease password must be match")
        return data
    
    def get_token_response(self, obj):
        payload = jwt_response_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(request, user, request= None)
        return  response

    def get_expires(self,obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def validate_email(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("plsease password must be match")
        return data

    def validate_usrname(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("plsease password must be match")
        return data

    def get_token(self,obj):
            user = obj
            payload = jwt_response_payload_handler(user)
            token = jwt_encode_handler(payload)
            return token

    def create(self, validated_data):
        user_obj = User(
            username= validated_data.get('username'),
            email = validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj

