from django.db import models



# Create your models here.
class User(models.Model):

    username = models.IntegerField('账号', unique=True, primary_key=True, null=False)
    password = models.CharField('密码', max_length=16)

    class Meta:
        ordering = ['username']  
        verbose_name = '学生'
        verbose_name_plural = '学生'

    def __str__(self):  # 使用__str__帮助人性化显示对象信息
        return self.username
    

class TeacherUser(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username',primary_key=True)
    password = models.CharField('密码', max_length=16)

    class Meta:
        ordering = ['username']  
        verbose_name = '老师'
        verbose_name_plural = '老师'
    def __str__(self):  # 使用__str__帮助人性化显示对象信息
        return self.username