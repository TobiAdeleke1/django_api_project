from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Order(models.Model):
    """
    
    """
    SHOE_SIZES =(
        ('small', 'SMALL' ),
        ('medium', 'MEDIUM' ),
        ('large', 'LARGE' ),
    )

    SHOE_TYPES =(
        ('flats', 'FLATS'),
        ('boots', 'BOOTS'),
        ('trainers', 'TRAINERS'),
        ('sandals', 'SANDLES'),

    )

    ORDER_STATUS=(
        ('pending', 'PENDING'),
        ('in_transit', 'IN_TRANSIT'),
        ('delivered', 'DELIVERED')
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

