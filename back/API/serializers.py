from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.role = validated_data.get('role', '')
        user.save()
        return user
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        order = Orders.objects.create(
            user=User.objects.filter(username=validated_data['user']).first(),
            title=validated_data['title'],
            status=validated_data['status'],
            orderType=validated_data['orderType'],
            adress=validated_data['adress'],
            price=validated_data['price'],
            time=validated_data['time']
        )
        order.save()
        return order
    
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

    def create(self, validated_data):
        order = Services.objects.create(
            image=validated_data['image'],
            title=validated_data['title'],
            description=validated_data['description'],
            openDescription=validated_data['openDescription'],
            price=validated_data['price'],
        )
        order.save()
        return order