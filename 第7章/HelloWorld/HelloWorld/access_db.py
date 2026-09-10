# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
#from django.views.decorators import csrf
from HelloModel.models import Table1

# 数据库操作
def add_data(name_v,age_v,height_v):
    if name_v=='':
        return '<p>name must not be empty!</p>'
    list_name=[]
    record_list=Table1.objects.all()
    for r in record_list:
        list_name.append(r.name)
    if list_name.count(name_v)>0:
        return '<p>name <I>%s</I> was existed!</p>' % name_v
    else:
        conn = Table1(name=name_v,age=age_v,height=height_v)
        conn.save()
        return '<p>Data is added successfully!</p>'
def get_names():
    resp_str="<p>Names are flowing</p><p>"
    record_list=Test.objects.all()
    for r in record_list:
        resp_str += r.name +' '
    resp_str += '</p>'
    return resp_str
def filter_by_age(age_v):
    resp_str="<p>Records that age %d is flowing</p>" % age_v
    record_list=Test.objects.filter(age=age_v)
    for r in record_list:
        resp_str += '<p>'+r.name +' '+str(r.age)+'  '+str(r.height)+'</p>'
    return resp_str
def get_by_height(height_v):
    resp_str="<p>Records that height %f is flowing</p>" % height_v
    try:
        r=Test.objects.get(height=height_v)
        resp_str += '<p>'+r.name +' '+str(r.age)+'  '+str(r.height)+'</p>'
    except Exception as e:
        resp_str += "<p> not found! </p>"
#    print("r=",r)
    return resp_str
def order_by_age():
    resp_str="<p>Records order by age are flowing</p>"
    record_list=Test.objects.order_by("age")
    record_list=record_list.reverse()
    for r in record_list:
        resp_str += '<p>'+r.name +' '+str(r.age)+'  '+str(r.height)+'</p>'
    return resp_str
def update_data():
    conn = Test.objects.get(name='sun')
    conn.height += 1.75
    conn.save()
    Test.objects.filter(name='zhao').update(height=1.99)
    Test.objects.all().update(age=25)
    return '<p>Data is updated successfully!</p>'
def delete_data():
    conn = Test.objects.get(name='li')

    conn.delete()
    Test.objects.filter(height=3.5).delete()
    #Test.objects.all().delete()
    return '<p>Data is deleted successfully!</p>'

def testdb(request):
    context={}
    try:
        name_v=request.POST['name']
        age_v=int(request.POST['age'])
        height_v=float(request.POST['height'])
        conn = Table1(name=name_v,age=age_v,height=height_v)
        conn.save()
        response='Data is added successfully!'
    except Exception as e:
        response='%s' % e
    context['result']=response
#    response += get_names()
#    response += filter_by_age(22)
#    response += get_by_height(1.86)
#    response += order_by_age()
#    response += update_data()
#    response += order_by_age()
#    response += delete_data()
#    response += order_by_age()
    return render(request, "insert_record.html", context)
