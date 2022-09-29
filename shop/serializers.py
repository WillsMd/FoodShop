from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from setuptools import setup, find_packages
setup(
    name= 'models',
    packages = find_packages()
    )
from  .models import *

class NewUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        
        fields = "__all__"
        

