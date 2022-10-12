from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Customer
