from rest_framework import serializers

from lunar.models import Lunar


class LunarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lunar
        fields = 'prof_img'
