from rest_framework import serializers
from subscriptions.models import Subs

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = '__all__'