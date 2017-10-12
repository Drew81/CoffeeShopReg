from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coffee
from .serializers import CoffeeSerializer
from django.template import loader
from django.views.generic.edit import CreateView
from django.db import models
from .models import Register
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_coffees'

    def get_queryset(self):
    	return Coffee.objects.all()


def coffee_view(request):
    return render(request, 'shop/coffee.html')

def baked_view(request):
    return render(request, 'shop/baked.html')

def contacts_view(request):
	return render(request, 'shop/contacts.html')

#api
class CoffeeList(APIView):

	def get(self, request):
		coffee = Coffee.objects.all()
		serializer = CoffeeSerializer(coffee, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class BakeryList(APIView):

	def get(self, request):
		bakery = Bakery.objects.all()
		serializer = BakerySerializer(bakery, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class FoodList(APIView):

	def get(self, request):
		food = Food.objects.all()
		serializer = FoodSerializer(food, many=True)
		return Response(serializer.data)

	def post(self):
		pass



class RegisterCreate(CreateView):
    model = Register
    fields = ['first_name', 'last_name', 'email',]
    success_url = reverse_lazy('shop:index')
