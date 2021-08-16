from django.contrib.auth.models import User, Group
from rest_framework import serializers
from plots.models import Plots


class PlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plots
        fields = '__all__'
