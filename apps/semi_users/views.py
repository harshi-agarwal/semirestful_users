from django.shortcuts import render,redirect
from . models import Product
# Create your views here.
def index(request):
    context={
    'products':Product.objects.all()
    }
    return render(request,"semi_users/index.html",context)
# def show(request):
#     pass
# def Edit(request):
#     pass
# def remove(request):
#     pass
 # def add(request):
 #     return redirect('products:new')
def new_product(request):
     if request.method == "POST":
         print "add user"
         Product.objects.add_product(request.POST)
         return redirect('products:index')

     else:
         return render(request,"semi_users/new.html")
def goback(request):
    return redirect('products:index')
def show_product(request,id):
    context ={
    'products':Product.objects.get(id=id)
    }
    return render (request,"semi_users/show.html",context)
def edit_product(request,id):
    if request.method == "POST":
        print request.POST
        Product.objects.filter(id=id).update(name=request.POST['name'],description=request.POST['description'],price=request.POST['price'])
        return redirect('products:index')


    context ={
                'products':Product.objects.get(id=id)
                }
    return render (request,"semi_users/edit.html",context)
def remove(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('products:index')
