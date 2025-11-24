from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}