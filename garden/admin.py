from django.contrib import admin
from .models import Flower, Fruit, Vegetable, Others

# Register your models here.
admin.site.register(Flower)
admin.site.register(Fruit)
admin.site.register(Vegetable)
admin.site.register(Others)