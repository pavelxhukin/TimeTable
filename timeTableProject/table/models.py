from django.db import models


class Building(models.Model):
    buildingId = models.IntegerField('buildingId')
    buildingAdres = models.TextField('Adres')
    # classId #classListOfAvailebleClasses
    
class Class(models.Model):
    classId = models.IntegerField('classId')
    # lessonId
    
class Course(models.Model):
    courseId = models.IntegerField()
    courseName = models.TextField()
    # courseExampleId

class CourseExample(models.Model):
    courseExampleId = models.IntegerField()
    # groupId
    # lessonId

class Faculty(models.Model):
    facultyId = models.IntegerField()
    # facultyInfo ???
    # group_ids

class Lesson(models.Model):
    lessonId = models.IntegerField()
    lessonInfo = models.TextField()
    # TimeSlotId
    # userId(teacherId)
    # classId
    # courseExampleId
    lessonType = models.CharField(max_length=255)

class Group(models.Model):
    groupId = models.IntegerField()
    groupName = models.TextField()
    # lessonId
    # groupExampleId

class TimeSlot(models.Model): 
    timeSlotId = models.IntegerField()
    slotTime = models.DateTimeField()
    
