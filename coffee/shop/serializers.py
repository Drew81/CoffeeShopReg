from rest_framework import serializers
from .models import Coffee, Bakery, Food

class CoffeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Coffee
		fields = '__all__'

class BakerySerializer(serializers.ModelSerializer):

	class Meta:
		model = Bakery
		fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):

	class Meta:
		model = Food
		fields = '__all__'