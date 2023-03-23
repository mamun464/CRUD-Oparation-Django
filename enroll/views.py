import time
from django.shortcuts import render
from .forms import StudentRegistration
from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def add_show(request):
    if request.method == 'POST':
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        with open("enroll\id.txt","r") as Store_id:
            id=int(Store_id.read())
            print(id)
            print(type(id))
        my_user=User(id,username,email,password)
        my_user.save()

        with open("enroll\id.txt","w") as ID_Insert:
            ID_Insert.write(str(id+1))
        
        
       
        
    stud=User.objects.all()
    
    
    return render(request,'enroll/addandshow.html',{'stu':stud})


def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request,id):
    pi=User.objects.get(pk=id)
    if request.method == 'POST':
        
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User(id,username,email,password)
        my_user.save()
        return HttpResponseRedirect('/')
   

    return render(request,'enroll/updatestudent.html', {'id':pi})

    # if request.method == 'POST':
    #     pi=User.objects.get(pk=id)
    #     pi.delete()
    #     return HttpResponseRedirect('/')
    


    
