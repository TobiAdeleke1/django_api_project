from django.contrib import admin
from orders.models import *

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    A Customers admin, that is different to django original one
    it. It customized to the project 
    """
    #the list to diplay in the admin
    list_display = ['shoe_size','shoe_type','order_status','quantity','created_at']

    #To add the filter functionality to specific columns
    list_filter = ['created_at','order_status', 'shoe_size','shoe_type' ]