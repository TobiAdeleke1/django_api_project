from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import ( IsAuthenticated,
                                    IsAuthenticatedOrReadOnly, IsAdminUser )

from drf_yasg.utils import swagger_auto_schema
from orders.serializers import *
from orders.models import *
from django.contrib.auth import get_user_model


# Create your views here.
User= get_user_model()

class CreateOrderListView(generics.GenericAPIView):
    
    # Need to specify the serializer class and the queryset 
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @swagger_auto_schema(operation_summary="List all orders made", 
    operation_description="Listing the orders made by this account")
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance= orders, many = True)

        return Response(data = serializer.data, status = status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create a new order", 
    operation_description="The parameters for new order. Sizes: Small, Medium and Large. Shoe Types: flats, boots, trainers and sandals ")
    def post(self, request):

        #Get the data from the request to validate it
        data = request.data

        serializer = self.serializer_class(data=data)
        
        # B. Get the user and save the data with users
        user = request.user

        #check if serializer is valid
        if serializer.is_valid():

            #then save the data
            serializer.save(customer = user)

            return Response(data = serializer.data , status = status.HTTP_201_CREATED)

        #ELSE
        return Response(data= serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class OrderDetailsView(generics.GenericAPIView):
    
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    
    @swagger_auto_schema(operation_summary="Retrive an order datails by its ID")
    def get(self, request, order_id):

        order = get_object_or_404(Order,pk =order_id)
        serializer = self.serializer_class(instance = order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an Order by its ID")
    def put(self, request, order_id):
        data = request.data

        order = get_object_or_404(Order, pk= order_id)

        serializer = self.serializer_class(data = data, instance= order)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status= status.HTTP_200_OK)

        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete an Order by its ID")
    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk= order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatusView(generics.GenericAPIView):
    
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Update an Order Status by its ID")
    def put(self, request,order_id):
        order = get_object_or_404(Order, pk = order_id)

        data = request.data
        serializer = self.serializer_class(data = data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return Response(data = serializer.data , status= status.HTTP_200_OK)
        
        return Response(data = serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class UserOrdersView(generics.GenericAPIView):
    #use the same serializer, as it as all the relevant parameters
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="View a specific User's Orders")
    def get(self,request, user_id):
        user = User.objects.get(pk = user_id)

        orders = Order.objects.filter(customer = user)
        serializer = self.serializer_class(instance = orders , many = True)
     
        return Response(data = serializer.data, status= status.HTTP_200_OK)


class UserOrderDetailView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="View a specific Order from a specific User")
    def get(self, request, user_id, order_id):
        user = User.objects.get(pk = user_id)

        orders = Order.objects.filter(customer= user).get(pk= order_id)

        serializer = self.serializer_class(instance=orders)

        return Response(data= serializer.data , status= status.HTTP_200_OK)


