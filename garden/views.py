from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class FlowersPageView(ListView):
    model=Flower
    template_name = 'flowers.html'


class FruitsPageView(ListView):
    model = Fruit
    template_name = 'fruits.html'


class VegetablesPageView(ListView):
    model = Vegetable
    template_name = 'vegetables.html'


class OthersPageView(ListView):
    model = Others
    template_name = 'others.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
