# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from _mysql import connection

from django.contrib.auth.models import User
from django.db import connection

from .models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def home(request):
    if(request.method=="GET"):
        return render(request,'index.html',{})

    else:
        #return HttpResponse("logging in..........")
        username=request.POST.get('username')
        password=request.POST.get('password')
        type=request.POST.get('type')
        print(type)

        #return HttpResponse(username+password)
        u=authenticate(username=username, password=password)
        if u:
            login(request,u)
            if(type=='1'):
                return redirect('student_profile/')
            else:
                return redirect('company_profile/')

        else:
            return HttpResponse("Invalid login details")


def student_profile(request):

    dic={}


    user_info = Student.objects.raw("select * from student where username=%s",[request.user])

    for u in user_info:
        
        dic['name'] = u.name
        dic['dob'] = u.dob
        dic['gender'] = u.gender
        dic['address'] = u.address
        dic['mobno'] = u.mobno
        dic['email'] = u.email
        dic['course'] = u.course
        dic['branch'] = u.branch
        dic['cgpa'] = u.cgpa
        dic['arrears'] = u.arrears
        dic['sslc'] = u.sslc
        dic['plustwo'] = u.plustwo
        dic['username'] = u.username 
    return render(request, 'profile_stud.html', dic)


def company_profile(request):
    return render(request, 'profile_comp.html', {})

def register(request):

    if request.method == 'POST':

        

        name = request.POST.get('name')
        birth_day = request.POST.get('birthday')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        regno = request.POST.get('regno')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        cgpa = request.POST.get('cgpa')
        arrears = request.POST.get('arrears')
        sslc = request.POST.get('sslc')
        plus_two = request.POST.get('plustwo')
        username=request.user
        var=Student.objects.raw("select * from  student where id=(select max(id) from student)")
        for i in var:
            id=i.id
        print(id)

        with connection.cursor() as cursor:
            cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [id+1,name,birth_day,gender,address,mobile,email,course,branch,cgpa,arrears,sslc,plus_two,username])





        return redirect('/student_profile')


    print (request.user)
    return render(request, 'register.html')

def company(request):
    return render(request, 'company.html', {})

def jobinfo(request):
    return render(request, 'jobinfo.html', {})