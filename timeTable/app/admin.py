from django.contrib import admin
from . models import Course,Professor,Student,Classroom,Lecture
# Register your models here.

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(Lecture)