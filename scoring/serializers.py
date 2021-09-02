from typing import OrderedDict
from operator import itemgetter
from django.db.models.fields import CommaSeparatedIntegerField
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Score, WebFlagMaster, Flags
from authentication.serializers import *
from drf_writable_nested import WritableNestedModelSerializer
from django.core import serializers as serial

class FlagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flags
        fields= '__all__'

class ScoreSerializer(WritableNestedModelSerializer):
    user = CustomUserSerializer(read_only=True)
    flags = FlagsSerializer(many=True)

    class Meta:
        model=Score
        fields = '__all__'
        depth=1

class UserFlagSerializer(WritableNestedModelSerializer):
    user = CustomUserSerializer(read_only=True)

    flags = serializers.PrimaryKeyRelatedField(
        queryset = Flags.objects.all().order_by('name'), many=True
    )

    ordering = ['id']
    class Meta:
        model=Score
        fields = '__all__'
        depth=1

class HighscoreFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flags
        fields= ['points']

class HighscoreSerializer(serializers.ModelSerializer):
    dictionary = serializers.DictField(
        child = serializers.CharField())
    

