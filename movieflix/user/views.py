from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer
from .tokens import create_jwt_pair_for_user

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)






""" 

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from .models import CustomUser
from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication #
from rest_framework.authtoken.models import Token #
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
    

class UserLogIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'user_name': user.username
        })

class SignUp(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        user = CustomUser.objects.create(
            username = request.data.get('username'),
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name'),
            email = request.data.get('email'),
            password = request.data.get('password'),
            )
# #data. request fix mit 
  #      if serializer.is_valid():
  #          serializer.save()
  #          token = Token.objects.get(user=user)
  #          subject = 'welcome to Movieflix'
  #          message = f'Hi {user.username}, thank you for registering in Movieflix.'
 #          email_from = settings.EMAIL_HOST_USER
 #           recipient_list = [user.email]
 #           send_mail( subject, message, email_from, recipient_list, token )
 #           return Response(serializer.data, status=status.HTTP_201_CREATED)
 #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#"""         """ serializer = self.serializer_class(data=request.data,
                                           context={'request': request}) """
        
 #      """  serializer.is_valid(raise_exception=True)                                 
     #   user = serializer.validated_data['user']
    #    token = Token.objects.create(user=user)
   #     subject = 'welcome to Movieflix'
  #      message = f'Hi {user.username}, thank you for registering in Movieflix.'
 #       email_from = settings.EMAIL_HOST_USER
#        recipient_list = [user.email]
#        send_mail( subject, message, email_from, recipient_list, token.key )
#        return Response(serializer.data, status=status.HTTP_201_CREATED) """ """
        




        

 

        
# der token muss jetzt per email zur password vergabe versendet werden.

        


# User Login müsste zum Sign um umgeschrieben werden. Beim Sign up den Token per Email versenden und mit diesem das password vergeben.

""" 

#def login(request):
 #   user_name = request.get('user_name')
  #  password = request.get('password')
   # token = Token.objects.create(user=...)#
    #print(token.key)#
    #return """



# date_joined mit aktuellem datum versehen

