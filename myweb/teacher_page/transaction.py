from django.db import transaction
import sys
sys.path.append('../')
from stu_page.models import Student, Exam
import logging

logger = logging.getLogger(__name__)

def delete_student(stu_id):
    try:
        #开启事务管理
        with transaction.atomic():
            student = Student.objects.get(stu_id_id=stu_id) #如果没有该学生，删除操作停止

            if Exam.objects.filter(stu_id_id=stu_id).exists(): #是否存在成绩数据
                Exam.objects.get(stu_id_id=stu_id).delete() #删除成绩数据

            student.delete() #删除学生数据

    except Student.DoesNotExist:
        print('删除学生不存在！')
        logger.error(f"尝试删除不存在学生学号: {stu_id}")

    except Exception as e:
        logger.error(f"在删除学号 {stu_id}学生时有错误{e}发生")



