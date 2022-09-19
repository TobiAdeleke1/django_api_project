from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Order(models.Model):
    """
    
    """
    SHOE_SIZES =(
        ('first_small', '3' ),
        ('second_small', '4' ),
        ('first_medium', '5' ),
        ('second_medium', '6' ),
        ('first_large', '7' ),
        ('second_large','8' ),
    )

    SHOE_TYPES =(
        ('FLATS', 'flat'),
        ('BOOTS', 'boot'),
        ('TRAINERS', 'trainers'),
        ('SANDLES', 'sandals'),

    )

    ORDER_STATUS=(
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )
   
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    shoe_size = models.CharField(max_length=50,choices=SHOE_SIZES, default=SHOE_SIZES[0][0])
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPES, default=SHOE_TYPES[0][0])
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default= ORDER_STATUS[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"< Order size: {self.shoe_size} by {self.customer.id}"

