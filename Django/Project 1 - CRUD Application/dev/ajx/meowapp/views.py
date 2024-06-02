from django.shortcuts import render,redirect
from .forms import Createuserform, loginform,createrecord,updaterecord
from .models import Record
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# - homepage

def home(request):

    #return HttpResponse('hello world!')

  return render(request, 'meowapp/index.html')

# - Register a user

def register(request):

   form = Createuserform()
   if request.method == 'POST':
      form=Createuserform(request.POST)
      if form.is_valid():
         
         form.save()
         return redirect('my-login') 
         
          
   
   context={'form':form}
   
   return render(request,'meowapp/register.html',context=context)
   

# - login a user  

def my_login(request):

    form = loginform()

    if request.method == "POST":

       form = loginform(request, data=request.POST)

       if form.is_valid():
    
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)

                #return redirect('dashboard')

    context = {'form':form}

    return render(request, 'meowapp/my-login.html', context=context)

# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all() 
    context = {'records': my_records}

    return render(request, 'meowapp/dashboard.html', context=context)


@login_required(login_url='my-login')
def create_record(request):
    form=createrecord()
    if request.method == 'POST':
        form =createrecord(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'meowapp/create-record.html',context=context)

        


 

   


# - user logout

def user_logout(request):

    auth.logout(request)
    
    return redirect('my-login')














