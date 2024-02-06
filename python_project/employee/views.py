from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from rest_framework.response import Response
# Create your views here.

SUCCESS_RESPONSE = {
    "status": True,
    "code": 200,
    "message": "Success",
    "data": ""
}

FAILURE_RESPONSE={
    "status": False,
    "code": 400,
    "message": ""
}

class EmployeeLogin(APIView):
    def post(self, request):
    
        request.data['email'] = request.data['email'].lstrip()
        request.data['email'] = request.data['email'].rstrip()
        if User.objects.get(username=request.data['email']):
            try:
               
                user = User.objects.get(username=request.data['email'])
                serialize = UserSerializer(user)
                print("hhhhhhh")
                token, created = Token.objects.get_or_create(user=user)
                print("hhhhhhh")

                login(request, user)
                SUCCESS_RESPONSE['message'] = 'koi b msg'
                SUCCESS_RESPONSE['data'] = {"User Detail": serialize.data, "Token": token.key}
                return Response(SUCCESS_RESPONSE)
            except:
                FAILURE_RESPONSE['message'] = 'koi b msg 2'
                return Response(FAILURE_RESPONSE)
        FAILURE_RESPONSE['message'] = 'koi b msg 6'
        return Response(FAILURE_RESPONSE)