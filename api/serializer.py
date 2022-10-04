from pyexpat import model
from rest_framework import serializers
from wallet import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=('first_name','email','age','address')  