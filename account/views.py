from django.contrib.auth import get_user_model
from django.shortcuts import render
from permission import permission
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from account.send_email import send_confirmation_email
from account.serializers import RegisterSerializer, ActivationSerializer, UserSerializer

# Create your views here.
User = get_user_model()
class RegistrationView(APIView):

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer)
        user = serializer.save()
        print(user.email)
        send_confirmation_email(user.email, user.activation_code)
        # if user:
        #     try:
        #         send_confirmation_email(user.email, user.activation_code)
        #     except:
        #         return Response({'message': 'code not to find in email', 'data': serializer.data}, status = 201)

        return Response(serializer.data, status=201)


class ActivationView(GenericAPIView):
    serializer_class = ActivationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response('Успешно активирован', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
