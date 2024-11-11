from rest_framework.serializers import ModelSerializer

from table.models import Lesson

class TableSerializer(ModelSerializer):
    class Meta:
        model = Lesson 
        fields = ['lessonId', 'lessonInfo', 'lessonType']