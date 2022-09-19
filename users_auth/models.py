from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ShoeUserManager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):

        # check if email is null, then throw error
        if not email:
            raise ValueError(_("Email Should be provided"))

        # normal the email: takes the email and convert the domain part to lowercase
        email= self.normalize_email(email)
        
        #get the new user from the manager model
        new_user = self.model(email=email, **extra_fields)

        #set the password, and the method/function HASHES the password,
        new_user.set_password(password)

        # then stores it to the database.
        new_user.save()

        return new_user


    def create_superuser(self,email, password, **extra_fields):
        """
         A function to createsuperuser, when django 'createuser'
        """
        #For when the superuser is a staff
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True "))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))


        return self.create_user(email,password,**extra_fields)


class ShoeUser(AbstractUser):
    
    username = models.CharField(_('Username'),max_length=30, unique= True)
    email = models.EmailField(_('Email'),max_length=100, unique=True)

    #use django phonenumber module fields, to check if valid
    #pip install django-phonenumber-field[phonenumbers]
    phone_number = PhoneNumberField(null =False,unique= True)
    date_joined = models.DateTimeField(_('Date'), auto_now_add=True)
    
    #here to use email to log-into the system 
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username','phone_number']

    #Specify how user object are created
    # objects =ShoeUserManager()

    def __str__(self):
        return f"<User {self.email}"