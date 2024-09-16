from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class DonationApplicationSerializer(serializers.ModelSerializer):
    organization = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DonationApplication
        fields = "__all__"
