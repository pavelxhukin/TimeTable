from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from table.models import Lesson
from table.serialazers import TableSerializer

class TableView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = TableSerializer
