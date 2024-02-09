from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
class Professor(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)
    def __str__(self) -> str:
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()
    name=models.CharField(help_text="Enter the Lecture name",max_length=255,default="Computer")
    def __str__(self) -> str:
        return self.name
