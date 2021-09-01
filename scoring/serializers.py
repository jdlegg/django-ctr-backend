from typing import OrderedDict
from operator import itemgetter
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Score, WebFlagMaster
from authentication.serializers import *
from drf_writable_nested import WritableNestedModelSerializer

class ScoreSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model=Score
        fields = '__all__'

class HighScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Score
        fields = ('points', 'slug')

