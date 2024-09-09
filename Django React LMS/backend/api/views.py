from django.shortcuts import render
from api import serializer as api_serializer
from userauths.models import User, Profile
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from random import randint

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer

def generate_random_opt(length=7):
    opt = ''.join([str(randint(0,9)) for _ in range(length)])
    return opt

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def get_object(self):
        email = self.kwargs['email'] # api/v1/password-email-verify/sousagomide@gmail.com
        user = User.objects.filter(email = email).first()
        if user: 
            uuidb64 = user.pk
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.refresh_token = refresh_token
            user.opt = generate_random_opt()
            user.save()
            link = f'http://localhost:5173/create-new-password/?opt={user.opt}&uuidb64={uuidb64}&refresh_token={refresh_token}'
            # print('link ======', link)
        return user

class PasswordChangeAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def create(self, request, *args, **kwargs):
        opt = request.data['opt']
        uuidb64 = request.data['uuidb64']
        password = request.data['password']
        user = User.objects.get(id=uuidb64, opt=opt)
        if user:
            user.set_password(password)
            user.opt = ''
            user.save()
            return Response({'message': 'Senha alterada com sucesso'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Usuário não existe'}, status=status.HTTP_404_NOT_FOUND)


