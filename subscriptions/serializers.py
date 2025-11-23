from rest_framework import serializers
from subscriptions.models import Subs

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}