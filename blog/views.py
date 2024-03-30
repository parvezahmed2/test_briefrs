from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers


class BlogViewset(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer



class CategorieViewset(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategorieSerializer