from django import forms

class InsertForm(forms.Form):
    stu_id = forms.IntegerField(label="学号", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="姓名", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    score1 = forms.IntegerField(label="1月考", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    score2 = forms.IntegerField(label="2月考", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    score3 = forms.IntegerField(label="3月考", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class_id = forms.IntegerField(label="班号", widget=forms.NumberInput(attrs={'class': 'form-control'}))

class DeleteForm(forms.Form):
    stu_id = forms.IntegerField(label="学号", widget=forms.NumberInput(attrs={'class': 'form-control'}))



from django.shortcuts import render
from django.contrib import messages
import sys
sys.path.append('../')
from stu_page.models import Student, Exam, Class0
from users.models import User
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def insert(request):
    # 获取POST数据
    data = request.POST
    stu_id = data.get('stu_id')
    name = data.get('name')
    score1 = data.get('score1')
    score2 = data.get('score2')
    score3 = data.get('score3')
    class_id = data.get('class_id')

    # 将'NaN'字符串转换为None，否则转换为int
    score1 = None if score1 == 'NaN' else int(score1) if score1 else None
    score2 = None if score2 == 'NaN' else int(score2) if score2 else None
    score3 = None if score3 == 'NaN' else int(score3) if score3 else None

    # 获取班级信息，如果不存在则返回错误响应
    try:
        class0 = Class0.objects.get(class_id=class_id)
    except Class0.DoesNotExist:
        return HttpResponse('不存在这样的班级', status=400)

    # 尝试获取或创建用户
    try:
        user0, created = User.objects.get_or_create(
            username=stu_id,
            defaults={'password': '123456'} 
        )
    except Exception as e:
        return HttpResponse(f'用户创建/获取失败：{str(e)}', status=500)

    # 确保学生信息在创建考试成绩前存在
    try:
        student0, student_created = Student.objects.get_or_create(
            stu_id=user0,
            defaults={'name': name, 'class_id': class0}
        )
    except Exception as e:
        return HttpResponse(f'学生信息创建/获取失败：{str(e)}', status=500)

    # 创建考试成绩
    try:
        Exam.objects.create(
            stu_id=student0,
            score1=score1,
            score2=score2,
            score3=score3
        )
    except Exception as e:
        return HttpResponse(f'考试成绩创建失败：{str(e)}', status=500)

    return HttpResponse('数据已成功插入！', status=201)

