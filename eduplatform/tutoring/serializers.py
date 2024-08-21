from rest_framework import serializers
from .models import TutorSession

class TutorSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSession
        fields = ['id', 'user', 'subject', 'session_date', 'notes']
