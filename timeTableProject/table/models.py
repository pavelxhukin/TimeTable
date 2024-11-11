from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    facultyInfo = models.TextField('faculty info')


class Building(models.Model):
    buildingAdres = models.TextField('building adres',default='blk5')
    #inFaculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Room(models.Model):
    roomNumber = models.IntegerField('room number')    
    #inBuilding = models.ForeignKey(Building, on_delete=models.CASCADE)


class Course(models.Model):
    courseInfo = models.TextField('coourse info')

    
class CourseExample(models.Model):
    courseExampleInfo = models.TextField('example info')
    #inCourse = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lesson(models.Model):
    lessonInfo = models.TextField('lesson info')
    lessonDate = models.DateField('lesson Date')
    lessonTime = models.DateTimeField('lesson time')
    #inRoom = models.OneToOneField(Room, on_delete=models.CASCADE)


class StudyGroup(models.Model):
    groupName = models.TextField('group name')
    #inFaculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    #inLesson = models.ManyToManyField(Lesson)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountInfo = models.TextField('account info')
    role = models.BooleanField('role')
    #inCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
    #inGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    #inFaculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
