from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    facultyInfo = models.TextField('faculty info')


class Building(models.Model):
    buildingAdres = models.TextField('building adres',default='blk5')
    inFaculty = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)


class Room(models.Model):
    roomNumber = models.IntegerField('room number')    
    inBuilding = models.ForeignKey(Building, null=True, on_delete=models.CASCADE)


class Course(models.Model):
    courseInfo = models.TextField('coourse info', null=True)

    
class CourseExample(models.Model):
    courseExampleInfo = models.TextField('example info')
    inCourse = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)


class Lesson(models.Model):
    lessonInfo = models.TextField('lesson info')
    lessonDate = models.DateField('lesson Date')
    lessonTime = models.DateTimeField('lesson time')
    inRoom = models.OneToOneField(Room, null=True, on_delete=models.CASCADE, related_name='roomInLesson')


class StudyGroup(models.Model):
    groupName = models.TextField('group name')
    inFaculty = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)
    inLesson = models.ManyToManyField(Lesson, null=True, related_name='lessonInGroup')

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountInfo = models.TextField('account info')
    role = models.BooleanField('role')
    inCourseExample = models.ForeignKey(CourseExample, null=True, on_delete=models.CASCADE)
    inGroup = models.ForeignKey(StudyGroup, null=True, on_delete=models.CASCADE, related_name='groupInAccount')
    inFaculty = models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)
