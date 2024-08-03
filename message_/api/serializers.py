from rest_framework import serializers
from message_.models import Templates


class template_serializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'