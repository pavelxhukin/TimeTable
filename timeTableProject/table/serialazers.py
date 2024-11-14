from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from table.models import Lesson

class TableSerializer(ModelSerializer):
    inRoom = serializers.SlugRelatedField(slug_field="roomNumber", read_only = True)
    class Meta:
        model = Lesson 
        fields = ['lessonInfo', 'lessonTime', 'inRoom']
