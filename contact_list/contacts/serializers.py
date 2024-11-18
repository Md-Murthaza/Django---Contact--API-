from rest_framework import serializers
from .models import Contact
from django.contrib.auth.models import User



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','name','phone_number','email']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user