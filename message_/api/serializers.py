from rest_framework import serializers
from message_.models import Templates, Contact


class template_serializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'

class Contacts_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'