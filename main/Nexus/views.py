from django.shortcuts import render
from .models import Nexus
from .forms import NexusForm,UserCreationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'Nexus/index.html')

def Nexus_list(request):
    nexus=Nexus.objects.all().order_by('created_at')
    return render(request,'Nexus/nexus_list.html',{'nexus':nexus})

@login_required
def Nexus_create(request):
    if request.method=='POST':
       form=NexusForm(request.POST,request.FILES)

       if form.is_valid():
           nexus=form.save(commit=False)
           nexus.user=request.user
           nexus.save()
           return redirect('Nexus:nexus_list')
    else:
        form=NexusForm()

    return render(request,'Nexus/nexus_form.html',{'form':form})  

@login_required
def Nexus_edit(request,nex_id):
    nexus=get_object_or_404(Nexus,pk=nex_id,user=request.user)

    if request.method=='POST':
        form=NexusForm(request.POST,request.FILES,instance=nexus)
        if form.is_valid():
           nexus=form.save(commit=False)
           nexus.user=request.user
           nexus.save()
           return redirect('Nexus:nexus_list')   
    else:
        form=NexusForm(instance=nexus)
    return render(request,'Nexus/nexus_form.html',{'form':form})

@login_required
def Nexus_delete(request,nex_id):
    nexus=get_object_or_404(Nexus,pk=nex_id,user=request.user) 
    if request.method=='POST':
        nexus.delete()
        return redirect('Nexus:nexus_list')
    return render(request,'Nexus/nexus_confirm_delete.html',{'nexus':nexus})

# @login_required
# def logout(request):
#     if request.method == "POST":
#       logout(request)
#       redirect('Nexus:logout')
#     return render(request,'Nexus/nexus_list.html')

def register(request):
    if request.method == 'POST':
       form=UserCreationForm(request.POST)
       if form.is_valid():
           user=form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request,user)
           return redirect('Nexus:nexus_list')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})


