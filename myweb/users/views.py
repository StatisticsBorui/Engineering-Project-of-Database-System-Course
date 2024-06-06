from django.shortcuts import render, redirect
from .models import User, TeacherUser
from users.myforms import UserForm
import hashlib

IsTeacher = False


def hash_code(s, salt='Database-System-Homework'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()




def login(request):
    if request.session.get('is_login', None):  # 防止重复登录
        logout(request)

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                teacher_user = TeacherUser.objects.get(username=username)

            except User.DoesNotExist: #无该用户
                message = "用户不存在！"

            except TeacherUser.DoesNotExist: #不是老师
                if hash_code(user.password) == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True  # 往session字典内写入用户状态和数据
                    request.session['user_id'] = user.username
                    request.session['user_name'] = user.username
                    return redirect('/student/')
                else:
                    message = "密码不正确！"
                
            else:
                if hash_code(teacher_user.password) == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True  # 往session字典内写入用户状态和数据
                    request.session['user_id'] = user.username
                    request.session['user_name'] = user.username
                    return redirect('/teacher/page')
                else:
                    message = "密码不正确！"
          
        return render(request, 'users/login.html', locals())
    login_form = UserForm()
    return render(request, 'users/login.html', locals())





def logout(request):
    if not request.session.get('is_login', None):  # 如果本来就未登录，也就没有登出一说
        return redirect("user/login/")
    request.session.flush()  # 将session中的所有内容全部清空
    return redirect('user/login')