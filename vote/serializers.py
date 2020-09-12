from rest_framework import serializers

from lunar.models import Lunar
from vote.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
