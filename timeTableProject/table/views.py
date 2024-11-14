from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from table.serialazers import TableSerializer
from table.models import Lesson

class TableViewer(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = TableSerializer


def table_app(request):
    return render(request, 'main_app.html') 