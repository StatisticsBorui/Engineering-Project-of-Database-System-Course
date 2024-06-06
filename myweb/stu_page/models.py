from django.db import models

import sys
sys.path.append('../')
from users.models import User

class Class0(models.Model):
    class_id = models.SmallIntegerField(null=False, primary_key=True)
    stu_number = models.SmallIntegerField(default=0)

# Create your models here.
class Student(models.Model):   
    #stu_id = models.IntegerField(null=False, primary_key=True)
    stu_id = models.OneToOneField(User, null=False, primary_key=True, to_field="username", on_delete=models.CASCADE)    
    name = models.CharField(max_length=64) 
    major = models.CharField(max_length=128) 
    class_id = models.ForeignKey(Class0, to_field="class_id", on_delete=models.SET(0))   



class Exam(models.Model):
    stu_id = models.OneToOneField(Student, to_field="stu_id", primary_key=True, on_delete=models.CASCADE)
    score1 = models.SmallIntegerField(null=True)
    score2 = models.SmallIntegerField(null=True)
    score3 = models.SmallIntegerField(null=True)

