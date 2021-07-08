from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

#Modelo de Productos

from .models import Product

# Create your views here.
