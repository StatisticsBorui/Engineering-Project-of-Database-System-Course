from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
from .searchScore import ShowScore
from django.core import serializers



# Create your views here.
def student_page(request):
    tempa = ShowScore.objects.filter(stu_id_id=request.session['user_id']).first()
    #data = serializers.serialize("json", tempa)
    context = {'id': tempa.stu_id_id,
               'name': tempa.name,
                'score1': tempa.score1,
                'score2': tempa.score2, 
                'score3': tempa.score3
               }

    return render(request,'stu_page/index.html',context)