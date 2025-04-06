from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )  # Send category as ID from frontend

    category_detail = CategorySerializer(source='category', read_only=True)  # For GET requests

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'category_detail',
            'description',
            'price',
            'stock_quantity',
            'is_available',
            'image',
        ]
