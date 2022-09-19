from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema #helps to generate documentation
from users_auth.models import *
from users_auth.seralizers import *
# Create your views here.


#create api view to create user
class CreateUserView(generics.GenericAPIView):

    serializer_class = CreateShoeUserSerializer
    
    @swagger_auto_schema(operation_summary= "Create a user account")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():

            #use serializer to save data
            serializer.save()
            return Response(data = serializer.data, status= status.HTTP_201_CREATED)

        return Response(data= serializer.errors , status = status.HTTP_400_BAD_REQUEST)