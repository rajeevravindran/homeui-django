from rest_framework import serializers
from .models import AlarmEvent

class AlarmEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmEvent
        fields = ('AlarmName', 'AlarmTime')
