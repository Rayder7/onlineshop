import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from onlineshop.models import Product


class ProductSerializer(serializers.Serializer):
    firm = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)
    description = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.ImageField(read_only=True)
    stock = serializers.IntegerField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    available = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firm = validated_data.get("firm", instance.firm)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.time_create = validated_data.get("time_create", instance.time_create)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance