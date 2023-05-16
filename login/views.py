from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .utils import *
from .models import *
from .forms import customer_info,CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as djangologin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


user_input=None
user_result=None

# Create your views here.
@login_required(login_url='login_page')
def home(request,pk):
    customer = User.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST["TOtitle"]
        number = request.POST["Tonumber"]
        if not number:
            number = 20
        #send title and number to result page
        global user_input
        def user_input():
            return customer,title,int(number)
        return redirect('result', pk=customer.id)
    return render (request,"loginTemp/home.html",{"customer":customer})



def result(request,pk):
    #get title and number from home page
    customer,title,number = user_input()
    pos,nat,neg = sentimental(str(title),int(number))
    gchart = chart([pos,nat,neg])
    gpich = show_pie_chart([pos,nat,neg])
    new_search = search(user=customer,title=title,number=number,pos=pos,nat=nat,neg=neg)
    new_search.save()
    return render(request,"loginTemp/result.html",{'chart':gchart,"pie":gpich,"customer":customer,'title':title,'number':number })


def show_result(request,pk):
    #get title and number from home page
    customer = user_result()
    search_result = search.objects.get(id=pk)
    gchart = chart([search_result.pos,search_result.nat,search_result.neg])
    gpich = show_pie_chart([search_result.pos,search_result.nat,search_result.neg])
    return render(request,"loginTemp/result.html",{'chart':gchart,"pie":gpich,"customer":customer,'title':search_result.title,'number':search_result.number})

@login_required(login_url='login_page') 
def search_history(request,pk):
    customer = User.objects.get(id=pk)
    search_result = customer.search_set.all()
    global user_result
    def user_result():
        return customer
    return render (request,"loginTemp/search.html",{'result':search_result, 'customer':customer})


def delet_item(request,pk):
    #get title and number from home page
    customer = user_result()
    search_result = search.objects.get(id=pk)
    if request.method == "POST":
        search_result.delete()
        return redirect("search_history",pk=customer.id)
    return render(request,"loginTemp/delete_form.html",{"delete":search_result,"customer":customer})

@login_required(login_url='login_page')
def user_profile(request,pk):
    customer = User.objects.get(id=pk)
    form = customer_info(instance=customer)
    if request.method == "POST":
        form = customer_info(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            messages.success(request, "تم تعديل الملف بنجاح")
    return render (request,"loginTemp/user_profile.html",{"customer":customer, "form":form})


def login_page(request):
    # if request.method == "POST":
    #     username = request.POST["Username"]
    #     password = request.POST["pass"]
    #     try:
    #         customer = User.objects.get(username=username,password=password)
    #         djangologin(request,customer)
    #         return redirect("home",pk=customer.id)
    #     except:
    #         messages.warning(request,"أسم المستخدم أو كلمة المرور غير صحيحة , الرجاء المحاولة مجددا")
    if request.user.is_authenticated:
        return redirect("home",pk=request.user.id)
    else:
        if request.method == "POST":
            username = request.POST["Username"]
            password = request.POST["pass"]
            user = authenticate(request,username=username, password=password)
            if user is not None:
                djangologin(request,user)
                return redirect("home",pk=user.id)
            else:
                messages.warning(request,"أسم المستخدم أو كلمة المرور غير صحيحة , الرجاء المحاولة مجددا")
        return render (request,"loginTemp/login.html")


def signUp(request):
    if request.user.is_authenticated:
        return redirect("home",pk=request.user.id)
    else:
        form = CreateNewUser()
        if request.method == "POST":
            form = CreateNewUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "تم انشاء حساب جديد بنجاح")
        return render (request,"loginTemp/signup.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect('login_page')


def my_index(request):
    return render (request,"loginTemp/index.html")

def about_us(request):
    return render (request,"loginTemp/About.html")

def contact_us(request):
    return render (request,"loginTemp/Contact.html")




