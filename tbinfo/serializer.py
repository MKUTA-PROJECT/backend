from rest_framework import serializers

from tbinfo.models import *

class TbInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInfo
        fields = "__all__"

