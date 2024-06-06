from django.shortcuts import render, redirect
from .insert import *

# Create your views here.
from .ShowScore import ShowScoreWithClass
from django.core import serializers
from .transaction import delete_student
import pandas as pd
from django.contrib import messages

import sys
sys.path.append('../')
from stu_page import models



# Create your views here.
def teacher_page(request):
    tempa = ShowScoreWithClass.objects.all()
    class1 = models.Class0.objects.get(class_id=1).stu_number
    class2 = models.Class0.objects.get(class_id=2).stu_number
    class3 = models.Class0.objects.get(class_id=3).stu_number
    classes = [class1,class2,class3]
    context = {'list': tempa,
               'classes':classes}

    return render(request,'teacher_page/index2.html',context)


def insert_data(request):
    if request.method == 'POST' and len(request.POST) > 0:
        insert(request)
        messages.success(request, "数据已成功插入！")
        # 重定向或渲染一个成功的页面
        return render(request, 'teacher_page/index2.html')
    else:
        form = InsertForm()

    return render(request, 'teacher_page/index2.html', {'form': form})

def delete_data(request):
    if request.method == 'POST' and len(request.POST) > 0:
        stu_id = request.POST.get('stu_id')
        print(stu_id)
        delete_student(stu_id)
    return render(request, 'teacher_page/index2.html')





from django.db import connection

def call_stored_procedure(information):
    with connection.cursor() as cursor:
        cursor.callproc('UpdateStudent', information)
    
    
def upload_result(request):
    if request.method == 'POST'and len(request.FILES) > 0:
        f = request.FILES['file']
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls']:
            data = pd.read_excel(f)
            for i in range(len(data)):
                stu_id = data.iloc[i,0]
                name = data.iloc[i,1]
                score1 = data.iloc[i,2]
                score2 = data.iloc[i,3]
                score3 = data.iloc[i,4]
                class_id = data.iloc[i,5]
                information = [stu_id, name, score1, score2, score3, class_id]

                try:
                    call_stored_procedure(information) #调用存储过程
                except:
                    print(f"数据{information}，可能不存在该学生或更新成绩超出实际范围！")
        else:
            error = '上传文件类型错误！'
            print(error)
            
    return render(request, 'teacher_page/index2.html')