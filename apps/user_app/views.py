from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):
    return render(request,"user_app/index.html")
def register(request):
    if request.method == "POST":
        user1={
        'fname':request.POST['first_name'],
        'lname':request.POST['last_name'],
        'email':request.POST['email'],
        'password':request.POST['Password'],
        'cpassword':request.POST['cpassword'],
        }
        user=User.objects.validate(user1)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"user_app/index.html",context)
        else:
            context={
            'user':user
            }
        return render(request,"user_app/success.html",context)
    # else:
    #     return redirect('/')
def login(request):
    if request.method == "POST":

        user=User.objects.login(request.POST)
        # print type(user)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"user_app/index.html",context)
        else:
            context ={
                'user2':user
                }
        return render(request,"user_app/success.html",context)
