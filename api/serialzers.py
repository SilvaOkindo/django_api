from rest_framework import serializers
from . models import Advocate

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'bio']
        model = Advocate
        
        