from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('flowers/', FlowersPageView.as_view(), name='flower'),
    path('fruits/', FruitsPageView.as_view(), name='fruit'),
    path('vegetables/', VegetablesPageView.as_view(), name='vegetable'),
    path('others/', OthersPageView.as_view(), name='other'),
]
