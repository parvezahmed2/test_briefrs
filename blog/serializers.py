from rest_framework import serializers
from . import models


class BlogSerializer(serializers.ModelSerializer):
 
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Blog
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'




class  CategorieSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Categories
        fields = '__all__'