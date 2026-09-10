from HelloModel.models import Table1
from django.http import HttpResponse
from django.shortcuts import render
import time
def page1(request):
    print('request=',request,type(request))
    return HttpResponse("<h1>Hello, I am page1!</h1>")
def page2(request):
    print('request=',request,type(request))
    context= {}
    context['name_title'] = 'page2.html'
    context['name_context'] = 'page2'
    xx=render(request, 'page2.html', context)
    print('xx=',xx)
    return xx
def page3(request):
    print('request=',request)
    context= {}
    context['time'] = time.strftime("%H:%M:%S",time.localtime())
    context['clock'] = time.localtime().tm_hour
    return render(request, 'page3.html', context)
def page4(request):
    print('request=',request)
    context= {}
    context['name_list']=['Zhao','Qian','Sun','Li']
    return render(request, 'page4.html', context)
def page5(request):
    return render(request, 'page5.html')
def add_data(request):
    print('request=',request)
    context={}
    if request.POST:
        try:
            name_v=request.POST['name']
            age_v=int(request.POST['age'])
            height_v=float(request.POST['height'])
            conn=Table1(name=name_v,age=age_v,height=height_v)
            conn.save()
            response='Data is added successfully!'
        except Exception as e:
            response='%s' % e
        context['result']=response
    return render(request, "insert_record.html", context)
def query_data(request):
    print('request=',request)
    context={}
    data_list=[]
    if request.POST:
        records=Table1.objects.all()
        for r in records:
            data_list.append([r.name,r.age,r.height])
        context['result']=data_list
    return render(request, "select_record.html", context)
def filter_data(request):
    print('request=',request)
    context={}
    data_list=[]
    if request.POST:
        age_v=int(request.POST['age'])
        records=Table1.objects.filter(age=age_v)
        for r in records:
            data_list.append([r.name,r.age,r.height])
        context['result']=data_list
    return render(request, "filter_by_age.html", context)
def delete_data(request):
    print('request=',request)
    context={}
    if request.POST:
        name_v=request.POST['name']
        try:
            Table1.objects.filter(name=name_v).delete()
            context['result']='Record is deleted successfully!'
        except Exception as e:
            context['result']=e
    return render(request, "delete_by_name.html", context)
def update_data(request):
    print('request=',request)
    context={}
    if request.POST:
        name_v=request.POST['name']
        height_v=float(request.POST['height'])
        try:
            Table1.objects.filter(name=name_v).update(height=height_v)
            context['result']='Record is updated successfully!'
        except Exception as e:
            context['result']=e
    return render(request, "update_by_name.html", context)
def index(request):
    print('request.META=',request.META)
    context={}
    context['ip']=request.META['HTTP_HOST']
    return render(request, "index.html", context)
