from django.db import models

import sys
sys.path.append('../')
from users.models import TeacherUser

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.OneToOneField(TeacherUser, to_field='username', primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    