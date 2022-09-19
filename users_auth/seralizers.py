from orders.models import *
from users_auth.models import *
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class CreateShoeUserSerializer(serializers.ModelSerializer):

    """
    Get the parameters from the model version, and 
    convert them to their serializer versions.
    
    """

    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_null =False, allow_blank= False)
    password = serializers.CharField(min_length =8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number','password']

     #customize the validation, hence we are overriding django's one
    def validate(self, attrs):

        #1. First check if username already exist
        username_exists = User.objects.filter(username = attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail= "User with username exists")

        #2. First check if email already exist
        email_exists = User.objects.filter(email = attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail= "User with email exists")
        
        #3. First check if phonenumber already exist
        phonenumber_exists = User.objects.filter(phone_number = attrs['phone_number']).exists()

        if phonenumber_exists:
            raise serializers.ValidationError(detail= "User with phonenumber exists")

        #Note: super calls the model serilizer class
        return super().validate(attrs)

    #create specific function to also be able to HASH the password
    def create(self, validated_data):

        user = User.objects.create(
            username = validated_data["username"],
            email =  validated_data["email"],
            phone_number = validated_data['phone_number'],
        )
        
        #For Password Hashing 
        user.set_password(validated_data["password"])

        user.save()

        return user