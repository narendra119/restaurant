from rest_framework import serializers
from .models import Orders, Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer()    

    class Meta:
        model = Orders
        fields = '__all__'