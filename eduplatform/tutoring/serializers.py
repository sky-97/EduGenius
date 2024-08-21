from rest_framework import serializers
from .models import TutoringSession

class TutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id', 'title', 'description', 'date']
