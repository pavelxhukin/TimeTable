from django.db import models


class Building(models.Model):
    buildingId = models.AutoField('buildingId')
    buildingAdres = models.TextField('Adres')
    # classId #classListOfAvailebleClasses
    
    def __str__(self):
        return self.title 
class Class(models.Model):
    classId = models.AutoField('classId')
    # lessonId
    
    def __str__(self):
        return self.title
