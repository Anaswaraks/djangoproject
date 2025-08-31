# it tell python how to transform our model into json data that we can access in our API
from rest_framework import serializers
from .models import myuser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myuser
        fields = '__all__'

