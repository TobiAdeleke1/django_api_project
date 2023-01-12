from orders.models import *
from rest_framework import serializers


class CreateOrderSerializer(serializers.ModelSerializer):

    shoe_size = serializers.CharField(max_length=50)
    shoe_type = serializers.CharField(max_length=50)
    quantity = serializers.IntegerField()

    #This will be an hiddenfield that can only by superuser, admin or staff
    order_status = serializers.HiddenField(default='pending')
    
  
    class Meta:
        model = Order
        fields = ['id','shoe_size', 'shoe_type','order_status', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):

    shoe_size = serializers.CharField(max_length=50)
    shoe_type = serializers.CharField(max_length=50)
    quantity = serializers.IntegerField()
    order_status = serializers.CharField(default='pending')
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    
  
    class Meta:
        model = Order
        fields = ['id','shoe_size', 'shoe_type','order_status', 'quantity', 'created_at', 'update_at']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='pending')

    class Meta:
        model = Order
        fields = ['order_status']