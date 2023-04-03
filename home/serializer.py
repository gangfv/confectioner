from rest_framework import serializers
from home.models import Number


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'
