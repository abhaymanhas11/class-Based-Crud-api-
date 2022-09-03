from rest_framework import serializers
from .models import  student

class s_serializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','roll','address']