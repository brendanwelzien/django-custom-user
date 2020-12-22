from django.urls import path
from .views import BreadList

urlpaterns = [
    path('bread/', BreadList.as_view(), name='bread-list'),
]